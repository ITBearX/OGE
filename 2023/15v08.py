print(max(filter(
    lambda x: x % 112 == 4,
    [int(input()) for _ in range(int(input()))]
)))
