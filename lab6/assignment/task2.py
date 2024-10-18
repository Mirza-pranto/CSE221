#task 2
'''
to solve the problem i have used dijkhsta two times for both the index and got 4 dictionary.
two visited dict containing the minimum time to reach other. then i have just compared each nodes two 
times and picked maximum one then got which one have the smallest one.
'''

from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        
        self.distances = {}
        
    def addNode(self, value):
        self.nodes.add(value)
        
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance
        
        
def maximum(a, b):
    if a< b :
        return b
    else:
        return a

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)
    
    nodes = set(graph.nodes)
    
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
                    
        if minNode is None:
            break 
        
        nodes.remove(minNode)
        currentWeight = visited[minNode]
        
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = path[minNode] + [edge]
                
    return visited, path 


# File I/O

#with open("input1.txt", "r") as boi, open("output1.txt", "w") as khata:
boi= open ("input2.txt","r")
khata= open("output2.txt","w")
x, y = map(int, boi.readline().split())
customGraph = Graph()
for i in range(y):
    a, b, c = map(int, boi.readline().split())
    customGraph.addNode(a)
    customGraph.addEdge(a, b, c) 

m, n = map(int, boi.readline().split())

#print(customGraph.edges, file=khata)
visited1, path1 = dijkstra(customGraph, m)
visited2, path2 = dijkstra(customGraph, n)
print(visited1)
print(visited2)
print(visited1[1])
mini = 9999
idx= "Impossible"
for  i in range(1,x+1):
    #print(visited1[i],visited2[i])
    if i in visited1 and i in visited2 and visited1[i] !=0 and visited2[i]!=0:
     
        temp = maximum(visited1[i], visited2[i])
        if temp < mini:
            mini = temp
            idx = i
if idx == "Impossible" :
    print("Impossible")
    khata.write("Impossible")

else:           
    print("Time ",mini)
    print( "Node" ,idx) 
    khata.write("Time "+str(mini)+"\n")
    khata.write("Node" +str(idx))       
boi.close()
khata.close() 



