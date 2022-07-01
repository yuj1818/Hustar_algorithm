
t = int(input())

for testcase in range(t):
    n, c = map(int, input().split())
    weight = list(map(int, input().split()))
    value = list(map(int, input().split()))
    D = []
    for i in range(n):
        D.append([])
        for j in range(c+1):
            D[i].append([])
            if weight[i] > j:
                if i == 0:
                    D[i][j] = 0
                else:
                    D[i][j] = D[i-1][j]
            else:
                if i == 0:
                    D[i][j] = value[i]
                else:
                    D[i][j] = max(D[i-1][j], D[i-1][j-weight[i]]+value[i])
    
    print(D[n-1][c])
    