# amount=float(input("Enter purchase amount:"))
# if amount <0:
#     print("Invalid amount")
# else:
#     discount=0.0
#     if amount >=5000:
#      discount=amount*20/100
#     elif amount>=2000 and amount<5000:
#      discount=amount*10/100
#     print("Discount amount :",discount)
#     print("Final payable amount:",amount-discount)

# num=int(input("Enter the number:"))
# total=0
# for i in range(1,num+1):
#     total=total+i
# print(total)

# num1=int(input("Enter fnumber:"))
# num2=int(input("Enter Snumber:"))
# totals=0
# for i in range(num1,num2+1):
#     if i% 2==0:
#          totals+=i
# print(totals)

# num=int(input("Enter a number:"))
# for i in range(1,11):
#     print(num*i)

# a=int(input("Enter a number:"))
# b=0
# for i in range(1,11):
#     b=a*i
#     print(a,'x',i,'=',b)

# n=int(int())#123
# digits=0
# total=0
# while n!=0:
#     ren=n%10
#     digits+=1
#     total=total+ren
#     n=n//10
# print("No of digits:",digits)
# print("Sum of digits:",total)

# num=int(input())#38
# while not (num>=0 and num<=9):
#     sums=0
#     while num!=0:
#         ren=num%10
#         sums=sums+ren
#         num =num//10
#     else:
#         print(num)

# num=int(input())
# digits=0
# temp=num
# temp1=num
# while num!=0:
#     digits+=1
#     num//=10
# sums=0
# while temp!=0:
#     rem=temp%10
#     sums=sums+rem**digits
#     temp=temp//10
# if temp1==sums:
#     print("Amstrong Number")
# else:
#     print("Not Amstrong number")

# num=int(input())
# count=0
# for i in range (1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

# for i in range (1,11):
#     if i==6:
#         break
#     print(i,end="")
# print()
# for i in range (1,11):
#     if i==6:
#         continue
#     print(i,end="")

# if True and False:
#     pass
# else:
#     print("javasript")


# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end="*")
#     print()

n = 5

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
    
#     for j in range(2 * i - 1):
#         print("*", end="")
    
#     print()

# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*"  * (2 * i - 1))
    
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))


# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * i)

# for i in range(2, 6):       
#     print(" " * (5 - i) + "*" * i)


# list_1=[24,56,78,9,0,23,23]
# list_2=["jagan","kumar","santhosh","enba"]
# list_3=["santhosh",20,"M",9.0,"RGCET",True]
# print(list_1)
# print(list_2)
# print(list_3)

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


# num1=int(input("first number:"))
# num2=int(input("second number:"))
# operator=input("enter operator:")
# match operator:
#     case'+':print(num1+num2)
#     case'-':print(num1-num2)
#     case'*':print(num1*num2)
#     case'/':print(num1/num2)
#     case'//':print(num1//num2)
#     case'%':print(num1%num2)
#     case'**':print(num1**num2)

# a=input("enter the file extension:")
# match a:
#     case'py':print('python file')
#     case'c':print('c file')
#     case 'c++':print('c++ file')
#     case'html':print('HTML FILE')
#     case'jpg':print('image file')
#     case'_':print('unknown file type')

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


# number=int(input())
# fact=1
# for i in range (1,number+1):
#     fact=fact*i
#     print(i,end=" ")
#     if i<number:
#         print("*",end="")
#         print("=",fact)

# modules and division methods:

# n=int(input())
# digits=0
# total=0
# while n!=0:
#     rem=n%10
#     digits+=1
#     total=total+rem
#     n=n//10
#     print("no of digits:",digits)
#     print("sum of digits:",total)

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

# n=int(input()) # we need to fix star program 
# a=n-1
# b=1
# for i in range(1,n*2):
#     for j in range (1,a+1):
#         print(" ",end=" ")
#     for k in range (1,b+1):
#          print("*",end=" ")
#          print()
#     if i>=5:
#                 a+=1
#                 b-=2
# else:
#                 a-=1
#                 b+=2

#list-ordered mutable allow duplicate 
# traversal-visiting the all element in list




# numbers=[]
# n=int(input())
# for i in range(n):
#     data=int(input())
#     numbers.append(data)
#     print(numbers)


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

# list_7=[10,20,30,40,20,30]
# list_7.remove(30)
# print(list_7)
# list_7.pop()
# print(list_7)
# list_7.clear()


# print("index")
# list_7=[10,20,30,40,20,30]
# print(list_7[4])
# print(list_7[-4])

# #list slicing 
# nums=[10,20,30,40,50,60]
# print(nums[1:4])
# print(nums[:3])
# print(nums[::2])
# print(nums[-3:])
# print(nums[::-1])
# print(nums[::])

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
        