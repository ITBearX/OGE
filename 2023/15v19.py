print(min(filter(
    lambda x: 1344 % x == 0,
    [int(input()) for _ in range(int(input()))]
)))
