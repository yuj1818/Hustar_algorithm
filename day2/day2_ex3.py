def maxsum(start, end):
    if start >= end:
        return numlist[end]
    
    mid = (start+end)//2
    
    flist = maxsum(start, mid)
    blist = maxsum(mid+1, end)
    
    lsum = 0
    lmax = 0
    for num in range(mid, start-1, -1):
        lsum += numlist[num]
        if lsum>lmax:
            lmax = lsum
    
    rsum = 0
    rmax = -100000
    for num in range(mid+1, end+1):
        rsum += numlist[num]
        if rsum>rmax:
            rmax = rsum

    return max(flist, blist, lmax+rmax)

t = int(input())

for testcase in range(t):
    numlist = list(map(int, input().split()))
    print(maxsum(0, len(numlist)-1))