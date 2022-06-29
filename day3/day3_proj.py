import heapq

def dijkstra(chart):
    heap = []
    distance = {loc: float('inf') for loc in chart}
    distance[0] = 0
    heapq.heappush(heap, [distance[0], 0])
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if cost > distance[node]:
            continue
        for nnode, ncost in chart[node].items():
            ndistance = cost + ncost
            if ndistance < distance[nnode]:
                distance[nnode] = ndistance
                heapq.heappush(heap, [ndistance, nnode])
                
    return distance

t = int(input())

for testcase in range(t):
    n,m = map(int, input().split())
    chart = {}
    for i in range(n):
        chart[i] = {}
    for j in range(m):
        u,v,c = map(int, input().split())
        chart[u][v] = c
        
    answer = dijkstra(chart)[n-1]
    
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)
    
        
