
t = int(input())

for testcase in range(t):
    T = [1, 2, 4]
    n = int(input())
    
    if n>3:
        for i in range(3, n):
            T.append((T[i-1] + T[i-2] + T[i-3])%1904101441)
    
    print(T[n-1])