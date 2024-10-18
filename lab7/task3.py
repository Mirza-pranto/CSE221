'''
Here we simply run a fibonaccici series but with memoriser.
if it finds a value it stores it in a array and when the same 
recursive function call it bring back the memories.
'''
def frog_climber(n,arr):
    if n == 1 or n==2 :
        return arr[n]
    else:
        if arr[n-1]== None and arr[n-2]== None:
            arr[n] = frog_climber(n-1,arr)+frog_climber(n-2,arr)
            return arr[n]
        elif arr[n-1]== None :
            arr[n] = frog_climber(n-1,arr) + arr[n-2]
            return arr[n]
        elif arr[n-2]== None:
            arr[n] = frog_climber(n-2,arr) + arr[n-1]
            return arr[n] 
        else :
            arr[n] = arr[n-1] + arr[n-2]
            return arr[n]
        
inp = open("input3.txt","r")
out = open("output3.txt","w")
x =  int(inp.readline())
arr1 = [None]*(x+1)
arr1[1] = 1
arr1[2] = 2
call = frog_climber(x,arr1)
out.write(f"{call}")