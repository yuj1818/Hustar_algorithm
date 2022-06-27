import collections
t = int(input())
for i in range(t):
    queue = collections.deque([]) 
    numlist = map(int, input().split())
    for j in numlist:
        if j not in queue:
            queue.append(j)
        else:
            if queue.popleft() != j:
                break

    if queue:
        print("YES")
    else:
        print("NO")