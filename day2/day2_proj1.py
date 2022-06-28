from collections import deque

def mergesort(l1, l2):
    answer = []
    total = len(l1) + len(l2)
    for i in range(total):
        if len(l1) == 0:
            for j in l2:
                answer.append(2)
                break
        elif len(l2) == 0:
            for j in l1:
                answer.append(1)
                break
        elif l1[0] < l2[0]:
            answer.append(1)
            l1.popleft()
        else:
            answer.append(2)
            l2.popleft()
    return answer        

t = int(input())
for testcase in range(t):
    list_1 = deque(map(int, input().split()))
    list_2 = deque(map(int, input().split()))
    print(*mergesort(list_1, list_2))
