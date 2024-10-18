#task1b
'''
here i used a dictionaty to represent the graph
as adjecent list.in dictionary each key represent vertex
and its value is the adj list.
'''
import numpy as np
#for opening file
boi= open ("input1b.txt","r")
khata= open("output1b.txt","w")

x,y = list(map(int,boi.readline().split()))

book={}
for i in range(x+1):
    book[i]=[]

for i in range(y):
    a,b,c =list(map(int,boi.readline().split()))
    #print(a,b,c)
    book[a].append((b,c))

for i in book.keys():
   #m=" ".join( book[i])

    m=""
    for j in book[i]:
        m+= str(j)
    print(f"{i} : {m}" )
    khata.write(f"{i} : {m}\n")

