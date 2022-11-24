print(max(filter(
    lambda x: 2200 % x == 0,
    [int(input()) for _ in range(int(input()))]
)))

