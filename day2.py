
#Typecasting--------------------------------------------

a="3532"
a = int(a)
print(type(a))
print(a + 5)
# you can convert "233554"  into int but you can not convert "32dcfas" into int .
# here "31" is string literal but 31 is numeric literal.



#inputfunction-----------------------------------------------------


a = input("enter a number:")
a = int(a) # convert a to an integer(if possible)
print(a)
print(type(a))

b = input("enter your name:")
print(b)
print(type(b))
# this function allow user to take input  from the keyboard as a string.


#practice question
# add two numbers
a = 34
b = 56
print("add two numbers a + b is", a+b)



# find a reminder when a number is divided by 2

a = 45
b = 15
print("the remainder when a is divided by b is ", a%b)


#cheak the type variable assigned using input function


a = input("enter your college name:")
print (a)
print(type(a))


# use camparision operator to find which value is greter than 

a = 34
b = 80
print("compare a>b:", a>b)
print("compare b>a:", b>a)


# find average of two number entered by users

a = int(input("enter first number:"))
b = int(input("enter second number:"))
avg = (a+b)/2
print("the avrage of a and b is: " , avg)


#sequre of a number entered by user

a = int(input("Enter any number:"))
print("squre of a is:" , a*a)



#strings-----------------------------------------------------

name = "hitanshi"

nameshort = len(name)
print(nameshort)
nameshort =name[0:3]
print(nameshort)
nameshort = name[1]
print(nameshort)


name = "jayshree"
#slicing
print(name[0:3])
#negative slicing
print(name[-4:-1])


print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])


#slicing with skip value
a = "hitanshiaasnani"
print(a[1:9:2])


#string function

name = "hitanshi aasnani"
print(len(name))
print(name.endswith("shii"))
print(name.startswith("hit"))
print(name.capitalize())
print(name.find("ta"))
print(name.replace("hitanshi","jayshree"))\



#escape sequence characters
name="hitanshi is good girls \n but not a bad \t girl"
print(name)



#practice question

name = input("Enter your name: ")

print(f"Good Afternoon, {name} ") 


letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Hitanshi").replace("<|Date|", "24 September 2050"))



name = "Hitanshi is a good  girl   "

print(name.find("  "))


name = "Hitanshi is a good  girl   "

print(name.replace("  "," "))