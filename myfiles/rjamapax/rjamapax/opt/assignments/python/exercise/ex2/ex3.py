'''Define a dictionary with 10 keys. If the dict key is > 10, then add it to new dict. 
Finally iterate and print the new dict'''

dct={11:1,9:2,8:3,0:4,76:5,5:6,4:7,3:8,922:9,911:10}
new_dct={}
for i,j in dct.items():
    if(i>10):
        new_dct[i]=j
print(new_dct)