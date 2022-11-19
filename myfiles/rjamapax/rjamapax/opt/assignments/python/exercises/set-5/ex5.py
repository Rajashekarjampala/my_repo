'''5. Write a function to take a dict as argument. Sort the dict by values and return the dict.
    Example : 
            testDict={1:4,10:20,3:40,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,4:7,12:9,60:11,10:20,3:40}
            :param org_dic: Original dictionary passed by the User
            :return: New dic with filtered values ONLY'''

#This function returns new sorted dictionary by values
def sort_value(org_dic):
    
    #define empty dictionary
    new_mapper={}
    #values() method gives list of values
    #stores sorted list of values
    _val=sorted(org_dic.values()) 
    #iterates values one by one
    for _key in _val:    
        #iterates keys from original dict one by one
        for _val in org_dic: 
            #checking for values and keys if condition true it adds to new dict. 
            if(_key==org_dic[_val]):   
                #add key-value pair to new dictionary
                new_mapper[_val]=_key  
    # finally return the new dic                         
    return new_mapper               

# Execution
testDict={1:4,10:20,3:40,4:7,60:11,12:9}
#function calling
result=sort_value(org_dic=testDict)
#finally print result
print("Final Result is :: {} ".format(result))

