answer = []
ran = int(input())
for i in range(ran):
    num_list = map(int, input().split(' '))
    answer.append(sum(num_list))
    
for j in answer:
    print(j)
