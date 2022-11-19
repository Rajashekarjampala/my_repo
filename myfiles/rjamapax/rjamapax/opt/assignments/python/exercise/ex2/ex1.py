'''Define a list of 10 elements. From the list pick all numbers that are > er 100. 
Add those numbers to new list. Finally print the new list.'''

lst=[12,100,122,98,128,300,990,24,68,10]
new_lst=[]
for i in lst:
    if(i>100):
        new_lst.append(i)
print(new_lst)