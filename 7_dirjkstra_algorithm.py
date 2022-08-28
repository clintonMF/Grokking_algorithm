# In the last chapter, you used breadth-irst search to ind the shortest
# path between two points. Back then, “shortest path” meant the path
# with the fewest segments. But in Dijkstra’s algorithm, you assign a
# number or weight to each segment. hen Dijkstra’s algorithm inds the
# path with the smallest total weight.

# To calculate the shortest path in an unweighted graph, use breadth-irst
# search. To calculate the shortest path in a weighted graph, use Dijkstra’s
# algorithm. 
# 
# Graphs can also have cycles. A cycle looks like this.It means you can start
# at a node, travel around, and end up at the same node.

# An undirected graph means that both nodes point to each other. hat’s
# a cycle! With an undirected graph, each edge adds another cycle.
# Dijkstra’s algorithm only works with directed acyclic graphs,
# called DAGs for short.

# The key or major idea behing the dijkstra's algorithm is the fact that 
# after finding the cheapest node there is no cheaper way to get to that same]
# node.

# NOTE: Negative-weight edges break the algorithm.

# implementation of dijkstra's algorithm

import json
# creating the graph
graph = {}
graph["start"] = {} 
graph["start"]["a"] = 6     
graph["start"]["b"] = 2     

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")

# creating the cost table
costs = {}
costs["start"] = 1
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# creating the parent table
parent = {}
parent["start"] = "j"
parent["a"] = "start"
parent["b"] = "start"
parent["fin"] = None


############################################################
# Algorithm for finding the lowest cost
# ----------------------------------------------------------
# loop through the keys of the costs
# get the cost of each node
# if it is less than the lowest cost and has not been processed 
# make it the new lowest cost
# update the lowest node to the current node
# finally return lowest cost
############################################################

processed = []
def find_lowest_cost(costs):
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs:
        new_cost = costs[node]
        if lowest_cost > new_cost and node not in processed:
            lowest_cost = new_cost
            lowest_node = node
    return lowest_node


def dirjkstra_algo(costs):
    node = find_lowest_cost(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node] #start is here 
        
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = find_lowest_cost(costs)
        
    return f"{parent} - parent\n{costs} - costs"
        
print(dirjkstra_algo(costs))
# print(json.dumps(graph, indent=4))

# the new parent table gotten after running the algorithm shows the 
# path that minimizes cost the most.
# from the result we can see that the node before "fin" should be "a"
# and the node to "a"" should be "b", while the node to "b" - "start"
# Hence the pathway is: start => b => a => finish