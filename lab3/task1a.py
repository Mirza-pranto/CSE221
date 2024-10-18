#task 1a
'''
For this task i have used numpy array to 
represent the graph.where i used 1 based indexing
for the 2d array. and in code i have read a line 
then puted edge's weight in the right posintion of the 
matrix with row and column number.
'''
import numpy as np
#for opening file
boi= open ("input1a.txt","r")
khata= open("output1a.txt","w")



x,y = list(map(int,boi.readline().split()))
panel=[[0]*(y)]*(y)
panel=np.array(panel)
for i in range(y):
    a,b,c =list(map(int,boi.readline().split()))
    #print(a,b,c)
    panel[a][b]=c
    #print(panel)

for i in panel:
    print(" ".join(map(str, i)))
    x=" ".join(map(str, i))+"\n"
    khata.write(x)
    


#khata.write(" ".join(map(str, x)))

#print(panel)
boi.close()
khata.close()