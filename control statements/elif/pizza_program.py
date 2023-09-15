pizza=(input("enter which pizza u want(s,m,l):"))
bill=0

if pizza == "s":
    bill+=100
    print("price is 100 rs")

elif pizza=="m":
    bill+=200
    print("price is 200 rs")

elif pizza=="l":
    bill+=300
    print("price is 300 rs")

add_pepperoni=input("do u want pepperoni(y or n):")
if add_pepperoni=="y" or add_pepperoni=="Y":
    if pizza == "s":
        bill+=30
    else:
        bill+=50

add_extracheese=input("do u want extra cheese(y or n):")
if add_extracheese=="y" or add_extracheese=="Y":
    bill+=20

print(f"ur final bill is :{bill}")



