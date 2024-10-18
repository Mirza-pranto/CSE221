#task 4 all working
'''
for detecting cycle in derected graph i need to aproch a 
diffrent way but it is a modified code of dfs.cause it is different form finding cycle in 
undirected graph. thus i have used two function one for returning boolen
if there is a cycle form a vertex. and another for calling the previous 
function for all vertex.

'''
def isCyclic(G):
    visited = {}
    path = {}

    for i in G:
        visited[i] = False
        path[i] = False

    
    for i in G:
        if not visited[i]:
            if DFS_detect_cycle(G, i, visited, path):
                return "YES"
    
    return "NO"

def DFS_detect_cycle(G, s, visited, path):
    visited[s] = True
    path[s] = True
    
    for v in G[s]:
        if not visited[v]:
            if DFS_detect_cycle(G, v, visited, path):
                return True

        elif path[v]:
            return True
    
    # Remove the current vertex from the path since we are backtracking
    path[s] = False
    return False

#for opening file
boi= open ("input4.txt","r")
khata= open("output4.txt","w")

x,y = list(map(int,boi.readline().split()))

book={}
for i in range(x+1):
    book[i]=[]

for i in range(y):
    a,b=list(map(int,boi.readline().split()))
    book[a].append((b))
x=isCyclic(book)
print(x) 
khata.write(str(x))   