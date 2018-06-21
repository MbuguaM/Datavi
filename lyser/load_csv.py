import csv

country = []
year = []
index = []
# openning the corruption index
def get_data(filename):
    """ getting the data from the csv files """
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            country.append(row[0])
        country.set()
        

           
    return 
get_data('Data/csv_data/corruption_index.csv')    
print(country)