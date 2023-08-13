# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json


# open the data file and load the JSON
with open("../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

from collections import defaultdict
d = defaultdict(int)

for feature in data['features']:
    d[feature['properties']['type']]+=1

for k,v in d.items():
    print(f"{k}: {v}")