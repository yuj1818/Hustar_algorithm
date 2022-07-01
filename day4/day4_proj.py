def minoil(g, l):
    st = []
    gasstation = list(map(int, input().split()))
    gasstation.append(l)
    cnt = 1
    loc = 0
    stop = [0]
    for x in range(1, len(gasstation)):
        if (gasstation[x] - gasstation[x-1]) > g:
            return -1
    
        if gasstation[x] - stop[-1] > g:
            cnt += 1
            stop.append(gasstation[x-1])
            if gasstation[x] != l and gasstation[x] - stop[-1] == g:
                cnt += 1
                stop.append(gasstation[x])
    return len(stop)-1

t = int(input())

for testcase in range(t):
    g, l = map(int, input().split())
    print(minoil(g, l))