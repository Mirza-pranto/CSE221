#task 3
'''
here i have used the dijkstra algo to solve the problem. but to get the minimum denger value
in its path. i have modified it. in the main dijkstra  used to compare the parents distance + path with current distance.
but here i have compared parents denger level with nodes denger level.
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
            #weight = currentWeight + graph.distances[(minNode, edge)]
            weight = max(currentWeight, graph.distances[(minNode, edge)])
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = path[minNode] + [edge]
                
    return visited, path 




#with open("input1.txt", "r") as boi, open("output1.txt", "w") as khata:
boi= open ("input3.txt","r")
khata= open("output3.txt","w")
x, y = map(int, boi.readline().split())
customGraph = Graph()
for i in range(y):
    a, b, c = map(int, boi.readline().split())
    customGraph.addNode(a)
    customGraph.addEdge(a, b, c) 



#print(customGraph.edges, file=khata)
visited, path= dijkstra(customGraph, 1)

print(visited[x])
khata.write(str(visited[x]))

boi.close()
khata.close()   