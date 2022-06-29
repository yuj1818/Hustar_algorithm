from collections import deque

t = int(input())

for testcase in range(t):
    n, m = map(int, input().split())
    queue = deque([0])
    check = []
    List = [[] for _ in range(n)]
    for con in range(m):
        u, v = map(int, input().split())
        List[u].append(v)
    
    for i in List:
        i.sort()
        
    while queue:
        a = queue.popleft()
        if a not in check:
            check.append(a)
            queue.extend(List[a])
    
    print(*check)
    