'''Write a function to take a dict as an argument. Multiply each key by 10, each value by 5. 
Finally iterate and return the new dict.'''

def mult_num(d1,x,y):
    d1=dict(d1)
    d2={}
    x=int(x)
    y=int(y)
    for i,j in d1.items():
        d2[i*10]=j*5
    return d2
print(mult_num({10:1,9:2,8:3,7:4,6:5,5:6,4:7,3:8,2:9,1:10},10,5))        

