'''3. Write a function to take a list. Select the number that is greater than product of all other numbers.
    Example :
        listA=[1,2,30,4,2]
        result=func_exec(listA)
        print(result)
        Expected Output : 30
        Reason: 30 is greater than product of [1,2,4,2] -> 16
    Example :
        listA=[1,2,3,4,2]
        result=func_exec(listA)
        print(result)
        Expected Output : []
        :param org_list: Original list passed by the User        
        :return: New list with filtered values ONLY
Solution Steps:
1. First iterate the list
2. Cheking for removed element is great than product of remaing elements in the list   
3. checking for number is greater than of product of remaining numbers in the list
3. Return greatest number in the list              
                
        '''
# This function is define pick greater number sum of all the list       
def check_greater(org_list):

    # iterate the orginal list
    for i in org_list:
        # assigning org list to another variable like new_mapper 
        new_mapper=org_list
        # remove a selected element from the New list
        new_mapper.remove(i)
        