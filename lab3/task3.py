#task 3
'''
for the DFS traversal i have used the scudo code of the
question. then modified it and used it. and printed the 
vertex when we first time visited the dfs tree.
and graph and file format is same as before bfs code

'''
def DFS(G, s):
    dfs_book = {}
    for i in G:
        dfs_book[i] = 0
    DFS_loop(G, s, dfs_book)

def DFS_loop(G, s, book):
    print(s, end=" ")
    # Print the vertex when it is visited
    khata.write(str(s)+" ")
    book[s] = 1
    for i in G[s]:
        if book[i] == 0:
            DFS_loop(G, i, book)

#for opening file
boi= open ("input3.txt","r")
khata= open("output3.txt","w")

x,y = list(map(int,boi.readline().split()))

book={}
for i in range(x+1):
    book[i]=[]

for i in range(y):
    a,b=list(map(int,boi.readline().split()))
    #print(a,b,c)
    book[a].append((b))
    book[b].append((a))
   
DFS(book,1)    
