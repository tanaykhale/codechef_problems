import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if (a == 1) or (b == 1):
        print('-1')
    else:
        if(math.gcd(a, b) == 1):
            print('1')
        else:
            print('0')
