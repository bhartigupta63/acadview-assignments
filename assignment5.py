
#1

year = int(input("Enter the year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("%d is a leap year" %(year))
       else:
           print("%d is not a leap year" %(year))
   else:
       print("%d is a leap year" %(year))
else:
   print("%d is not a leap year" %(year))


#2

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
if (l == b):
    print("It is a sqaure")
else:
    print("It is a rectangle")

#3

a = int(input("enter age of first person "))
b = int(input("enter age of second person "))
c = int(input("enter age of third person "))
if ( a > b and a > c):
    print("First person is oldest")
    if(b > c):
        print("Third person is youngest")
    else:
        print("Second person is youngest")
elif ( b > a and b > c):
    print("Second person is oldest")
    if(a > c):
        print("Third person is youngest")
    else:
        print("First person is youngest")
else:
    print("Third person is oldest")
    if(b > a):
        print("First person is youngest")
    else:
        print("Second person is youngest")


#4


points = int(input("Enter points earned by the participant(upto 200): "))
if (points > 0 and points <= 50):
    print("Sorry! No prize this time!")
elif(points > 50 and points <= 150):
    print("Congratulations! You have won a Wooden Dog")
elif(points > 150 and points <= 180):
    print("Congratulations! You have won a Book")
elif(points > 180 and points <= 200):
    print("Congratulations! You have won a Chocolates")

#5

quantity = int(input("Enter the quantity of items: "))
cost = quantity*100
if cost > 1000:
    print("You got 10% discount")
    discount = (cost*10)/100
    updated_cost = cost - discount
    print("You need to pay %d" %(updated_cost))
else:
    print("You need to pay %d" %(cost))
