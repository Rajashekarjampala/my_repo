'''Define a dictionary with 10 keys. Multiply each key by 10, each value by 5.
Finally iterate and Print the new dict.'''

dct={10:1,9:2,8:3,7:4,6:5,5:6,4:7,3:8,2:9,1:10}
new_dct={}
for i,j in dct.items():
        new_dct[i*10]=j*5
print(new_dct)