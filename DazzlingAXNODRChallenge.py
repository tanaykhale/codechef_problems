from re import T


t = int(input())
for i in range(t):
    n = 0
    n = int(input())
    ans = 0
    if(n % 2 == 0):
        if(n % 4 == 0):
            ans = 3 ^ n

        else:
            ans = 3
    else:
        if (n-1) % 4 == 0:
            ans = 3 ^ (n-1) & n
        else:
            ans = 3
    print(ans)
