print(sum(filter(
    lambda x: 10 < x < 50,
    [int(input()) for _ in range(int(input()))]
)))
