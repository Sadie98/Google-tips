if __name__ == "__main__":
    n, s = input().split()
    n = int(n)
    s = int(s) - 1  # since they gives numeration from 1, but I’m not
    matrix = []

    for i in range(n):
        matrix.append(input().split())
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    queue = set()
    visited = set()

    queue.add(s)
    while queue:
        nowAt = queue.pop()
        visited.add(nowAt)

        for i in range(n):
            if matrix[nowAt][i] == 1 and i not in visited:
                queue.add(i)

    print(len(visited))
