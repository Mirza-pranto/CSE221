#task 1
'''
here in graph class i have made graph actually. in dijkstra i heve used two dictiony and a set.
then initially all vertexs distance is 0 then i have made the starting one zero. after that picking 
up the minimum index from the graph and not in visited i have compared the parents distance + path with current distance.
and if then sum is less then updated the current distance . thats how i got dijkstra algo

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



boi= open ("input1.txt","r")
khata= open("output1.txt","w")
x, y = map(int, boi.readline().split())
customGraph = Graph()
for i in range(y):
    a, b, c = map(int, boi.readline().split())
    customGraph.addNode(a)
    customGraph.addEdge(a, b, c) 

k = int(boi.readline().strip())


visited, path = dijkstra(customGraph, k)

for i in range(1,x+1):
    if i in visited:
        
        print(visited[i], end= " ")
        khata.write(str(visited[i])+" ")
        
    else:
        print("-1",end= " ")
        khata.write("-1" +" ")
        
boi.close()
khata.close()        