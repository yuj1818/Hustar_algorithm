stack = []
answer = []
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        query = int(input())
        if query != -1:
            stack.append(query)
        else:
            answer.append(stack.pop())
            
for k in answer:
    print(k)