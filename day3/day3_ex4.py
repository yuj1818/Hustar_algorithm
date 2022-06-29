t = int(input())

for testcase in range(t):
    n,m = map(int, input().split())
    List  = [[] for _ in range(n)]
    stack = [0]
    check = []
    for i in range(m):
        u,v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
        
    for j in List:
        j.sort(reverse=True)
    
    while stack:
        a = stack.pop()
        if a not in check:
            check.append(a)
            stack.extend(List[a])
    
    print(*check)