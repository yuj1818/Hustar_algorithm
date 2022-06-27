answer = []
ran = int(input())
for i in range(ran):
    num_list = tuple(map(int, input().split()))
    answer.append(max(num_list) - min(num_list))
    
for j in answer:
    print(j)