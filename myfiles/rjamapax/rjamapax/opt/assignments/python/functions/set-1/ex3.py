'''Write a function to take a dict, number X and number Y as arguments. 
Multiply each key by number X, each value by number Y. Finally iterate and return the new dict.'''

def mult_num(d1,x,y):
    d2={}
    d1=dict(d1)
    x=int(x)
    y=int(y)
    for i,j in d1.items():
        d2.[i*x]=j*y
    return d2
print(mult_num({10:1,9:2,8:3,7:4,6:5,5:6,4:7,3:8,2:9,},10,20))        