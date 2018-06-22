#lists
#1

tup = (1,2,'bharti','gupta',(1,2))
print(len(tup))

#2

tup=(1,2,4,7,2,5,8,0)
print("maximum value is: ",max(tup))
print("minimum value is: ",min(tup))

#3

tup = (1,2,4,7,2,5,8)
product=1
for x in tup:
    product = product*x
print("product: ",product)

#sets
#1

set1={2,1,3,4,6,7}
set2={1,4,7,5,8}
print("difference: ", set1 - set2)
print("comparison: ", set1<=set2)
print("intersection: ", set1 & set2)

#dictionaries
#1

dict = {}
for i in range(10):
    name = input("enter name")
    marks = int(input("enter marks"))
    dict[name] = marks
print(dict)

#2 Sir said to leave

#3

dict={}
str = "MISSISSIPPI"
m = str.count('M')        
i = str.count('I')
s = str.count('S')
p = str.count('P')
dict['M']= m
dict['I']= i
dict['S']= s
dict['P']= p
print(dict)






