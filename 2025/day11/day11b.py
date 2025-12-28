CONNECTIONS = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        source, sinks = [piece.strip() for piece in line.split(":")]
        CONNECTIONS[source] = sinks.split(" ")

PATHS = {}

SPECIAL_NODES = ["out", "fft", "dac", "svr"]


def count_paths(path, destination):
    last_node = path[-1]
    count = 0
    for next_node in CONNECTIONS[last_node]:
        if next_node in PATHS:
            count += PATHS[next_node]
        elif next_node == destination:
            count += 1
        else:
            if next_node not in path and next_node not in SPECIAL_NODES:
                new_path = path[:]
                new_path.append(next_node)
                count += count_paths(new_path, destination)
    PATHS[last_node] = count
    return count


RESULTS = {}
PATHS = {}
RESULTS["svr_fft"] = count_paths(["svr"], "fft")
PATHS = {}
RESULTS["svr_dac"] = count_paths(["svr"], "dac")
PATHS = {}
RESULTS["dac_fft"] = count_paths(["dac"], "fft")
PATHS = {}
RESULTS["fft_dac"] = count_paths(["fft"], "dac")
PATHS = {}
RESULTS["dac_out"] = count_paths(["dac"], "out")
PATHS = {}
RESULTS["fft_out"] = count_paths(["fft"], "out")

result = (
    RESULTS["svr_fft"] * RESULTS["fft_dac"] * RESULTS["dac_out"]
    + RESULTS["svr_dac"] * RESULTS["dac_fft"] * RESULTS["fft_out"]
)
print("paths", result)
