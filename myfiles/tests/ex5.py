'''
Write a function to take a dict as argument. Find the key that has max value.
    Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {3:40}
            Reason: Key "3" has value of "40" >er than other values
'''
# Define function
def check_num(dic): 
    # Iterate the dic   
    for k,v in dic.items():
        # Store the dictionary values in variable
        val=dic.values()
        # Find the max value from dictionary
        if (v==max(val)):
            # Finally return  the key
            return k
            
print(check_num({1:4,10:20,3:40,4:7,60:11,12:9}))            

