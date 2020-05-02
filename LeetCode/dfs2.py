if __name__ == "__main__":
    n, m = input().split()
    n, m = int(n), int(m)

    components = []
    vertexes = {}
    
    for vertex in range(1, n + 1):
        vertexes[vertex] = -1
    
    for i in range(m):
        fromV, to = input().split()
        fromV, to = int(fromV), int(to)

        if vertexes[fromV] == -1 and vertexes[to] == -1:
            components.append({fromV, to})
            vertexes[to] = len(components) - 1
            vertexes[fromV] = len(components) - 1
        elif vertexes[fromV] != -1 and vertexes[to] == -1:
            vertexes[to] = vertexes[fromV]
            components[vertexes[to]].add(to)
        elif vertexes[to] != -1 and vertexes[fromV] == -1:
            vertexes[fromV] = vertexes[to]
            components[vertexes[fromV]].add(fromV)
        elif vertexes[to] != -1 and vertexes[fromV] != -1 and vertexes[to] != vertexes[fromV]:
            toCopy = components[vertexes[to]].copy()
            components[vertexes[fromV]] = components[vertexes[fromV]].union(toCopy)
            components[vertexes[to]] = {}

            for vertexToChange in toCopy:
                vertexes[vertexToChange] = vertexes[fromV]

    for vertex in range(1, n + 1):
        if vertexes[vertex] == -1:
            components.append({vertex})
            vertexes[vertex] = len(components) - 1

    while {} in components:
        components.remove({})

    print(len(components))
    for component in components:
        print(len(component))
        print(' '.join(list(map(str, component))))
