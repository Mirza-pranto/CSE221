# -*- coding: utf-8 -*-
"""task1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zAjGqHpzjF68tzW11yDJNQCv1E779Ihc
"""

#task 1 a
'''
in this problem as it is O(N**2) problem i have simply used
nested loops to check two values sum is equal to the given number or not.with
the first loop I have taken a number then with another nested loop
I peeked others number to check the sum
'''
#for opening file
boi= open ("input1a.txt","r")
khata= open("output1a.txt","w")

x,y=boi.readline().split()
box = boi.readline().split()
x,y=int(x),int(y)
#print(box)
def sum_check(box,y):
    for i in range(len(box)-1):
        for j in range(i+1, len(box)):
            if int(box[i])+int(box[j])==y:



                print(i+1, j+1)
                khata.write(f"{i+1} {j+1}")
                return f"{i+1} {j+1}"
    khata.write(f"IMPOSSIBLE")
    print("IMPOSSIBLE")





sum_check(box,y)

boi.close()
khata.close()