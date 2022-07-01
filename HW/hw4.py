
t = int(input())

for testcase in range(t):
    n = int(input())
    a = [None]*(n+1)
    
    for i in range(n+1):
        if i == 0:
            a[i] = 1
        elif i == 1:
            a[i] = 1
        elif i%2 == 0:
            a[i] = (2*a[i-1] + a[i-2])%20211209
        else:
            a[i] = (a[i-1] + 2*a[i-2])%20211209
    print(a[n])