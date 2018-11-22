tests = int(input())
for test in range(tests):
	arraySize = int(input())
	li = list(map(int,input().split()))
    	print (min(li)*(arraySize-1))

