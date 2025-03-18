
#Program for while loop
count=0
while(count < 3):
    count=count+1
    print("Hello World")


#Program for iterating over a List
print("List Iteration")
I=["geeks","for","geeks"]
for i in I:
    print(i)

#Program for iterating over a tuple
print("Tuple Iteration")
t=("geeks","for","geeks")
for i in t:
    print(i)

#Program for iterating over a string
print("String Iteration")
s="string"
for i in s:
    print(i)

#Program for iterating by index
list=["geeks","for","geeks"]
for index in range(len(list)):
  print(index)

#Program for print all letters except 'e' and 's'
for letter in "geekforgeeks":
    if letter =='e'or letter=='s':
       continue
    print("Current Letter: ",letter)

#Program for using a break statement
for letter in "geekforgeeks":
    if letter=="e"or letter=="s":
       break
print ("Current Letter: ",letter)

#Program for defining a function
def my_function():
    print("Hello from a function")

my_function()

#Program for giving different parameters to function
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Toblas")
my_function("Linus")

#Program for giving a default parameter to function
def my_function(country="Norway"):
    print("I am from "  + country)

my_function("Swedon")
my_function("Pakistan")
my_function()
my_function("Brazil")

#Program for giving a list as parameter to function
def my_function(Food):
  for x in Food:
      print(x)

fruits=["Apple","Banana","Cherry"]
my_function(fruits)

#Program for using a return statement
def my_function(x):
    return 5*x

print (my_function(3))
print (my_function(5))
print (my_function(9))

#Program for using a keyword Arguments
def my_function (child3,child2,child1): 
    print("The youngest child is "+ child3)

my_function(child1="Emil",child2="Tobias",child3="Linus")

#Program for class
class my_class:
    x=5

p1=my_class()
print(p1.x)

#Program for using a _init_() function
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("John",36)
print(p1.name)
print(p1.age) 

#Program for using a object method
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_func(self):
        print("My name is "+ self.name)

p1=Person("John",36)
p1.my_func()
