start = ['(', '{', '[']
stop = [')', '}', ']']
t = int(input())
for i in range(t):
    bracket = input()
    stack = []
    for j in bracket:
        if j in start:
            stack.append(j)
        else:
            if stack and stack[-1] in start and start.index(stack[-1]) == stop.index(j):
                stack.pop()
            else:
                stack.append(j)
                
    if stack:
        print("NO")
    else:
        print("YES")
    
    