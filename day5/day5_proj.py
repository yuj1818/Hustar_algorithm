def maxsum(List):
    DP = [None]*len(List)
    DP[0] = List[0]
    for i in range(1, len(List)):
        DP[i] = (max(DP[i-1]+List[i], List[i]))
    return max(DP)

t = int(input())

for testcase in range(t):
    List = list(map(int, input().split()))
    print(maxsum(List))