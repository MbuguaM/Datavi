import csv
# getting all the countries
def get_country(filename):
    """ getting all the countries as list """
    country = []
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            country.append(row[0])
        country = list(set(country))        
    return  sorted(country)


# filename = 'Data/csv_data/corruption_index.csv'
# countries = get_country(filename)


#getting the year and index dict
def yr_index_dict(countries, filename):
        final = [] 
        for country in countries:
            set_dict = {}
            with open(filename, 'r') as csvFile:
                csvFileReader = csv.reader(csvFile)
                next(csvFileReader) 
                for row in csvFileReader:
                    if country == row[0]:
                        year = row[2]
                        index = row[3]
                        first_dict ={year:index}
                        set_dict.update(first_dict)
                final_dict = {'country':country,'value':set_dict}
                final.append(final_dict) 
        final = {d.pop("country"): d.pop("value") for d in final}               
        return final

# final = yr_index_dict(countries,filename)
# year_list = list(final.values())
# print(year_list)
