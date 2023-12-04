# routing-demo-client
Python client for routing-demo

# Approach
Since the vehicle routing problem (VRP) is classified as a NP-hard problem it becomes necessary to use a heuristic
to implement a solution that will run in a reasonable amount of time as the number of nodes increase. The Heuristic used
is the Greedy Algorithm.

The driver with the highest suitability score is assigned to a destination. Then that driver cannot be assigned to another destination.
The next destination is then assigned the driver with the highest suitability score from the list of remaining drivers. This is
repeated until all destinations are assigned drivers or the list of drivers is exhausted.

## Requires the following run the application:
- Python3
- requests module

## If the requests module is not installed then run the below pip command:
pip install requests

## To run the routing-demo-client:
python3 routing-client.py destinations.txt drivers.txt

## Note:
Make sure https://github.com/markarmendariz/routing-demo is running before running routing-client

