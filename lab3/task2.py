#task 2
'''
for the bfs traverse i used the scudo code of the 
question then modified it.and printed the vertex 
at the time of enqueing.for the queue i use inbuild queue module.
and the graph is in adjcent list in terms of dictionary.
'''
import queue

def BFS(G, s):
    bfs_book={}
    for i in G:
        bfs_book[i]= 0

    q= queue.Queue()
    bfs_book[s] = 1
    q.put(s)
    while not q.empty():
        u = q.get()
        print(u, end=" ")
        khata.write(str(u)+" ")
        #print(type(u))
        for v in G[u]:
            if bfs_book[v]== 0:
                bfs_book[v]= 1
                q.put(v)





#for opening file
boi= open ("input2.txt","r")
khata= open("output2.txt","w")

x,y = list(map(int,boi.readline().split()))

book={}
for i in range(x+1):
    book[i]=[]

for i in range(y):
    a,b=list(map(int,boi.readline().split()))
    #print(a,b,c)
    book[a].append((b))
    book[b].append((a))
 
    
BFS(book,1)    

