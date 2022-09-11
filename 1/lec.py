#print("hello, world")

a = int(input("a= "))
b = int(input("b= "))
if a > b:
    print (a)
else:
    print (b)



original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //=10
print (inverted)