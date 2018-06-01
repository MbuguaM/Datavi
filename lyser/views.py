from django.shortcuts import render

# Create your views here.
def landing(request):
    """ models displaying the main laning page """
    return render (request, 'app_temp/landing.html')