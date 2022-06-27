answer = []
t = int(input())
for i in range(t):
    distance = []
    numlist = tuple(map(int, input().split()))
    for j in range(numlist[0],numlist[-1] + 1):
        total = 0
        for k in numlist:
            total += abs(k-j)
        distance.append(total)
    answer.append(min(distance))
    
for x in answer:
    print(x)