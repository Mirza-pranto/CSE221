# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zu9p3IrVfuclMGLf4xT5Zd8hZjXhOsYO

**Task 4**--
After reading input file with loop i have made two list one for train names and other for departure time. then i havee performed a selection sorting on train names list comparing just names but in the sort algo i have added one more option if the two names are same then it checks if the time is small or big.if it is small then it changes it position otherwise not. At last i have just printed as output.
"""

#task 4

#for opening file
boi = open("input4.txt","r")
khata = open("output_4.txt","w")

num=int(boi.readline())

train, dep = [] , []
#for file reading part
for i in range(num):
    s = boi.readline()
    #for appending train names
    box=s.split()
    train.append(box[0])
    #for appending depture time
    dep.append(box[-1])
#sorting part
for i in range(len(train)):
        for j in range(i + 1, len(train)):
            if train[i] > train[j]:
                train[i], train[j] = train[j], train[i]
                dep[i], dep[j] = dep[j], dep[i]
            elif  train[i] == train[j]:
                if dep[i]<dep[j]:
                    train[i], train[j] = train[j], train[i]
                    dep[i], dep[j] = dep[j], dep[i]



#printing part
for i in range(len(train)):
    x,y=str(dep[i]).split(":")
    s=str(x+":"+y)
    print(f"{train[i]} will departure for Dhaka at {s}")
    khata.write(f"{train[i]} will departure for Dhaka at {s}\n")

boi.close()
khata.close()