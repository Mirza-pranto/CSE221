# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zAjGqHpzjF68tzW11yDJNQCv1E779Ihc
"""

#task 4
'''
here i have the same tecniq as before just addeded somthing new.
 here two make it more accurate and to maximize i have done the same code twice
  one i have picked job from the first. and the oter time i have picked it
   form the last. then compared in which time the count was much more bigger.
    and i have chosen the bigger one.

'''
#for opening file
boi= open ("input4.txt","r")
khata= open("output_4.txt","w")

start = []
last = []


a, b= list(map(int,boi.readline().split(" ")))
print(a)
for i in range(a):
    x, y = list(map(int,boi.readline().split()))
    start.append(x)
    last.append(y)

n= len(last)
for i in range(n):
                # Last i elements are already in place, so we don't need to compare them again
                for j in range(0, n-i-1):
                    # Traverse the array from 0 to n-i-1, swap if the element found is greater than the next element
                    if last[j] > last[j+1]:
                        last[j], last[j+1] = last[j+1], last[j]
                        start[j], start[j+1] = start[j+1], start[j]
start2= start.copy()
last2= last.copy()
for i in range(a):
            print(start[i], last[i])
print("--------")

#takinh the job from the first
count1=0
for i in range(b):
    if len(start)>0:



        f=0
        l=0

        for j in range(len(start)):
            if start[j]>=l:
                count1+=1
                l=last[j]

                start[j]=-1
                last[j]=-1
#taking job from the last


count2=0
for i in range(b):
    if len(start2)>0:



        f=0
        l=99999

        for j in range(len(start2)-1,-1,-1):
            #print(j)
            if last2[j]<=l and start2[j]>0:
                count2+=1
                l=start2[j]
                #print(start2[j], last2[j])
                start2[j]=-1
                last2[j]=-1
        #print(start2, last2)
       # print("-----")


       # khata.write(f"{count} \n")
#print(count1,count2)
if count1>count2:
    khata.write(f"{count1} \n")
    print(count1)
else:
    khata.write(f"{count2} \n")
    print(count2)