t = int(input())

for testcase in range(t):
    n, m = map(int, input().split())
    answer = []
    for i in range(n):
        answer.append([])
    for j in range(m):
        u, v = map(int, input().split())
        answer[u].append(v)
        answer[v].append(u)
        
    for k in range(n):
        answer[k].sort()
        print(*answer[k])
        
