

t = int(input())
for i in range(t):
    x, y = [int(x) for x in input().split()]
    if x >= y:
        print('Yes')
    else:
        print('no')
