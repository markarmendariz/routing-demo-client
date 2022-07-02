import requests
import csv
import sys

# Load destinations
def load_destinations(street_filename):
    street_list = []
    with open(street_filename, mode='r') as street_file:
        street_reader = csv.DictReader(street_file)
        line_count = 0
        for row in street_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(row["street name"])
            street_list.append(row["street name"])
            line_count += 1
        print(f'Processed {line_count} street records.')

    return street_list    

# Load drivers
def load_drivers(drivers_filename):
    driver_list = []
    with open(drivers_filename, mode='r') as drivers_file:
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

    return driver_list

# Main
def main(destination_filename, driver_filename):
    # URL to routing-demo service
    URL = "http://localhost:8080/calculateSS"

    # Load destinations
    street_list = load_destinations(sys.argv[1])
    print(street_list)

    # Load drivers
    driver_list = load_drivers(sys.argv[2])

    print(driver_list)

    # Determine the suitability score for each street per driver
    for i in range(len(street_list)):
        total_score = 0
        for j in range(len(driver_list)):
            PARAMS = {
                'street' :street_list[i],
                'driver': driver_list[j]
            }

            resp = requests.get(url = URL, params = PARAMS)
            data = resp.json()

            print(f'Street: {street_list[i]} and Driver: {driver_list[j]} has a SS of: {data["score"]}')
            total_score = total_score + data["score"]
        
        print(f'Total SS    : {total_score}')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python3 routing-client.py destinations.txt drivers.txt")
        exit(1)

    main(sys.argv[1], sys.argv[2])




    