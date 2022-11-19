'''Define a list of 10 elements. If the element is even then multiply that element by 100, 
if the element is odd then multiply that element by 200. Finally print the new list'''

lst=[11,100,127,99,128,331,990,23,68,10]
new_lst=[]
for i in lst:
    if(i%2==0):
        new_lst.append(i*100)
    else:
        new_lst.append(i*200)
print(new_lst)