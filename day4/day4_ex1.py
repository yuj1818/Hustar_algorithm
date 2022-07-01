t = int(input())

for testcase in range(t):
    tax = int(input())
    coin = 0
    unit = [50000, 10000, 5000, 1000, 500, 100]
    for x in unit:
        coin += tax//x
        tax = tax%x
    print(coin)