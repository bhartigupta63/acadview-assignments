 #1
 l1=[]
 a = input("enter value")
 l1.append(a)
 b = input("enter value")
 l1.append(b)
 c = input("enter value")
 l1.append(c)
 print(l1)

 #2

 l2=['google','apple','facebook','microsoft','tesla']
 l1=l1+l2
 print(l1)

 #3

 l1=[1,2,3,4,1,5,1,6,1]
 print(l1.count(1))

 #4

 l1=[1,2,9,4,3,6,4,3,6,9]
 l1.sort()
 print(l1)

 #5

 l1=[4,3,4,2,6,1,9]
 l2=[8,4,6,3,7,2,8]
 l3=l1+l2
 l3.sort()
 print(l3)

 #6

 #stack
 l1=[]
 l1.append(2)
 print(l1)
 l1.append(5)
 print(l1)
 l1.append(7)
 print(l1)
 print(l1.pop(-1))
 print("now the list is ",l1)
 print(l1.pop(-1))
 print("now the list is ",l1)
 print(l1.pop(-1))
 print("now the list is ",l1)

 #queue
 l1=[]
 l1.append(2)
 print(l1)
 l1.append(5)
 print(l1)
 l1.append(7)
 print(l1)
 print(l1.pop(0))
 print("now the list is ",l1)
 print(l1.pop(0))
 print("now the list is ",l1)
 print(l1.pop(0))
 print("now the list is ",l1)
 
 #7(optional)

 l1=[1,2,3,4,5,6]
 even=0
 odd=0
 for x in l1:
     if x%2==0:
	even+=1
     else:
	odd+=1
 print("even numbers=",even)
 print("odd numbers=",odd)
 

 

 


 
