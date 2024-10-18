'''we ran the same process as thak 1 but in this task we connected
the small counted bond with the large counted bond. and also updated
the distanve it made then printed it.
'''

import heapq as h
def rank_finder(ind,lis ):
    if ind == lis[ind][0]:
        return ind
    else:
        return rank_finder(lis[ind][0] , lis)
inp = open("input2.txt","r")
out = open("output2.txt","w")
x,y = inp.readline().split(" ")
lis1 = []
lis2 = []
distance = 0
rank = [None]* (int(x)+1)

for i in range(int(x)+1):
    rank[i] = [i,1]

for j in range(int(y)):
    k,q,z = inp.readline().split(" ")
    k = int(k)
    q = int(q)
    z = int(z)
    h.heappush(lis1,[z,k,q])

while len(lis1)!= 0:
    p = h.heappop(lis1)
    a , b , c = p

    u = rank_finder(b,rank)
    v = rank_finder(c,rank)


    if u != v:
        if rank[u][1]>= rank[v][1]:
            rank[u] = [u , rank[u][1] + rank[v][1]]
            rank[c] =  [ u ,  rank[c][1]]
            
        else:
            rank[v] = [v , rank[v][1] + rank[u][1]]
            rank[b] =  [ v ,  rank[b][1]]
        distance += p[0]
        lis2.append(p)

out.write(f"{distance}\n")