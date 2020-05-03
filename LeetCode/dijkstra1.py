def findMinIndex(findArray, notIn):
    min_val = 1000000000
    ind = 1000000000

    for j in range(len(findArray)):
        if findArray[j] < min_val and j not in notIn:
            min_val = findArray[j]
            ind = j

    return ind


if __name__ == "__main__":
    n, start, final = input().split()
    n, start, final = int(n), int(start) - 1, int(final) - 1

    matrix = []
    for i in range(n):
        row = input().split()
        for colNum in range(n):
            row[colNum] = int(row[colNum])
        matrix.append(row)

    saw = set()
    d = [1000000000] * n
    d[start] = 0
    nowAt = findMinIndex(d, saw)

    while (nowAt != 1000000000):
        saw.add(nowAt)

        for i in range(n):
            if matrix[nowAt][i] != 0 and matrix[nowAt][i] != -1:
                newVal = d[nowAt] + matrix[nowAt][i]
                d[i] = newVal if newVal < d[i] else d[i]
        nowAt = findMinIndex(d, saw)

    print(d[final] if d[final] != 1000000000 else -1)

