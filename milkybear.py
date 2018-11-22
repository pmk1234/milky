
#program  
for t in range(int(input())):         #no. of inputs
    n=int(input())                    #no. of minutes
    flag=0
    l = input().split()
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
