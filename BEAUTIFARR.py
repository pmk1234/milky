for m in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    positives = negative_ones = zeroes = others = ones = 0
    for i in li:
        if i == -1:
            negative_ones += 1
        elif i == 0:
            zeroes += 1
        elif i == 1:
            ones += 1
        else:
            others += 1
    if others > 1 or (negative_ones > 1 and ones == 0) or (negative_ones and others):
        print('no')
    else:
        print('yes')
        

