#1

radius = int(input("Enter the radius: "))
def area(radius):
   a = 3.14*radius*radius
   print("area of circle:",a)

area(radius)
   

#2


def Perfect(n):
   summ = 1
   i = 2
   while(i*i<=n):
      if n%i == 0:
         summ = summ+ i + n/i
      i+=1
      return(True if summ == n and n!=1 else False)
print("Below are all perfect numbers")
n = 2
for n in range(1000):
   if Perfect(n):
      print(n)


#3



def multiply(n, i=1):
   print(n*i)
   if(i == 11):
      return 1
   else:
      multiply(n, i+1)
   
n = 12
multiply(n)


#4


def power(a,b):
   
   if(b == 0):
      return 1
   else:
      return(a*power(a, b-1))
   
a = int(input("Enter the number: "))
b = int(input("Enter the power"))
print("Answer: ",power(a,b))


#5


def fact(n):
   
   if(n == 0):
      return 1
   else:
      return(n*fact(n-1))
d={} 
n = int(input("Enter the number: "))
a = fact(n)
print("Factorial: ",a)
d = {n:a}
print("Dictionary is: ", d)
