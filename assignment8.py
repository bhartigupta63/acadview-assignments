#1

#We represent time in a way that’s easy for us to understand. However, Python stores it in tuples. These python tuples are made of nine numbers.
#Leap seconds are added to make up to Earth’s slowing rotation. When DST is 0, it isn’t applied. When it’s 1, it is applied. However, when it is -1, it is up to the library to determine that.
#This tuple has an equivalent struct_time structure.

#2
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d"))

#3

 import datetime
 x = datetime.datetime.now()
 print(x.month)

 #4

 import datetime
 x = datetime.datetime.now()
 print(x.day)

 #5

 import datetime
 #11/01/2021
 d = datetime.datetime(2021,1,11)
 print(d.year,d.month,d.day)

 #6

 import time
 print(time.localtime())

 #7

 import math
 x = int(input("enter the number"))
 print(math.factorial(x))

 #8

 import math
 x=int(input("enter first number"))
 y = int(input("enter second number"))
 print(math.gcd(x,y))

 #9

 import os
 print(os.getcwd())
 print(os.environ)



 
 
