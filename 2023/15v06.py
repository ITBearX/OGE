print(len(list(filter(
    lambda x: x % 221 < 7,
    [int(input()) for _ in range(int(input()))]
))))
