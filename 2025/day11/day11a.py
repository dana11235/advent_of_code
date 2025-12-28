CONNECTIONS = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        source, sinks = [piece.strip() for piece in line.split(":")]
        CONNECTIONS[source] = sinks.split(" ")

print(CONNECTIONS)

CONNECTIONS["out"] = 0


def get_paths(path):
    last_node = path[-1]
    next_nodes = CONNECTIONS[last_node]
    for next_node in next_nodes:
        if next_node == "out":
            CONNECTIONS["out"] += 1
        else:
            new_path = path[:]
            new_path.append(next_node)
            get_paths(new_path)


get_paths(["you"])

print(CONNECTIONS["out"])
