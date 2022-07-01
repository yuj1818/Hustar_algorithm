from collections import deque

t = int(input())

for testcase in range(t):
    n, m, k = map(int, input().split())
    queue = deque([k])
    check = [False]*n
    List = [[] for _ in range(n)]
    for con in range(m):
        u, v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
    
    for i in range(n):
        List[i].sort()
        
    while queue:
        a = queue.popleft()
        if check[a] == True:
            continue
        check[a] = True
        for i in List[a]:
            if check[i] == False:
                queue.append(i)
    print(check.count(False))
    