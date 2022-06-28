import requests
import csv
import sys

# URL to routing-demo service
URL = "http://localhost:8080/calculateSS"

if len(sys.argv) < 3:
    print("usage: python3 routing-client.py address.txt drivers.txt")
    exit(1)

# Load street for deliveries
street_list = []
with open(sys.argv[1], mode='r') as address_file:
    address_reader = csv.DictReader(address_file)
    line_count = 0
    for row in address_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(row["street name"])
        street_list.append(row["street name"])
        line_count += 1
    print(f'Processed {line_count} street records.')

print(street_list)

# Load drivers
driver_list = []
with open(sys.argv[2], mode='r') as drivers_file:
    drivers_reader = csv.DictReader(drivers_file)
    line_count = 0
    for row in drivers_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(row["driver"])
        driver_list.append(row["driver"])
        line_count += 1
    print(f'Processed {line_count} driver records.')

print(driver_list)

# Determine the suitability score for each street per driver
for i in range(len(street_list)):
    for j in range(len(driver_list)):
        PARAMS = {
            'street' :street_list[i],
            'driver': driver_list[j]
        }

        resp = requests.get(url = URL, params = PARAMS)
        data = resp.json()

        print(f'Street: {street_list[i]} and Driver: {driver_list[j]} has a SS of: {data["score"]}')

'''
TODO:
Now that there is a suitability score for each street per driver the next step is to determine the combination of suitability scores
when added together gives highest total score so as to maximize the total score over the set of drivers adhering to the rule that each
driver can have only one shipment and each shipment can can only be assiged to one driver. Unfortunately I ran out of time to implement
this part.
'''




    