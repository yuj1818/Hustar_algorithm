
t = int(input())

for testcase in range(t):
    n = int(input())
    score = list(map(int, input().split()))
    score.insert(0,0)
    DP = [None]*(n+1)
    
    for i in range(n+1):
        if i == 0:
            DP[i] = 0
        elif i == 1:
            DP[i] = DP[i-1] + score[i]
        elif i == 2:
            DP[i] = max(DP[i-1]+score[i], DP[i-2]+score[i])
        else:
            if i%3 == 0:
                d = i//3
                DP[i] = max(DP[i-1]+score[i], DP[i-2]+score[i], DP[d]+score[i])
            else:
                DP[i] = max(DP[i-1]+score[i], DP[i-2]+score[i])
            
    print(DP[n])