# -*- coding: utf-8 -*-
"""Task1(b).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zu9p3IrVfuclMGLf4xT5Zd8hZjXhOsYO

**task 1(b)**--
at first i have opened two file one for read and another for write. then  variable "a" reads the number of test cases.then to read multiple line i used loop  and in each iteration it read a line then break it and make a list with split function. then it checks the operation with condition and write the outputs after doing arrithmatic part.
"""

#task 1 b

#for opening file
boi= open("input1b.txt","r")
khata= open("output_1b.txt","w")

a=int(boi.readline())
for i in range(a):
    stack=boi.readline()
    x,y,z,m=stack.split()
    if z=="+":
        khata.write(f"The result of {y} {z} {m} is {int(y)+int(m)}\n")
    elif z=="-":
        khata.write(f"The result of {y} {z} {m} is {int(y)-int(m)}\n")
    elif z=="*":
        khata.write(f"The result of {y} {z} {m} is {int(y)*int(m)}\n")
    elif z=="/":
        khata.write(f"The result of {y} {z} {m} is {int(y)/int(m)}\n")
boi.close()
khata.close()