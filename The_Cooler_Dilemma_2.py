t = int(input())

for i in range(t):
    count = 0
    x, y = [int(x) for x in input().split()]

    for j in range(1, y):
        if j*x >= y:
            break
        else:
            count += 1

    print(count)
