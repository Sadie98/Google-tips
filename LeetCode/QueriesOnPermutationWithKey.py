queries = [7,5,5,8,3]
m = 8

p = list(range(1, m + 1))

ans = []
for i in range(len(queries)):
    for pFindIndex in range(m):
        if queries[i] == p[pFindIndex]:
            ans.append(pFindIndex)

            insert = p[pFindIndex]
            for j in reversed(range(1, pFindIndex + 1)):
                p[j] = p[j - 1]
            p[0] = insert
print(ans)