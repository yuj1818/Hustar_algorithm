answer = []
f = [0]
t = int(input())
for i in range(t):
    n = int(input())
    if n in [1,2]:
        f.insert(n,1)
    else:
        f.insert(n,f[n-1] + f[n-2])
    answer.append(f[n])
    
for j in answer:
    print(j)