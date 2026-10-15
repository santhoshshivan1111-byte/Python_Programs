amount=float(input("Enter purchase amount:"))
if amount <0:
    print("Invalid amount")
else:
    discount=0.0
    if amount >=5000:
     discount=amount*20/100
    elif amount>=2000 and amount<5000:
     discount=amount*10/100
    print("Discount amount :",discount)
    print("Final payable amount:",amount-discount)