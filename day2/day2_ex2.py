t = int(input())
for testcase in range(t):
    idx_list = []
    numlist = list(map(int, input().split()))
    findlist = list(map(int, input().split()))
    for fnum in findlist:
        start = 0
        end = len(numlist)-1
        while start <= end:
            mid_idx = (start+end)//2
            if fnum == numlist[mid_idx]:
                break
            elif fnum > numlist[mid_idx]:
                start = mid_idx+1
            elif fnum < numlist[mid_idx]:
                end = mid_idx-1
        if start > end:
            idx_list.append(-1)
        else:
            idx_list.append(mid_idx)
    print(*idx_list)