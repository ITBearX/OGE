print(sum(filter(
    lambda x: x <= 16 and x % 10 != 5,
    [int(input()) for _ in range(int(input()))]
)))
