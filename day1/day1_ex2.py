answer = []
ran = int(input())
for i in range(ran):
    a,b = map(int, input().split(' '))
    answer.append(a+b)
    
for j in answer:
    print(j)