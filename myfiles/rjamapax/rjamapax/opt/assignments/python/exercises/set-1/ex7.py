'''Write a function to take a list as an argument. From the list pick the elements that are not divisible by 5. 
Add those elements to new list. Finally return the new list.'''

def div_num(l1,x):
    l1=list(l1)
    l2=[]
    x=int(x)
    for i in l1:
        if (i%5!=0):
            l2.append(i)
    return l2
print(div_num([5,12,15,23,14,99,100],5))                  
            

