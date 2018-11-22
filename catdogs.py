for t in range(int(input())):
    c, d, l = map(int, input().split())
    if l % 4 == 0 and l >= (d + max(c - 2 * d, 0)) * 4 and l <= (c+d)*4:
        print('yes')
    else:
        print('no')

        
