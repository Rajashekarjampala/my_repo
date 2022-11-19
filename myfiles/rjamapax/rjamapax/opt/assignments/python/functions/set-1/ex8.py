'''Write a function to take a list, number X as arguments. 
From the list pick the elements that are not divisible by number X. Add those elements to new list. Finally return the new list.'''

def pic_ele(l1,x):
    l1=list(l1)
    l2=[]
    x=int(x)
    for i in l1:
        if (i%x!=0):
            l2.append(i)
    return l2
print(pic_ele([12,4,45,89,99,100,50],5))            