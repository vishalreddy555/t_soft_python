import random
name=input("enter everybody name separate by comma:")

name_list=name.split(',')
#print(name_list)
length=len(name_list)

choice_name=random.randint(0,length-1)
print(f"{ name_list[choice_name]} will pay the bill")