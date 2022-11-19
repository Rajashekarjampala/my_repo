'''Write a function to take a list, number X, number Y as arguments. If the element is even then multiply that element by number X, 
if the element is odd then multiply that element by number Y. Finally return the new list.'''

def mult_num(l1,x,y):
    l1=list(l1)
    l2=[]
    x=int(x)
    y=int(y)
    for i in l1:
        if (i%2==0):
            l2.append(i*x)
        else:
            l2.append(i*y)
    return l2
print(mult_num([2,5,8,9,3,4],2,3))              