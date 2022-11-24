print(len(list(filter(
    lambda x: 4040 % x == 0 and x != 1,
    [int(input()) for _ in range(int(input()))]
))))
