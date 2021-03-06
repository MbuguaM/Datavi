from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .models import counties, WordBorder
from django.core.serializers import serialize
from django.http import HttpResponse
from . import views
from .forms import SignUpForm
from django.contrib.auth import login
from .tokens import account_activation_token
from django.contrib.auth.models import User
# decorator
from django.contrib.auth.decorators import login_required
# importing economics and perception index infomation 
from .load_csv import get_country, yr_index_dict
from .load_json import load


# Create your views here.
def landing(request):
    """ models displaying the main landing page """
    return render (request, 'app_temp/home.html')

def more_about(request):
    """ displaying more inforamtion about us """
    return render(request, 'app_temp/us.html')

def stories(request):
    """displaying map projection"""
    return render(request, 'app_temp/stories.html')

def projection(request):
    """displaying map projection"""
    return render(request, 'app_temp/projection.html')


@login_required(login_url='/accounts/login/')
def your_projection(request):
    """displaying map projection"""
    gdp_file = './Data/csv_data/gdp.json'
    corruption_file = './Data/csv_data/corruption_index.csv'
    countries = get_country(corruption_file)
    gdp_data = load(gdp_file)
    corruption_data = yr_index_dict(countries,corruption_file)

    return render(request, 'app_temp/projection.html', {'gdp':gdp_data, 'corruption':corruption_data})


def signup(request):
    """ registration for the user """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Data-X Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
        print(form)
    return render(request, 'registration/reg_form.html', {'form': form})

def account_activation_sent(request):
    """ view function to redirect user to the user registration complete page """
    current_user = request.user
    if current_user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'registration/account_activation_complete.html')

def activate(request, uidb64, token):
    """ funtction to authenticate user activation from the email """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('landing')
    else:
        return render(request, 'registration/account_activation_invalid.html')
        
def documentation(request):
    """displaying detailed map infomation"""
    return render(request, 'app_temp/Documentation.html')


# Provider urls ( urls for providing geometric data)
def county_data(request):
    """ fetching the county data """
    county = serialize('geojson',counties.objects.all())
    return HttpResponse(county, content_type = 'json')

def world_borders(request):
    """ fetching the world borders data"""
    world_borders = serialize('geojson',WordBorder.objects.all())
    return HttpResponse(world_borders, content_type = 'json')
