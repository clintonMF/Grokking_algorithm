states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

############################################################
# Explanation of the greedy algorithm used below.
# ----------------------------------------------------------
# this algorithm is used to pick the least number of stations required
# to cover a given number of states

# it is preferable to put the list of states and stations in sets rather than
# a list. This is because set have some unique operations that are needed in
# this algorithm. such operations include difference and intersection.

# The algorithm
# Get the number of states_needed (these are the states that are not yet
# covered but needed).
# while states_needed is not empty
    # loop through the stations to get the station and the states each covers

        # get the intersection of the states_needed and those covered by the station
        # call it covered.
        
        # if length of covered is greater than the length_covered
        # length_covered is a variable that holds the length of the station that 
        # currently covers the most states. You should create it before the for loop
        # give it a value of 0. 
            # length_covered = length of covered
            # best_station (the station that covers the most uncovered states) = station
            # covered_states = covered (holds the states covered by the best_station)
    # add the best_station to the required states list
    # states_needed is updated by removing the list of covered states from states_needed.
    # in code: states_needed = states_needed - covered_states

#  return the required states
############################################################

def greedy_algo(stations, states_needed):
    """This is a function that minimizes the number of station required to
    reach audience in a given number of states."""
    required_states = [] #the minimum number of states needed
    while states_needed:
        length_covered = 0
        for station, states_covered in stations.items():
            covered = states_covered & states_needed
            if len(covered) > length_covered:
                length_covered = len(covered)
                best_station = station 
                # the station that currently covers the most states
                covered_states = covered
        required_states.append(best_station)
        states_needed = states_needed - covered_states
        # the minus sign is a set operation that finds the difference between
        # states_needed and those covered. these are the states that are 
        # uncovered but needed.
    return required_states

print(greedy_algo(stations, states_needed)) 