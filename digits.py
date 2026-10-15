n=int(int())#123
digits=0
total=0
while n!=0:
    ren=n%10
    digits+=1
    total=total+ren
    n=n//10
print("No of digits:",digits)
print("Sum of digits:",total)