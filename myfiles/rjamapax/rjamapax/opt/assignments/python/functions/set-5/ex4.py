'''4. Write a function to take a dict as argument. Sort the dict by keys and return the dict.
    Example : 
            testDict={1:4,10:20,3:4,4:7,60:11,12:9}
            result=func_exec(testDict)
            print(result)
            Expected Output : {1:4,3:4,4:7,12:9,20:3,60:11}
            :param org_dic: Original dictionary passed by the User
            :return: New dic with filtered values ONLY'''

#This function returns new sorted dictionary
def check_sort(org_dic):

    #define empty dictionary
    new_mapper={}    
    #sorted method on dictionary gives a list with sorted keys
    #iterates keys from least to maximum
    for i in sorted(org_dic):
        #adds key-value pair to new dictionary
        new_mapper[i]=org_dic[i]
    #finally return the new dic    
    return new_mapper


# Execution
testDict={1:4,10:20,3:4,4:7,60:11,12:9}
#function calling
result=check_sort(orgDictsort=testDict)
#finally print result
print("Final Result is :: {} ".format(result))