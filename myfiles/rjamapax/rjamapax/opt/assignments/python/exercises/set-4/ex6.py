'''6. Write a function to take 2 lists. Iterate both the lists, 
   if the elements in both the lists match then add it to new list.
   From that list select all elements in ODD indexes.
   Finally return the new list. The new list must not contain duplicates.
    Example :
        org_listA=[10,20,30,40,50,60,100]
        org_listB=[10,200,30,40,500,60,100,400,90]
        result=func_exec(org_listA,org_listB)
        print(result)
        Expected Output : [30,100]
    Example :
        org_listA=[10,20,30,40,50,60,100]
        org_listB=[101,2001,130,140,1500,610,1100,4001,190,901]
        result=func_exec(org_listA,org_listB)
        print(result)
        Expected Output : []
        :param org_list: Original list(org_listA,org_listB) passed by the User
        :return: New list with filtered values ONLY'''

def check_mat(org_listA,org_listB):
    #define an empty list
    match_list=[]
    #define an empty list
    final_list=[]
    #iterates 2 different list Simantanously using zip
    for (_key,_value) in zip(org_listA,org_listB):
            #checking for elements from both lists are equal if condition true element adds to new empty list
            if (_key==_value):
                #add element to new list
                match_list.append(_key)    
    
    #checking for duplicates 
    # loop is value contains even numbers                  
    for _key in range(1,len(match_list),2): 
        #checking for an element is not present already in new list if condition true an element is adds to new list
        if (_key not in final_list):
            #adding elements to new list
            final_list.append(match_list[_key])
    #finally return list without duplicates        
    return final_list

# Execution
testListA=[10,20,30,40,50,60,100]
testListB=[10,200,30,40,500,60,100,400,90]
#function calling
result=check_mat(org_listA=testListA,org_listB=testListB)
#finally print result
print("Final Result is :: {} ".format(result))
