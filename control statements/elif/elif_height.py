height=int(input("enter ur height:"))
bill=0

if(height>=3):
    print("u can ride")
    age=int(input("enter ur age:"))
    if(age<12):
        bill=150
        print("pay 150 rs")
    elif(age<18):
        bill=250
        print("pay 250 rs")
    else:
        bill=300
        print("pay 300 rs")

    want_photo=input("do you want photo(y or n):")
    if want_photo=="y" or want_photo=="Y":
         bill = bill + 50
         print(f"total bill is {bill}")

else:
    print("cant ride")
    print("bye")