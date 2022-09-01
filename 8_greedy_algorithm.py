states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


def greedy_algo(stations, states_needed):
    required_states = []
    while states_needed:
        print(states_needed)
        length_covered = 0
        for station, states_covered in stations.items():
            covered = states_covered & states_needed
            if len(covered) > length_covered:
                length_covered = len(covered)
                best_station = station
                covered_states = covered
        required_states.append(best_station)
        states_needed = states_needed - covered_states
    
    return required_states

print(greedy_algo(stations, states_needed)) 