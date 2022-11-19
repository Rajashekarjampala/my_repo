'''Write a function to take a list as an argument. If the element is even then multiply that element by 100, 
if the element is odd then multiply that element by 200. Finally return the new list.'''

def mult_num(l1,x,y):
    l1=list(l1)
    l2=[]
    x=int(x)
    y=int(y)
    for i in l1:
        if (i%2==0):
            l2.append(i*100)
        else:
            l2.append(i*200)
    return l2
print(mult_num([11,100,127,99,128,331,990,23,68,10],100,200))           