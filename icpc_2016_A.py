while (True):
    N = int(input())
    if (N == 0): exit()
    points = sorted(list(map(int, input().split())))
    print(points)
    diff = []
    for i in range(N - 1):
        diff.append(abs(points[i] - points[i + 1]))
    print(min(diff))
