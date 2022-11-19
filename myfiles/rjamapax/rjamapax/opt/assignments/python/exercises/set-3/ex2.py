'''2. Write a function to take a org_dict as an argument. Find the key that has maximum value and return the key.
    Example : 
        testorg_Dict={1:4,10:100,3:90,4:40,6:80,12:200}
        result=func_exec(testorg_Dict)
        print(result)
        Expected Output : 12
        Reason: Output is 12 since 12 has value of 200 which is greater than other values
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY'''

# This function is define maximum value and return the key
def max_key(org_dic):

    #stores list of values from org_dic
    val=org_dic.values()    
    #items method gives list of tuples from org_dictionary
    # key and values iterates Simanatanously
    for _key,_value in org_dic.items():           
           #checking for largest value in the org_dictionary, if condition true it returns the key for that large value
           if (max(val)==_value):
              #finally returns the key of large value pair
              return _key             

# Execution
test_Dict={1:4,10:100,3:90,4:40,6:80,12:200}
result=max_key(org_dic=test_Dict,)
print("Final Result is :: {} ".format(result))