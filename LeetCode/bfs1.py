if __name__ == "__main__":
    n = int(input())  # vertexes amount

    matrix = []
    for i in range(n):
        row = input().split()
        for j in range(n):
            row[j] = int(row[j])
        matrix.append(row)
    
    fromV, to = input().split()
    fromV, to = int(fromV) - 1, int(to) - 1
    depth = []
    path = [-1] * n
    visited = set()

    queue = set()
    queue.add(fromV)
    while queue:
        now = queue.pop()
        visited.add(now)
    
        for i in range(n):
            if matrix[now][i] and i not in visited:
                visited.add(i)
                queue.add(i)
                path[i] = now
            print(queue)

    print(path)
    if to not in visited:
        print(-1)
    else:
        localPath = []
        v = to
        while path[v] != -1:
            localPath.append(path[v])
            v = path[v]
    
        print(localPath)
    
