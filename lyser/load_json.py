import json
from pprint import pprint

def load(filename):
    with open(filename) as f:
        data = json.load(f)
    parsed_data = {n.pop('Country Name'):n for n in data}
    # with open('parsed_gdp.json', 'w') as  n :
    #     n.write(json.dumps(parsed_data))
    return parsed_data
# filename = 'Data/csv_data/gdp.json'

# parsed_data = load(filename)
#file starts form 1960 - 2016
# print(parsed_data.get('Aruba').get('1995'))