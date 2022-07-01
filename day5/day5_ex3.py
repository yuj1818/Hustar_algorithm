
t = int(input())

for testcase in range(t):
    n, m = map(int, input().split())
    p = [[]*m for _ in range(n)]
    mp = [[0]*m for _ in range(n)]
    for x in range(len(p)):
        p[x] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                mp[i][j] = p[i][j]
            elif i == 0 and j > 0:
                mp[i][j] = mp[i][j-1] + p[i][j]
            elif i > 0 and j == 0:
                mp[i][j] = mp[i-1][j] + p[i][j]
            elif i > 0 and j > 0:
                mp[i][j] = min(mp[i-1][j], mp[i][j-1], mp[i-1][j-1])+p[i][j]
        
    print(mp[n-1][m-1])