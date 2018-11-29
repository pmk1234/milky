
#program
#read no. of test cases in t
for t in range(int(input())):
    #read no minutes in n
    n=int(input())
    #flag is variable initialized to zero
    flag=0
    #enter the cookies and milk for input minutes  
    l = input().split()
    #for each minute check the sequence for cookies and milk
    for i in range(n):
        if (l[i]=="cookie") and (l[i+1]=="cookie"):
            flag=1
            break
    if(l[-1]=="cookie"):
        flag=1
    if flag==0:
        print("YES\n")
    else:
        print("NO\n")
