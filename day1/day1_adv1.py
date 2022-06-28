t = int(input())
for i in range(t):
    distance = []
    numlist = tuple(map(int, input().split()))
    mid = int((numlist[0]+numlist[-1]/2))
    print(min(distance))
    