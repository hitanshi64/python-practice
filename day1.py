
#---------------------------------------------------------------
# comments
#---------------------------------------------------------------
#author : hitanshi
#licenced to : abc company
'''author : hitanshi
licenced to : abc company'''
#---------------------------------------------------------------
#import os
#---------------------------------------------------------------
import os # importing os module
print("Current Working Directory:", os.getcwd())


#---------------------------------------------------------------
#print statement
#---------------------------------------------------------------
print("hello world")


#---------------------------------------------------------------
#variable and datatypes
#---------------------------------------------------------------
#storing value in variable

a = "hitanshi"
a1 = 'hitanshi'
a2 = '''hitanshi'''
b = 343
c = 45.32
d = True 
e = None
# printing variables
print(a)
print(a1)
print(a2)
print(b)
print(c)
print(d)
print(e)

#printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#---------------------------------------------------------------
#operators
#---------------------------------------------------------------
a = 3
b = 4


#arithmetic operator
print(" The  value 3+4 is" ,3+4)
print(" The  value 3-4 is" ,3-4)
print(" The  value 3*4 is" ,3*4)
print(" The  value 3/4 is" ,3/4)

#assignment operator
a = 38
a += 2
print(a)

b = 86
b -= 12
print(b)

c = 4
c *=3
print(c)

d = 10
d /= 2
print(d)


#comparison operator


e = (14>=7)
f = (14<=7)
g = (14>7)
h = (14>7)
i = (14==7)
j = (14!=7)
print(e)
print(f)
print(i)
print(h)
print(g)
print(j)


#logical operator
bool1=True
bool2=False
print("The value of boo1 and boo2 is", (bool1 and bool2))
print("The value of boo1 or boo2 is", (bool1 or bool2))
print("The value of not boo2 is", (not bool2))