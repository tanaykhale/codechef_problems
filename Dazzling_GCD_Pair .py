
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if (x % 2 == 0):
        if (y-x > 1):
            print(x, " ", x+2)
        else:
            print('-1')
    else:
        if(y-x >= 3):
            if(x % 3 == 0):
                print(x, " ", x+3)
            else:
                print(x+1, " ", x+3)
        else:
            print('-1')
