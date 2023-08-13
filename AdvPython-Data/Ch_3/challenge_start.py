# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import datetime
import json
import csv


# open the data file and load the JSON
with open("../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
def getsignif(q):
    return 0 if q['properties']['sig'] is None else q['properties']['sig']

sigevents = sorted(data["features"], key=getsignif, reverse=True)
sigevents = sigevents[:40]
sigevents.sort(key=lambda e: e["properties"]["time"], reverse=True)
header = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows = []

for event in sigevents:
    thedate = datetime.date.fromtimestamp(
        int(event["properties"]["time"]) / 1000)
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"

    rows.append([event["properties"]["mag"],
                event["properties"]["place"],
                0 if event["properties"]["felt"] is None else event["properties"]["felt"],
                thedate,
                gmaplink])

with open("significantevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)