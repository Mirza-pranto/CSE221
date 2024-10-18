'''
In this task first made a array where each index holding a tupple
list containing thier own number and 1 as a count. Then for every
bond we found we run rank_finder . if the  rank are not same then 
we created a bond and updated the count in rank.
'''
def rank_finder(ind , lis ):
    if ind == lis[ind][0]:
        return ind
    else:
        return rank_finder(lis[ind][0] , lis)
inp = open("input1.txt","r")
out = open("output1.txt","w")
x,y = inp.readline().split(" ")
rank = [None]* int(x)
for i in range(int(x)):
    rank[i] = [i,1]
for j in range(int(y)):
    k,q = inp.readline().split(" ")
    k = int(k)
    q = int(q)
    u = rank_finder(k,rank)
    v = rank_finder(q,rank)
    if u != v:
        rank[u] = [u , rank[u][1] + rank[v][1]]
        rank[q] =  [ u ,  rank[q][1]]
    out.write(f"{rank[u][1]}\n")