#1

for x in range(10):
   y = int(input("Enter a number: "))
   print("The number is: ",y)


#2


count = 10
while(count>0):
   print("We have entered an infinite loop!")


#3


l1=[]
for x in range(5):
   y = int(input("Enter an integer value: "))
   l1.append(y)

print("Entered list is: ",l1)
l2=[]
for x in l1:
   z = x*x
   l2.append(z)

print("Updated list is: ",l2)


#4


l1 = [1,2,'Ronaldo',7,9.2,'bale',3.6]
l2 = []
l3 = []
l4 = [] 
for x in l1:
   if  type(x) == int:
      l2.append(x)
   elif type(x)== str:
      l3.append(x)
   elif type(x) == float:
      l4.append(x)

print("List of integers: ",l2)
print("List of strings: ",l3)
print("List of floats: ",l4)


#5


even = []
odd = []

for x in range(1,101):
    if not x % 2:
        even.append(x)
    else:
        odd.append(x)

print("List of even numbers: ",even)
print("List of odd numbers: ",odd)


#6

c = 1
while(c<=4):
    print("*"*c)
    c = c+1


#7


d = {'One':1,'Two':2,'Three':3,'Four':4}
for x in d.keys():
    print(x,d[x])


#8


l1=[]
s = int(input("Enter the size of list"))
for x in range(s):
    y = int(input("Enter value: "))
    l1.append(y)
d = int(input("Enter element to be deleted"))
for x in l1:
    if x == d:
        l1.remove(x)
    else:
        print("Element not in the list")
print("The list is: ",l1)






