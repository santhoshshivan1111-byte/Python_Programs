





















# amount=float(input("enter purchase amount: "))
# if amount < 0:
#     print(" invalid amount")
# else:
#     discount=0.0
#     if amount>=5000:
#         discount=amount*20/100
#     elif amount>=2000 and amount < 5000:
#         discount=amount*10/100
#         print("discount amount :",discount)
#         print("final payable amount:",amount-discount) 


num1=int(input("first number:"))
num2=int(input("second number:"))
operator=input("enter operator:")
match operator:
    case'+':print(num1+num2)
    case'-':print(num1-num2)
    case'*':print(num1*num2)
    case'/':print(num1/num2)
    case'//':print(num1//num2)
    case'%':print(num1%num2)
    case'**':print(num1**num2)

a=input("enter the file extension:")
match a:
    case'py':print('python file')
    case'c':print('c file')
    case 'c++':print('c++ file')
    case'html':print('HTML FILE')
    case'jpg':print('image file')
    case'_':print('unknown file type')

# for i in range (10):
#      print("hello")
   

# for i in range (1,11):
#     print(i)

# for i in range (1,101,3):# for adding numbers '3'
#     print(i,end="")  

# for i in range(5,0,-1):#reverse the number order
#         print(i)

# num=int(input("enter number :"))
# total=0
# for i in range (1,num+1):
#      total=total+i
#      print(total)


# num= int(input()) # multiple tables enter the valu to run 
# for i in range (1,11):
#     print(num ,"*",i, "=",num*i) 


number=int(input())
fact=1
for i in range (1,number+1):
    fact=fact*i
    print(i,end=" ")
    if i<number:
        print("*",end="")
        print("=",fact)

modules and division methods:

n=int(input())
digits=0
total=0
while n!=0:
    rem=n%10
    digits+=1
    total=total+rem
    n=n//10
    print("no of digits:",digits)
    print("sum of digits:",total)

# add number to get single digit value answer:

# num=int(input())
# while not (num>=0 and num<=9):
#     sums=0
#     while num!=0:
#         rem=num%10
#         sums=sums+rem
#         num=num//10
#         num=sums
# else: 
#               print (num)

# num=int(input())
# digits=0
# temp=num
# temp1=num
# while num!=0:
#     digits=1
#     num//=10
# sums=0
# while temp!=0:
#     rem=temp%10
#     sums=sums+rem**digits
#     temp=temp//10
# if temp1==sums:
#     print("amstrong number")
# else:
#     print("not amstrong number")

# check the prime number

# num=int(input())
# count=0
# for i in range (1,num+1):
#     if num%i==0:
#         count+=1
#         if count==2:
#             print("prime number")
#         else:
#             print("not prime number")

# break,continue,pass:

# break:
# for i in range(1,11)
# if i==6:
#     break
# print(i,end=" ")
 
#continue:
# for i in range (1,11):
#     if i==6:
#         continue 
#     print(i,end=" ")


#pass:
# if True and False:
#     pass
# else:
#     print("javascript")

n=int(input()) # we need to fix star program 
a=n-1
b=1
for i in range(1,n*2):
    for j in range (1,a+1):
        print(" ",end=" ")
    for k in range (1,b+1):
         print("*",end=" ")
         print()
    if i>=5:
                a+=1
                b-=2
else:
                a-=1
                b+=2

#list-ordered mutable allow duplicate 
# traversal-visiting the all element in list




numbers=[]
n=int(input())
for i in range(n):
    data=int(input())
    numbers.append(data)
    print(numbers)


# list_5=[1,2,3,4,5]
# print(list_5)

# for data in list_5:
#     print(data,end="")
#     print()
#     i=0 #1<5
#     while i<len(list_5):
#         print(list_5[i],end=" ")
#         i+=1
#         print()

# list_6=[1,2,3,4,5]
# list_6.append(6)
# list_6.append(7)
# print(list_6)    
# list_6.insert(0,1000)
# print(list_6)

list_7=[10,20,30,40,20,30]
list_7.remove(30)
print(list_7)
list_7.pop()
print(list_7)
list_7.clear()


print("index")
list_7=[10,20,30,40,20,30]
print(list_7[4])
print(list_7[-4])

#list slicing 
nums=[10,20,30,40,50,60]
print(nums[1:4])
print(nums[:3])
print(nums[::2])
print(nums[-3:])
print(nums[::-1])
print(nums[::])

# nums_1=[10,30,40,10]
# print(10 in nums_1)
# print(nums_1.count(10))
# print(nums_1.index(30))


# nums_2=[32,78,12,0,-9]
# nums_2.sort()
# print(nums_2)
# nums_2.sort(reverse=True)
# print(nums_2)

# nums_3=[4,3,2,1]
# nums_3.reverse()
# print(nums_3)

# nums_4=[10,20,367,74,845,6372,83939]
# print(nums_4)
# print(sum(nums_4))

# nums_3=[4,3,2,1]
# nums_3.reverse()
# print(nums_3)

# nums_4=[56,78,2,3,6,9,4,5,1,2,98,45,23,78,90,345,788,12]
# print(len(nums_4))
# print(sum(nums_4))
# print(min(nums_4))
# print(max(nums_4))
 

# #two sums
# nums=[]
# n=int(input())
# for i in range(n):
#     data=int(input())
#     nums.append(data)

# target=int(input())
# found=False

# for i in range(n):
#   for j in range(i+1,n):
#      if nums[i]+nums[j]==target:
#         print(f"{i},{j}")
#         found=True
#         break
#     if found:
#         break
# if not found:
#      print("-1,-1")

# tuple_1=()


# number={1,2,3,4,5,}
# print(number)
# empty_set={45,67,89}
# print(empty_set)

# nums1=[1,2,3,4,5,6,7]
# unique_set=(nums1)
# print(unique_set)

# nums2=[1,2,3,1.2,3,3,3,2,4,67,567]
# unique_set =set(nums2)
# print(unique_set)

# nums3=discard(100)
# print(nums3)
# nums.clear()
# print(nums3)

# nums4={1,2,3,4,5,6,7,8,9}
# for value in nums4:
#     print(value,end="")
#     print()

# a={1,2,3}
# b={3,4,5}
# print(a,union(b))
# print(a,intersection(b))
# print(a,difference(b))



# student1={
#     "name":"santhosh",
#     "age":20
#     "mark":580,
#     "dept":ECE,
# }
# print(name)
# print(dept)
# print(dept[0])
# print(dept[1])
# print(dept[-1])
# #pyt
# print(dept[:3])
# #thon
# print(dept[2:6)
# #mohtlyp
# print(dept[::1])

# a="Python"#1000
# a="j"+a[1:]
# print(a)
# print(len(a))
# for ch in a:
#  print(ch)

def greet(n):

def counts(num):
    if num==11:
        return
    print(num,end="")
    counts(num+1)
    count(1)

class phone :
    def camera(self)
        print("Taking a normal photo")

class smartphone :
    def camera(self)
        print("Taking a portrait photo")

smasung=smartphone()
smasung.camera()
nokia=phone
nokia.camera

class bank:
    _amount=8000
    def printamount(self):
        return self._amount
    hdfc=bank()
    print(hdfc.print)

class payment (ABC):
    abstract method
    def pay (self)
        pass
    class UPI(Payement):
        def pay (self):
            print("Payment done using upi")

bitwise operator
a= int(input())
b= int(input())
print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)

number=int(input())
result="Even"if number%2==0 else"Odd"
print(result)

a=3
if a>0:
    print("Positive")
elif a<0:
    print("Negative")    
else:
    print("Zero")    
      

mark=int(input())
if mark in range(90,100):
    print("A")
elif mark in range(75,89):
    print("B")
elif mark in range(60,74):
    print("C")        
elif mark in range(40,59):
    print("D")
else:
    print("Fail")         
 
ifelse
amount=float(input("Enter the purchase amount:"))
if amount<0:
 print("Invalid amount")
else:
 discount=0.0
if amount>=5000:
 discount=amount*20/100
elif amount>=2000 and amount <5000:
 dicount=amount*10/100
print("Discount amount:",discount)
print("Final payable amount:",amount-discount)    


match case
num1=int(input("Enter the first value"))
num2=int(input("Enter the second value"))
operator=input("Enter the operator:")
match operator:
    case '+' :print(num1+num2)
    case '-' :print(num1-num2)
    case '*' :print(num1*num2)
    case '/' :print(num1/num2)  
    case '//' :print(num1//num2)
    case '%' :print(num1%num2)
    case '**' :print(num1**num2)


file=(input("Enter file extension:"))
match file:
       case'py' :print("python file")
       case'c' :print("c file" )
       case'c++' :print("c++ file ")
       case'html' :print("html file" )
       case'jpg' :print("jgp file" )
       case _:print("unknown file type" )



for loop to print more times same thing
for i in range(10):
    print("hello Kee")

for loop for start stop num
for i in range(1,11):
    print(i)

for i in range(1,101,3):
    print(i,end=" ")

to add number and add even numbs
num=int(input("Enter number:"))
total=0
for i in range(1,num+1):
    total=total+i
print(total)


num1=int(input("Enter Fnumber:"))
num2=int(input("Enter Snumber:"))
totals=0
for i in range(num1,num2+1):
    if i%2==0:
        totals+=i
print(totals)        


tables 
num = 5
for i in range(1,11):
    num1=num*i
    print(num,"*",i,"=",num1)   


to multiply numbers
number=int(input())
fact=1
for i in range(1,number+1):
    fact=fact*i
    print(i,end=" ")
    if i<number:
        print("*",end=" ")
print("=",fact)


while loop to calculate sum and num of digits
n=int(input()) #12345
digits=0
total=0
while n!=0:
    rem=n%10
    digits+=1
    total=total+rem
    n=n//10
print("N0 of digits:",digits)
print("sum of digits:",total)    

to print digit until it become single digit 
num=int(input())#38
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums=sums+rem
        num=num//10
    num=sums
else:
    print(num)      


to find Amstrong number 
num=int(input()) #153
digits=0
temp=num
temp1=num
while num!=0:
    digits+=1
    num//=10
sums=0
while temp!=0:
    rem=temp%10
    sums=sums+rem**digits
    temp=temp//10
if temp1==sums:
    print("Amstrong number")
else:
    print("Not Amstrong number")       



to print prime numbers
num=int(input())
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("Prime number")
else:
    print("Not Prime number ")        



break,continue,pass
for i in range(1,11):
    if i==6:
        break   #to stop at current loop
    print(i,end=" ")
print()
for i in range(1,11):
    if i==6:
       continue         #to continue from next
    print(i,end=" ")
if True and False:
    pass                 #for future use
else:
    print("Javascript")        


to print stars
n=int(input())#5
a=n-1
b=1
for i in range(1,n*2):
    for j in range(1,a+1):
        print(" ",end=" ")
    for k in range(1,b+1):
        print("*",end=" ")
    print()  
    if i>=5:
        a+=1
        b-=2
    else:
        a-=1
        b+=2

 

to print stars
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()     



List ordered mutable allow duplicate
list_1=[24,56,78,9,0,23,23]
list_2=["Jagan","KUmar","Navin","Praveen"]
list_3=["Naveen",18,"N",9.8,"RGCET",True]
print(list_1)
print(list_2)
print(list_3)
print(type(list_1))
list_4=[10,20,30,40]
list_4[2]=300
print(list_4)

list_5=[1,2,3,4,5]
print(list_5)

for data in list_5:
    print(data,end=" ")
print()
i=0 
while i<len(list_5):
    print(list_5[i],end=" ")
    i+=1
print()    
list_6=[1,2,3,4,5]
list_6.append(6)
list_6.append(7)
print(list_6)
list_6.insert(0,1000)
print(list_6)

list_7=[10,20,30,40,20,30]
list_7.remove(30)
print(list_7)
list_7.pop
print(list_7)
list_7.clear()
print(list_7)

print("Index")
list_7=[10,20,30,40,20,30]
print(list_7[4])
print(list_7[-4])


list slicing
nums=[10,20,30,40,50,60] #list[start:stop:step]

print(nums[1:4])
print(nums[:3])
print(nums[3:])
print(nums[::2])
print(nums[-3:])
print(nums[::-1])
print(nums[:])

nums_1=[10,30,40,10]
print(10 in nums_1)
print(nums_1.count(10))
print(nums_1.index(10))

nums_2=[32,78,12,0,-9]
nums_2.sort()
print(nums_2)
nums_2.sort(reverse=True)
print(nums_2)

nums_3=[4,3,2,1]
nums_3.reverse()
print(nums_3)

nums_4=[56,78,2,3,6,9,4,5,1,2,90,45,23,78,90,345,788,12]
print(len(nums_4))
print(sum(nums_4))
print(min(nums_4))
print(max(nums_4))


to find sum of numbers 
nums=[]
n=int(input())
for i in range(n):
    data=int(input())
    nums.append(data)
target=int(input())
found=False
for i in range(n):
     for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print(f"{i},{j}")
            found=True
            break
        if found:
            break
if not found:
    print("-1,-1")
 


 ordered immutable allow duplicate
tuple_1=(34,67,89,23)
print(tuple_1)
print(type(tuple_1))

tuple_2=(5,)
print(type(tuple_2))

tuple_3=(12,45,67,89,23)
for data in tuple_3:
    print(data,end=" ")
print()
i=0
while i<len(tuple_3):
    print(tuple_3[i],end=" ")
    i+1=1
print()
tuple_4=(1,2,3,2,3,1)
print(tuple_4.count(3))
print(tuple_4.index(3))

print(len(tuple_4))
print(max(tuple_4))
print(min(tuple_4))

tuple_1 = (10,20,10,30,20,40)
for num in set(tuple_1):
    if tuple_1.count(num) >1:
        print(num)


Set -unique unordered mutable
numbers={1,2,3,6,4,3,2}
print(numbers)
names={"Abi","Bash","Ash","Kee"}
print(names)
empty_set=set() #create empty set
empty_set={45,67,89}
print(empty_set)

nums1={10,20,30,40}
print(nums1)
nums1.add(50)    #to add only one number
print(nums1)
nums1.update([60,70,80])   #to add multiple numbers
print(nums1)

nums2=[1,2,3,1,2,3,3,2,4,67,88]
unique_set=set(nums2)
print(unique_set)

nums3={56,78,90,34,12}
nums3.remove(56)
print(nums3)
nums3.discard(12)
print(nums3)
# nums3.remove(100)
# print(nums3)
nums3.discard(100)
print(nums3)
nums3.clear()
print(nums3)

nums4={1,2,3,4,5,6,7,8,9}
for value in nums4:
    print(value,end=" ")
print()
a={1,2,3,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))



disctionary- mutable,collection of key value pairs key unique values repeat
student1={
    "name":"Kee",
    "age":20,
    "mark":459,
    "dept":"ECE"
}
print(student1)
print(student1["name"])
print(student1["age"])
print(student1.get("mark")) #to access
print(student1.get("city","Not Applicable"))
student1["mark"]=499 #to updaate
print(student1)
student1["city"]="Pondy" #to add
print(student1)
student1.pop("age")
print(student1)

for a,b in student1.items():
    print(a," :",b)

strings-collection of chara and immutable
name="Kee"
dept='python'
print(name)
print(dept)
print(dep[0])
print(dept[1])
print(dept[-1])
#pyt
print(dept[:3])
#thon
print(dept[2:6])
#pyth
print(dept[0:4])
#nohtyp
print(dept[::-1])

a="Python" #1000
a="J"+a[1:]
print(a)
print(len(a))
for ch in a:
    print(ch,end=" ")
print()
text="Java Programming"
print(text.upper())    



function
def greet(): #function def
    print("hi Jagan")
greet() #func calling
greet()

def addition(a,b):
    print(a+b)

addition(5,6)  #method calling with argument or parameter
addition(100,200)
addition(200,300)

def multiplication(a,b,c):
    return a*b*c

result=multiplication(5,5,5) #method calling with argument with return
print(result)


Global variable and local variable














recursion - function calling  itself - loop

def greet(n):
    if n==0:
        return
    print("Hello Kee")
    greet(n-1)
greet(5)

def counts(num):
    if num==11:
        return
    print(num,end=" ")
    counts(num+1)
counts(1)
print()
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input())
result=factorial(n)
print(result)

a=0
b=1
print(a," ",b,end=" ")
for i in range(3,11):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
print()
def fib(num):
    if num==0 or num==1:
        return num
    return fib(num-1)+fib(num-2)

num=int(input())
print(fib(num))




lambda function
lambda arguments:expression
import math
from math import sqrt
import Calculator
addition=lambda a,b:a+b
print(addition(4,3))
square=lambda a:a*a
print(square(5))

#modlues and packages
print(math.sqrt(25))
print(math.factorial(25))
print(math.pi)

print(Calculator.multi(5,5,5))

#Exception Handling
try:
    a=int(input())
    b=int(input())
    c=a//b
    print(c)
except ZeroDivisionError:
    print("Please enter positive number")
except ValueError:
    print("Enter integer only")
finally:
    print("Java Programming")    



oops - Object oriented programming language or system
Class Object inheritance polymorphism encapsulation abstraction interface
class studenttwo:
    def display(self):
        print(self.name," ",self.mark)

class studentone:
   name="Ash"
   age=20
   dept="ECE"
   def marks(self):
       print("Maths: 90,English: 78")

class studentthree:
    name="unknown"
    mark=0
    def _int_(self,name,mark):
        self.name=name
        self.mark=mark


#def setdetails(self,name,mark):
# self.name=name
# self.mark=mark
def printdetails(self):
    print(self.name," ",self.mark)


s1=studentone()
print(s1.name)
print(s1.age)
s1.marks()

s2=studenttwo()
s2.name="Kee"
s2.mark=345
s2.display()
s3=studenttwo()
s3.name="Kii"
s3.mark=456
s3.display()

s4=studentthree("kumar",34)
#s4.seddetails("jagan",500)
s4.printdetails()



single inheritance -> one parent class one child class
class Device:
    def power_on(self):
        print("Device switched on")
class Phone(Device):
    def call(self):
        print("Making a phone call") 
samsung=Phone()
samsung.power_on()
samsung.call()
print()
#multilevel inheritance -> Grandparent ->parent ->son
class Device:
    def power_on(self):
        print("Device switched on")
class Computer(Device):
    def run_program(self):
        print("Running a Python program")
class Laptop(Computer):
    def charge(self):
        print("Laptop battery charging")            
asus=Laptop()
asus.power_on()
asus.run_program()
print()


#multiple inheritance one child class multiple  parent class
class Camera:
    def take_photos(self):
         print("taking a photo")
class musicplayer:
    def play_music(self):
        print("playing a music") 
class smartphone(Camera,switched on)                                          




hierarchial inheritance - one parent class multiple child class
class Device:
    def power_on(self):
        print("Device switched on")
class Phone(Device):
    def call(self):
        print("Making a phone call")
class Computer (Device):
    def run_program(self):
        print("Running a python program")        
samsung=Phone()
samsung.call()
samsung.power_on()
hp=Computer()
hp.power_on()
hp.run_program()



Polymorphism
method overriding - method overriding means redefining a parent class met
child class with the same name and parameters to provide different behaviour
class Phone:
    def Camera(self):
        print("Taking a normal Photo")
class Smartphone(Phone):
    def Camera(self):
        print("Taking a portrait Photo")
samsung=Smartphone()
samsung.Camera()
nokia.Camera()
#Encapsulation
class bank:
    _amount=800
    def printamount(self):
        return self._amount
hdfc=bank()
print(hdfc.printamount())
#Abstraction-hiding the internal details and showing only essential
#feature
from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass                
class UPI(payment)
    def pay(self):
        print("payment done using phonepe")
payment=UPI()
payment.pay()
payment=phonepe()
payment.pay()
