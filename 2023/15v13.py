print(min(filter(
    lambda x: x % 16 == 0,
    [int(input()) for _ in range(int(input()))]
)))
