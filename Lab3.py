#   Program no 1:

for i in range(1500,2700):
  if i%7==0 and i%5==0:
   print(i)

#   Program no 2:

c=int(input("Enter a temperature in Celsius:"))
f=(c*9/5)+32
print(c, " in Fahrenheit is ",f )
f=float(input("Enter a temperature in Fahrenheit:"))
c=(f-32)*5/9
print(f, "in Celcius is ", int(c))

#   Program no 3:

import random
num= random.randint(1, 9)
guess=int(input("Enter a guess: "))
while(guess!=num):
  guess=int(input("Enter a guess: "))
print("Well guesed!")

#   Program no 4:

for i in range(0,5):
  for j in range(0,i+1):
    print("*" ,end=" ")
  print()
for i in range(4,0,-1):
  for j in range(1,i+1):
    print("*" ,end=" ")
  print()

#   Program no 5:

s=str(input("Enter a word: "))
rev = ''.join(reversed(s))
print(rev)

#   Program no 6:

number=[1,2,3,4,5,6,7,8,9]
j=0
k=0
for i in number:
 if i%2==0:
   j=j+1
 else:
   k=k+1
print("Number of even numbers: ",j)
print("Number of odd numbers: ",k)


#   Program no 7:

datalist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V',"section":'A'}]
for i in datalist:
     print(i)
     print(type(i)) 

#   Program no 8:


for i in range(0,7):
 if i==3 or i==6:
    continue
 else:
   print(i)

#   Program no 9:   

n1=0
n2=1
fib=1
while(fib<50):
    print(fib,end=" ")
    fib=n1+n2
    n1=n2
    n2=fib
print("")

#   Program no 10:

for i in range(1,51):
    if(i%3==0 and i%5==0):
      print("Fizzbuzz")
    elif (i%3==0):
     print("Fizz")
    elif (i%5==0):
     print("Buzz")
    else:
      print(i)

#   Program no 11:
  
rows=int(input("Enter a numbwe of rows: "))
cols=int(input("Enter a numbwe of columns: "))
for i in range(0,rows):
    for j in range(0,cols):
        print(i*j,end=" ")
    print(" ")

#   Program no 12:

list=[]
x="invalid"
while(x):
  x=input("Enter a line in lower case characters:")
  while not x.islower() and x: 
     x=input("All characters are not in lower case Please enter again:")
  list.append(x)
print("You entered")
for i in list:
  print(i)  

#   Program no 13:

list=[]
n = [x for x in input("Enter a sequence of comma separated 4-digit binary numbers: ").replace(' ', ',').split(',')]
for y in n:
   dec=int(y,2)
   if  not dec % 5 :
      list.append(y)
print(','.join(list))

#   Program no 14:

d=0
l=0
s=input("Enter a string:")
for i in s:
 if i.isalpha():
   l=l+1
 elif i.isdigit():
   d=d+1
print("Letters",l)
print("Digits",d)

#   Program no 15:

import re
x="False"
p=input('Enter a password: ')
while(True):
    if (len(p)<6 or len(p)>16):
      break
    elif not re.search("[a-z]",p):
      break
    elif not re.search("[A-Z]",p):
      break
    elif not re.search("[0-9]",p):
      break
    elif not re.search("[$#@]",p):
      break
    elif not re.search("/s",p):
      break
    else:
      print("Valid password")
      x="True"
      break
if x=="False":
  print("Invalid password")