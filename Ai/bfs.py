from queue import Queue

graph = {
    "a": ["b", "c", "d"],
    "b": ["a", "e", "h"],
    "c": ["a", "f", "g"],
    "d": ["a", "g"],
    "e": ["b", "h"],
    "f": ["c"],
    "g": ["c", "d"],
    "h": ["b", "e"],
}

visited = []
que = Queue()


root = "a"
que.put(root)

while not que.empty():
    node = que.get()

    if node not in visited:
        visited.append(node)

        for subNode in graph[node]:
            if subNode not in visited:
                que.put(subNode)

print(visited)

visitedDfs = []


def Dfs(node):
    
    visitedDfs.append(node)
    
    for n in graph[node]:
        
