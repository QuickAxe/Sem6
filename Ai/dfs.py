def DFS(vertices, edges, start, end):
    assert start in vertices, "Start must be a vertex"
    assert end in vertices, "End must be a vertex"

    def print_sol(current, start):
        if current == start:
            # print(f"{current} ", end="")
            return
        print_sol(parent[current], start)
        # print(f"-> {current} ", end="")

    def dfs_helper(current):
        visited.add(current)
        print(f"{current} visited!")

        # if current == end:
        #     # print("End reached!")
        #     return True

        for next_vertex in edges[current]:
            if next_vertex not in visited:
                parent[next_vertex] = current
                if dfs_helper(next_vertex):
                    return True

        return False

    parent = {}
    visited = set()
    dfs_helper(start)

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

DFS(Gvertices, Gedges, "A", "K")
