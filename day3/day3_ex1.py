def Matrix(n):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(0)
    return mat
    

t = int(input())

for testcase in range(t):
    n, m = map(int, input().split())
    answer = Matrix(n)
    for line in range(m):
        u, v, c = map(int, input().split())
        answer[u][v] = c
    for i in range(n):
        print(*answer[i])
    