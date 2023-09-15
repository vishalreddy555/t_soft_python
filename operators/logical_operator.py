a,b=5,4
c=0
d=1
print(a>b and a>b)  #true
print(a<b and a>b)  #false
print(a>b and a<b)  #false
print(a<b and a<b)  #false

#OR

a,b=5,4
print(a>b or a>b)  #true
print(a<b or a>b)  #true
print(a>b or a<b)  #true
print(a<b or a<b)  #false

#not
print(not (c))  #true
print(not (d))  #false
