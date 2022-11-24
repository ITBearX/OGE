print(min(filter(
    lambda x: x % 112 < 9,
    [int(input()) for _ in range(int(input()))]
)))
