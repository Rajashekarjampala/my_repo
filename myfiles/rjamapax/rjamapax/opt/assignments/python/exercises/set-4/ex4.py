'''4. Write a function to take a dict and number X arguments. 
If the dict key is divisible by number X, then
   add the key to new dict and return the new dict.
    Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {10:20,60:11}
    Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            numX=101
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {}
             :param orgList: Original dictionary passed by the User
             :param numX: Number X passed by the User. Type is INT.
             :return: New dictionary with filtered values ONLY.'''

#This function gives a new dictionary with key-value pair which the keys from original dictionary is divisible by value x entered by the user
def check_div(org_dic,numx):#function defined
    
    #define new empty dictionary
    new_mapper={}
    
    #items method gives list of tuples from dictionary
    # iterates keys and  values from original dictionary
    for _key,_value in org_dic.items():
        #checking for is key divisible with value numx , if condition true the key and value is added to the new dictionary
        if (_key%numx==0):
            #adding key-value pair to new dictionary
            new_mapper[_key]=_value
    #finally return new dictionary        
    return new_mapper
    

# Execution
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
numx=10
#function calling
result=check_div(org_dic=testDict,numx=numx)
#finally print the result
print("Final Result is :: {} ".format(result))