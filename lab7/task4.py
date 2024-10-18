'''
In this task we again checked for each coin how the minimum 
number of coin is required then printed the largeset value.
'''
def min_coin(c,arr1):
    for i in range(1,len(arr1)):
        if i>=c:
            k= b = i
            j = 1
            while k>0:
        
                s = b - j*c
                if s >= 0:
                   a = j + arr[(i-j*c)]
                   arr1[i] = min(a,arr1[i])

                k = k- j*c
                j +=1
inp = open("input4.txt","r")
out = open("output4.txt","w")
x,y = inp.readline().split(" ")
arr = [ float('inf')]* (int(y)+1)
arr[0]= 0
lis = inp.readline().split(" ")
lis2 = []
for i in lis:
    min_coin(int(i),arr)

out.write(f"{arr[int(y)]}")
