
#read no of test cases in tests
tests = int(input())
for test in range(tests):
        #eread size of array
        arraySize = int(input())
        #read value of array
        li = list(map(int,input().split()))
        #print the minimum no of cost required for array
        print (min(li)*(arraySize-1))

