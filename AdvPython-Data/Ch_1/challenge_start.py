# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1: How many quakes are there in total?

num_quakes = len(data['features'])
print(num_quakes)

# 2: How many quakes were felt by at least 100 people?

def get_felt_atleast100(q):
    if q['properties']['felt'] is not None and q['properties']['felt']>=100:
        return True
    return False

quakes_felt_100 = list(filter(get_felt_atleast100, data['features']))
print(len(quakes_felt_100))

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports

def getfelt(feature):
    felt =  feature['properties']['felt']
    if felt is None:
        felt=0
    return int(felt)
res3 = max(data['features'], key=getfelt)
print(f"Place: {res3['properties']['place']}, #reports: {res3['properties']['felt']}")

# 4: Print the top 10 most significant events, with the significance value of each

def getsignif(dataitem):
    significance = dataitem["properties"]["sig"]
    if (significance is None):
        significance = 0
    return int(significance)

data['features'].sort(key=getsignif, reverse=True)
for i in range(0,10):
    print(data['features'][i]['properties']['sig'])
