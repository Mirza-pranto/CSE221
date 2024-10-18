#task6
'''
two solvel this problem i have used flood fill algorithm
at first made a numpy array or 2d array with file.then
used two function one for conting all the diamond from a point.and another for 
two get maximum diamond i called the previous function for all the diamond point
and got the maximum number point. :') 
'''
import numpy as np
def FloodFill(r, c, rows, cols, G):
    if r < 0 or r >= rows or c < 0 or c >= cols or G[r][c] == '#' or G[r][c]=="/":
        return 0

    count = 0
    if G[r][c] == 'D':
        count += 1

    G[r][c] = '/'

    count += FloodFill(r + 1, c, rows, cols, G)
    count += FloodFill(r - 1, c, rows, cols, G)
    count += FloodFill(r, c + 1, rows, cols, G)
    count += FloodFill(r, c - 1, rows, cols, G)

    return count

def countdiamonds(rows, cols, G):
    maxDiamonds = 0
    for r in range(rows):
        for c in range(cols):
            x=G.copy()
            if G[r][c] == 'D':
                diamond = FloodFill(r, c, rows, cols, x)
                maxDiamonds = max(maxDiamonds, diamond)

    return maxDiamonds


boi = open("input6.txt", "r")
khata = open("output6.txt", "w")

row, col = map(int, boi.readline().split())
box = []

for i in range(row):
    a=boi.readline()
    x=[]
    for j in a:
        x.append(j) 
    #print(len(x))
    box.append(x[:-1]) 
    '''
    if i ==row-1:    
     box.append(x)
    else:
        box.append(x[:-1])
'''   
           
G=np.array(box)    
result = countdiamonds(row, col, G)
print(result)

khata.write(str(result))
boi.close()
