import collections

answer = []
t = int(input())
for i in range(t):
    queue = collections.deque([])
    n = int(input())
    for j in range(n):
        query = int(input())
        if query != -1:
            queue.append(query)
        else:
            answer.append(queue.popleft())
            
for k in answer:
    print(k)