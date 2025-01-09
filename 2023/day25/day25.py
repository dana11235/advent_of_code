import math
import heapq
import random
import time
connection_list = []
CONN = {}
START_NODE = 'pdm'
INPUT_FILE = 'day25_input.txt'
with open(INPUT_FILE, 'r') as file:
    for line in file:
        source = line[0:3]
        destinations = line[5:].split()
        if source not in CONN:
            CONN[source] = []
        for destination in destinations:
            CONN[source].append(destination)
            connection_list.append([source, destination])
            if destination not in CONN:
                CONN[destination] = []
            CONN[destination].append(source)
keys = list(CONN.keys())
num_nodes = len(keys)
print('nodes', num_nodes)

# This function will explore a node, and return the number of nodes connected to it.
# Can be used to verify that the network has been partitioned


def explore(start_node, cut_nodes):
    visited_nodes = []
    nodes_to_visit = [start_node]
    while len(nodes_to_visit) > 0:
        node = nodes_to_visit.pop(0)
        if node not in visited_nodes:
            visited_nodes.append(node)
            for child_node in CONN[node]:
                if child_node not in visited_nodes and [node, child_node] not in cut_nodes and [child_node, node] not in cut_nodes:
                    nodes_to_visit.append(child_node)
    return len(visited_nodes)


PATHS = {}


def get_key(node1, node2):
    return f"{node1}-{node2}"


def find_path(node1, node2):
    # If we have solved this previously, return the answer
    solution = get_key(node1, node2)
    if solution in PATHS:
        return PATHS[solution]
    inv_solution = get_key(node2, node1)
    if inv_solution in PATHS:
        inv = PATHS[inv_solution].copy()
        inv.reverse()
        return inv

    visited_nodes = []
    # We use a minpq so that we expand smallest paths first (BFS)
    to_visit = []
    heapq.heapify(to_visit)
    heapq.heappush(to_visit, (1, random.random(), node1, [node1]))
    candidate = None

    while len(to_visit) > 0:
        next = heapq.heappop(to_visit)
        node = next[2]
        path = next[3]
        # We only want to use the candidate if it is less than or equal to the current path
        if candidate and len(path) >= len(candidate):
            return candidate

        # We should only visit a node once per crawl
        if node not in visited_nodes:
            visited_nodes.append(node)
            connections = CONN[node]
            # If the terminal node is in the list of connections, we can stop
            if node2 in connections:
                path.append(node2)
                # Add this key to the paths
                key = get_key(node1, node2)
                if key not in PATHS:
                    PATHS[key] = path

                return path
            else:
                for connection in connections:
                    path_key = get_key(connection, node2)
                    if path_key in PATHS:
                        completed_path = path + PATHS[path_key]
                        # If we find a path from the current node to the end, we can consider it
                        # We don't return this immediately, because there could be a shorter path
                        if not candidate or len(completed_path) < len(candidate):
                            candidate = completed_path
                    else:
                        # If this node doesn't compelte the puzzle, extend the path and add it to the PQ
                        new_path = path.copy()
                        new_path.append(connection)
                        heapq.heappush(
                            to_visit, (len(path), random.random(), connection, new_path))
    return candidate


def n_choose_k(n, k):
    return round(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


print('number', n_choose_k(num_nodes, 2))
FREQS = {}
n = 0
last_time = time.time()
for index in range(num_nodes - 1):
    for index2 in range(index + 1, num_nodes):
        n += 1
        # Some quick status info, because this code runs pretty slowly
        if n % 1000 == 0:
            num_keys = len(list(PATHS.keys()))
            curr_time = time.time()
            elapsed = curr_time - last_time
            last_time = curr_time
            print(f"iter: {n}, keys: {num_keys}, time: {elapsed}")
        node1 = keys[index]
        node2 = keys[index2]
        path = find_path(node1, node2)
        for i in range(len(path) - 1):
            pair = [path[i], path[i+1]]
            pair.sort()
            key = f"{pair[0]}-{pair[1]}"
            if key not in FREQS:
                FREQS[key] = 1
            else:
                FREQS[key] += 1

sorted_dict = dict(sorted(FREQS.items(), key=lambda item: item[1]))
NUM_CANDIDATES = 7
num_destinations = explore(START_NODE, [])
candidates = list(sorted_dict.keys())[-1 * NUM_CANDIDATES:]
for index1 in range(0, NUM_CANDIDATES - 1):
    for index2 in range(index1 + 1, NUM_CANDIDATES - 1):
        for index3 in range(index2 + 1, NUM_CANDIDATES):
            to_cut = [candidates[index1].split(
                '-'), candidates[index2].split('-'), candidates[index3].split('-')]
            num_new_destinations = explore(START_NODE, to_cut)
            if num_new_destinations < num_destinations:
                print('connections cut', to_cut)
                print('answer', num_new_destinations *
                      (num_destinations - num_new_destinations))
