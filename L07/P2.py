from collections import deque

def P2_route(map_fname, start, goal):
    # สร้างกราฟจากไฟล์
    graph = {}
    with open(map_fname, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # แยกชื่อเมืองและส่วน neighbors
            main_parts = line.split(";")
            town_part = main_parts[0].split(":")
            town = town_part[0].strip()
            graph.setdefault(town, [])

            if len(main_parts) > 1:
                neighbors_part = main_parts[1].strip()
                # แยก neighbors ด้วย comma
                neighbors_list = neighbors_part.split(",")
                for n in neighbors_list:
                    # แยกชื่อเมืองออกจากระยะทาง
                    n_name = n.split(":")[0].strip()
                    graph[town].append(n_name)
                    graph.setdefault(n_name, []).append(town)  # undirected

    # BFS หาเส้นทางผ่านเมืองน้อยที่สุด
    if start == goal:
        return start

    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city == goal:
            return " - ".join(path)

        if city not in visited:
            visited.add(city)
            for neighbor in graph.get(city, []):
                if neighbor not in path:
                    queue.append(path + [neighbor])

    return "No route found"

if __name__ == "__main__":
    r = P2_route("P2romania.txt", "Arad", "Bucharest")
    print(r)
