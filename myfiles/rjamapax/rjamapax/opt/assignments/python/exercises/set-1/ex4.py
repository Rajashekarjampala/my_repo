'''Write a function to take a dict, number X as arguments.
If the dict key is > number X, then add it to new dict. Finally iterate and return the new dict.'''

def num_gre(d1,x):
    d2={}
    d1=dict(d1)
    x=int(x)
    for i,j in d1.items():
        if (i>x):
            d2[i]=j
    return d2
print(num_gre({11:1,9:2,8:3,0:4,76:5,5:6,4:7,3:8,922:9,911:10},50))            
