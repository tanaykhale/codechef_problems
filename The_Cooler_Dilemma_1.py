t = int(input())
for i in range(t):
    x, y, m = [int(x) for x in input().split()]
    x = x*m
    if x < y:
        print('yes')
    else:
        print('no')
