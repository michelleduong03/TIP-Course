# Problem 1: Graphing Flights

"""
The following graph represents the different flights offered by CodePath Airlines. 
Each node or vertex represents an airport (JFK - New York City, LAX - Los Angeles, 
DFW - Dallas Fort Worth, and ATL - Atlanta), and an edge between two vertices 
indicates that CodePath airlines offers flights between those two airports.

Create a variable flights that represents the undirected graph below as an adjacency 
dictionary, where each node's value is represented by a string with the airport's 
name (ex. "JFK").

flights graph
"""
"""
JFK ----- LAX
|
|
DFW ----- ATL
"""
# No starter code is provided for this problem
# Add your code here
flights = {
    "JFK": ["LAX", "DFW"],
    "LAX": ["JFK"],
    "DFW": ["ATL", "JFK"],
    "ATL": ["DFW"]
}

# Example Usage:

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])

# Example Output:

# ['JFK', 'LAX', 'DFW', 'ATL']
# [['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
# ['LAX', 'DFW']
# 💡 Hint: Introduction to Graphs



# Problem 2: There and Back

"""
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency 
list flights with n nodes where each node represents the ID of a different destination 
and flights[i] is an integer array indicating that there is a flight from destination 
i to each destination in flights[i]. Write a function bidirectional_flights() that 
returns True if for every flight from a destination i to a destination j there also 
exists a flight from destination j to destination i. Return False otherwise.
"""

def bidirectional_flights(flights):
    for i in range(len(flights)):
        for j in flights[i]:
            if i not in flights[j]:
                return False
    return True


# Example Usage:

# Example 1: flights1

# 'flights1' graph diagram

# Example 2: flights2'flights2' graph diagram

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

# Example Output:

# True
# False



# Problem 3: Finding Direct Flights

"""
Given an adjacency matrix flights of size n x n where each of the n nodes in the 
graph represent a distinct destination and n[i][j] = 1 indicates that there exists 
a flight from destination i to destination j and n[i][j] = 0 indicates that no such 
flight exists. Given flights and an integer source representing the destination a 
customer is flying out of, return a list of all destinations the customer can reach 
from source on a direct flight. You may return the destinations in any order.

A customer can reach a destination on a direct flight if that destination is a neighbor of source.
"""

def get_direct_flights(flights, source):
    direct_destinations = []
    for i in range(len(flights[source])):
        if flights[source][i] == 1:
            direct_destinations.append(i)
    return direct_destinations

# Example Usage:

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
# Example Output:

# [0, 1, 3]
# []




# Problem 4: Converting Flight Representations

"""
Given a list of edges flights where flights[i] = [a, b] denotes that there exists 
a bidirectional flight (incoming and outgoing flight) from city a to city b, return 
an adjacency dictionary adj_dict representing the same flights graph where adj_dict[a] 
is an array denoting there is a flight from city a to each city in adj_dict[a].
"""

def get_adj_dict(flights):
    adj_dict = {}

    for a, b in flights:
        # Make sure a is in dictionary
        if a not in adj_dict:
            adj_dict[a] = []
        # Make sure b is in dictionary
        if b not in adj_dict:
            adj_dict[b] = []

        # Add each direction because flights are bidirectional
        adj_dict[a].append(b)
        adj_dict[b].append(a)

    return adj_dict


# Example Usage:

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))

# Example Output:

# {
#     'Cape Town': ['Addis Ababa', 'Cairo'],
#     'Addis Ababa': ['Cape Town', 'Lagos'],
#     'Lagos': ['Cairo', 'Addis Ababa'],
#     'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
#     'Nairobi': ['Cairo']
# }
# 💡 Hint: Converting Between Graph Representations




# Problem 5: Find Center of Airport

"""
You are a pilot navigating a new airport and have a map of the airport represented 
as an undirected star graph with n nodes where each node represents a terminal in 
the airport labeled from 1 to n. You want to find the center terminal in the airport 
where the pilots' lounge is located.

Given a 2D integer array terminals where each terminals[i] = [u, v] indicates that 
there is a path (edge) between terminal u and v, return the center of the given airport.

A star graph is a graph where there is one center node and exactly n-1 edges 
connecting the center node ot every other node.
"""

def find_center(terminals):
    pass

# Example Usage:

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))

# Example Output:

# 2
# 1