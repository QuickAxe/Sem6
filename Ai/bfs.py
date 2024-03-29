from queue import Queue


def BFS(vertices, edges, start, end):
    assert start in vertices, "Start must be a vertex"
    assert end in vertices, "End must be a vertex"

    def print_sol(current, start):
        if current == start:
            # print(f"{current} ", end="")
            return
        print_sol(parent[current], start)
        # print(f"-> {current} ", end="")
        return

    parent = {}
    q = Queue()
    q.put(start)
    while not q.empty():
        current = q.get()
        if current in parent.values():
            continue
        print(f"{current} visited!")
        # if current == end:
        #     print("End reached!")
        #     break
        for next in edges[current]:
            if next not in parent.keys():
                parent[next] = current
                q.put(next)
    if end in parent:
        print_sol(end, start)


Gvertices = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"}
Gedges = {
    "A": ["B", "C", "D"],
    "B": ["A", "E", "F", "C"],
    "C": ["A", "B", "F", "G"],
    "D": ["A", "G"],
    "E": ["B", "H"],
    "F": ["B", "C", "G", "H", "I"],
    "G": ["C", "F", "D", "I"],
    "H": ["E", "F", "I", "K", "J"],
    "I": ["F", "G", "H", "K"],
    "J": ["H"],
    "K": ["H", "I"],
}

BFS(Gvertices, Gedges, "A", "K")
