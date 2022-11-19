'''5. Write a function to take a dict and number X arguments. 
If the dict key is NOT divisible by number X, then
   add the key to new dict and finally return the new dict.
    Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {1:4,3:4,4:7,12:9}
    Example : 
            testDict={1:4,101:20,130:4,41:7,601:11,120:9}
            numX=5
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {1:4,101:20,41:7,601:11}
    Example : 
            testDict={1:4,101:20,130:4,41:7,601:11,120:9}
            numX=1
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {}
            :param orgDict: Original dictionary passed by the User
            :param numX: Number X passed by the User. Type is INT.
            :return: New dictionary with filtered values ONLY.'''

#This function gives a new dictionary with key-value pair which the keys from original dictionary is not divisible by value x entered by the user
def check_not_div(org_dic,numx):
    
    #difine an empty dictionary
    new_mapper={} 
    
    #items method gives list of tuples from dictionary
    # iterates keys and values from original dictionary
    for _key,_value in org_dic.items():
        #checking for is key not divisible with value numx , if condition true the key and value is added to the new dictionary
        if (_key%numx!=0):
            #adding key-value pair to new dictionary
            new_mapper[_key]=_value
    #finally returns new dictionary        
    return new_mapper 
    

# Execution
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
numx=10
#function calling
result=check_not_div(org_dic=testDict,numx=numx)
#finally print the result
print("Final Result is :: {} ".format(result))
