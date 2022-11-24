print(next(i for i, x in enumerate(
    [int(input()) for _ in range(int(input()))])
    if x % 2 == 0) + 1)
