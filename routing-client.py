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

# See if driver already assigned
def is_driver_assigned(assignments, driver):
    for i in range(len(assignments)):
        if assignments[i]["driver"] == driver:
            return True

    return False

# Assign drivers using the Greedy Algorithm heuristic. A driver with highest suitability score is
# assigned to a destination. Then that driver cannot be assigned to destination. The next destination
# is then assigned the driver with the highest suitability score from the list of remaining drivers. This is
# repeated until all drivers are assigned drivers or the list of drivers is exhausted.
def assign_drivers(street_list, driver_list):
    # URL to routing-demo service
    URL = "http://localhost:8080/calculateSS"

    assignments = []
    for i in range(len(street_list)):
        destination_dict = {"street": street_list[i], "driver": "", "score": 0}
        for j in range(len(driver_list)):
            if is_driver_assigned(assignments, driver_list[j]):
                continue

            PARAMS = {
                'street' :street_list[i],
                'driver': driver_list[j]
            }

            resp = requests.get(url = URL, params = PARAMS)
            data = resp.json()

            print(f'Street: {street_list[i]} and Driver: {driver_list[j]} has a SS of: {data["score"]}')

            if destination_dict["score"] < data["score"]:
                destination_dict["score"] = data["score"]
                destination_dict["driver"] = driver_list[j]

        assignments.append(destination_dict)
        print(destination_dict)

    return assignments

def print_assignments(assignments):
    # Print assignments
    total_score = 0
    for i in range(len(assignments)):
        street = assignments[i]["street"]
        driver = assignments[i]["driver"]
        score = assignments[i]["score"]
        total_score += score
        print(f'Destination [{street}] is assigned driver [{driver}] with a score of [{score}]')
    
    # Print the total suitability score
    print(f'The suitability score is [{total_score}]')

# Main
def main(destination_filename, driver_filename):
    # Load destinations
    street_list = load_destinations(sys.argv[1])
    print(street_list)

    # Load drivers
    driver_list = load_drivers(sys.argv[2])

    print(driver_list)

    # Determine the suitability score for each street per driver
    assignments = assign_drivers(street_list, driver_list)
    
    # Print assignments
    print_assignments(assignments)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python3 routing-client.py destinations.txt drivers.txt")
        exit(1)

    main(sys.argv[1], sys.argv[2])




    