#1- Extract the user id, domain name and suffix from the following email addresses. 

emails = "zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"
desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

import re
li=["zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"]
l2=[]
for i in li:
    l=re.split('[@./s]',i)
    l2.append(tuple(l))
    print(l2)


#2.Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."

import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
lst=re.findall('[bB]\w*',text)
print(lst)

#.3- Split the following irregular sentence into words 

sentence = "A, very very; irregular_sentence"
desired_output = "A very very irregular sentence"

import re
sentence = "A, very very; irregular_sentence"
l=re.sub('[\W_]',' ',sentence)
for i in l:\
    print(i,end="")
