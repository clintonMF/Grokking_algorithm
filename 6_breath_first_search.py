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
# false
def ends_in_a(name):
    return name[-1] == "a"

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