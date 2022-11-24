print(max(filter(
    lambda x: x % 100 == 12,
    [int(input()) for _ in range(int(input()))]
)))
