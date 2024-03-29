from collections import deque

t = int(input())

for testcase in range(t):
    n, m, k = map(int, input().split())
    queue = deque([k])
    check = []
    List = [[] for _ in range(n)]
    for con in range(m):
        u, v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
    
    for i in List:
        i.sort()
        
    while queue:
        a = queue.popleft()
        if a not in check:
            check.append(a)
            queue.extend(List[a])
    
    print(*check)
    