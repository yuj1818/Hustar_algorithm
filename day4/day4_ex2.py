from math import floor


def findmaxw(n,c):
    liquid = []
    vtotal = 0
    wtotal = 0
    stop_idx = 0
    for _ in range(n):
        w, v = map(int, input().split())
        liquid.append([w, v])
    
    liquid.sort(key = lambda x:x[0]/x[1], reverse=True)
    
    for x in range(len(liquid)):
        if (vtotal + liquid[x][1]) <= c:
            vtotal += liquid[x][1]
            wtotal += liquid[x][0]
            if (vtotal == c):
                return wtotal
        else:
            stop_idx = x
            break
    
    wtotal += (c - vtotal)*liquid[stop_idx][0]/liquid[stop_idx][1]
    return wtotal

t = int(input())

for testcase in range(t):
    n, c = map(int, input().split())
    print(floor(findmaxw(n,c)))