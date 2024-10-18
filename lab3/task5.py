#task5
'''
to get the shortes path of a graph i have used
bfs and modified it. and used two dictionry.
one for storing time and other for storing a vertex's predessesor in bfs tree.
then after the bfs traversal i have just made a list by back tracing 
with the predessasor dictionary.simpe-_-
'''
import queue

def BFS_shortest_path(G, s, destination):
    distances = {} # for storeing distances from source node
    predecessors = {} # for storeing predecessors for each node
    for i in G:
        distances[i] = -1  # Initialize all distances to -1
        predecessors[i] = None
    
    q = queue.Queue()
    distances[s] = 0  # Distance from source to itself is 0
    q.put(s)
    
    while not q.empty():
        u = q.get()
        if u == destination:  # If destination reached, stop BFS
            break
        for v in G[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                predecessors[v] = u
                q.put(v)
    #print(distances)
    #print(predecessors)
    # Backtrack to find the shortest path
    shortest_path = []
    current = destination
    {0: None, 1: None, 2: 3, 3: 1, 4: 1, 5: 6, 6: 4}
    while predecessors[current] is not None:
        shortest_path.append(current)
        current = predecessors[current]
    #print(shortest_path)    
    shortest_path.append(s)
    shortest_path.reverse()
    
    return shortest_path, distances[destination]

# Read input from file
boi = open("input5.txt", "r")
khata= open("output5.txt","w")
x, y, d = map(int, boi.readline().split())

book = {}
for i in range(x + 1):
    book[i] = []

for i in range(y):
    a, b = map(int, boi.readline().split())
    book[a].append(b)
    book[b].append(a)

# Find the shortest path from node 1 to node d
shortest_path, shortest_distance = BFS_shortest_path(book, 1, d)
print("Time:", shortest_distance)
#print(shortest_path)
x=""
for i in shortest_path:
    x+= str(i)+" "
print("Shortest Path:",x )
a="Time:"+str(shortest_distance)+"\n"
b="Shortest Path:"+str(x)
khata.write(a)
khata.write(b )

