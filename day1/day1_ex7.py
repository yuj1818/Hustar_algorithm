import heapq

answer = []
t = int(input())
for i in range(t):
    hq = []
    n = int(input())
    for j in range(n):
        query = int(input())
        if query != -1:
            heapq.heappush(hq, query)
        else:
            answer.append(heapq.heappop(hq))
            
for k in answer:
    print(k)
