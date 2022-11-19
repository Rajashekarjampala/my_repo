'''From the list pick the elements that are not ODD. 
Add those elements to new list. Finally print the new list.'''

lst=[11,100,127,99,125,331,990,23,68,10]
new_lst=[]
for i in lst:
    if(i%2==0):
        new_lst.append(i)
print(new_lst)