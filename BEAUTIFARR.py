
#read no of testcase in m
for m in range(int(input())):
    #read no of elements of array
    n = int(input())
    #read actual value of array
    li = list(map(int, input().split()))
    #initialize variables to zero
    positives = negative_ones = zeroes =  others = ones = 0
   # Read each line in a loop to check  value of arguments is(1,-1,0)or others
    for i in li:
        if i == -1:
            negative_ones += 1
        elif i == 0:
            zeroes += 1
        elif i == 1:
            ones += 1
        else:
            others += 1
            #check the condition 
    if others > 1 or (negative_ones > 1 and ones == 0) or (negative_ones and others):
        print('no')
    else:
        print('yes')
        

