'''2. Write a function to take a list. Sort and return the new list.
    Example :
        listA=[100,20,300,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [20,40,50,60,100,100,300]
        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY'''   

#This function gives a new sorted list
def check_sort(org_list):

    #define new list
    new_mapper=[]
    # sort the orginal list as listA
    for i in sorted(org_list):
        #adds to new list
        new_mapper.append(i)
    #Finally return new sorted list           
    return new_mapper
    
# Execution
testList=[100,20,300,40,50,60,100]
#Calling function
result=check_sort(org_list=testList)
#output final result
print("Final Result is :: {} ".format(result))

