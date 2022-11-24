print(sum(filter(
    lambda x: x % 2 == 0 and x < 30,
    [int(input()) for _ in range(int(input()))]
)))
