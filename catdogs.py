
#Read no of test cases in t 
for t in range(int(input())):
    #read values for no of cats,no of dogs,no of legs 
    c, d, l = map(int, input().split())
    #check  the condition for each test case
    if l % 4 == 0 and l >= (d + max(c - 2 * d, 0)) * 4 and l <= (c+d)*4:
        print('yes')
    else:
        print('no')

        
