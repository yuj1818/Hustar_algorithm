import bisect

def search(numlist, num):
    tmp = bisect.bisect_left(numlist, num)
    if tmp == 0:
        return numlist[0]
    elif tmp == len(numlist):
        return numlist[tmp-1]
    else:
        if numlist[tmp] == num:
            return numlist[tmp]
        elif num - numlist[tmp-1] <= numlist[tmp] - num:
            return numlist[tmp-1]
        elif num - numlist[tmp-1] > numlist[tmp] - num:
            return numlist[tmp]
    
t = int(input())

for testcase in range(t):
    answer = []
    numlist = list(map(int, input().split()))
    findlist = list(map(int, input().split()))
    for num in findlist:
        answer.append(search(numlist,num))
        
    print(*answer)