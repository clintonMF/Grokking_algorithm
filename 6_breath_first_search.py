# What is a graph?
# A graph models a set of connections.
# Graphs are made up of nodes and edges. A node
# can be directly connected to many other nodes. hose nodes are called
# its neighbors.
# Graphs are a way to model how diferent things are connected to one
# another. Now let’s see breadth-irst search in action.

# Breadth-irst search
# We looked at a search algorithm in chapter 1: binary search. Breadthirst
# search is a diferent kind of search algorithm: one that runs on
# graphs. It can help answer two types of questions:
# • Question type 1: Is there a path from node A to node B?
# • Question type 2: What is the shortest path from node A to node B?

# Queue and stack
# he queue is called a FIFO data structure: First In, First Out. In
# contrast, a stack is a LIFO data structure: Last In, First Out.

# implementing a graph
# example: if theres a graph in which you are connected to 3 people named
# Goku, Gohan, Vegita. the graph of this connection is shown below

graph = {}
graph["you"] = ["Goku","Gohan", "Vegita"]

# if vegeta was also connected to Trunks and bulma
# goku also connected to chichi and gotenks
# Gohan is connected to chichi

graph["Goku"] = ["chichi","gotenk"]
graph["Gohan"] = ["chichi"]
graph["Vegita"] = ["bulma", "trunks"]
graph["chichi"] = ["Goku"]
graph["bulma"] = ["Vegita"]
graph["trunks"] = []
graph["gotenk"] = []

# implementing breath first search
from collections import deque

# in this search we want to find your cl0sest friend whose name ends in "a"
# the function below prints True if the name ends in a, otherwise it prints 
# 
def ends_in_a(name):
    return name[-1] == "a"


# below is the pseudo code or algorithm for the breath first search

# while queue is not empty
# get the leftmost member of the queue and check if it ends in a. given that it has not been processed before
# if yes thats what we are looking for end the loop
# if not add the members of this member to the queue
# if the queue is empty return none


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        
        if person not in searched:
            if ends_in_a(person):
                print(f"{person} ends in \"A\"")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print(searched)
    return False

print(search("Vegita"))

# A tree is a special type of graph, where no edges
# ever point back.


# the algorithm can also be done without importing deque
# below lies the code for that algorithm

def ends_with_f(node):
    return node[-1] == "f"

def add_element_in_node(search_queue, node):
    for n in graph[node]:
        search_queue.append(n)
    return search_queue

def shortest_path(node):
    search_queue = []
    search_queue = add_element_in_node(search_queue, node)
    searched = []
    
    while search_queue:
        cur_node = search_queue.pop()
        
        if ends_with_f(cur_node) and cur_node not in searched:
            print(cur_node, "ends with F")
            return cur_node
        else:
            search_queue = add_element_in_node(search_queue, cur_node)
            searched.append(cur_node)
    else:
        return None
    
shortest_path("start")
