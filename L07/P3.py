import heapq

def P3_route(map_fname, start, goal):
    graph = {}
    with open(map_fname, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(";")
            town_name = parts[0].split(":")[0].strip()
            graph.setdefault(town_name, {})

            if len(parts) > 1:
                neighbors_str = parts[1].strip()
                neighbors_list = neighbors_str.split(",")
                for n in neighbors_list:
                    n_parts = n.split(":")
                    neighbor_name = n_parts[0].strip()
                    distance = int(n_parts[1].strip())
                    graph[town_name][neighbor_name] = distance
                    if neighbor_name not in graph:
                        graph[neighbor_name] = {}
                    if town_name not in graph[neighbor_name]:
                        graph[neighbor_name][town_name] = distance


    queue = []
    heapq.heappush(queue, (0, [start]))  
    visited = set()

    while queue:
        cost_so_far, path = heapq.heappop(queue)
        city = path[-1]

        if city == goal:
            return " - ".join(path)

        if city not in visited:
            visited.add(city)
            for neighbor, dist in graph.get(city, {}).items():
                if neighbor not in path:
                    heapq.heappush(queue, (cost_so_far + dist, path + [neighbor]))

    return "No route found"

if __name__ == "__main__":
    r = P3_route("P2romania.txt", "Arad", "Bucharest")
    print(r)
