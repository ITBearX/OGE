print(sum(filter(
    lambda x: x % 10 != 3 and x <= 25,
    [int(input()) for _ in range(int(input()))]
)))
