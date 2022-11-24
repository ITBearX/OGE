print(sum(filter(
    lambda x: x < 10 or x > 50,
    [int(input()) for _ in range(int(input()))]
)))
