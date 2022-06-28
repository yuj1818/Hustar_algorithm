t = int(input())
for testcase in range(t):
    n,k,m = map(int, input().split())
    if n == 1:
        print(n)
        continue
    if k == 0:
        print("1")
    elif k % 2 == 0:
        print((pow(n,k//2,m)**2)%m)
    else:
        print(((pow(n,k//2,m)**2)*n)%m)