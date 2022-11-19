'''2. Write a function to take a list as an argument. Find all the elements that occur in ODD indexes.
    Example : 
        org_list=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
        result=func_exec(org_list)
        print(result)
        Expected Output : [2,4,6,2,9,100,2,10]
        :param orgList: Original list passed by the User
        :return: ODD indexes from list ONLY'''

#This function gives a new list with odd index elements in the original list
def check_odd_ind(org_list):

  #define an empty new list
  new_mapper=[] 
  # loop i value contains odd numbers
  for i in range(1,len(org_list),2): 
    #elements adds to new list from original list which are in odd indexs
    new_mapper.append(org_list[i]) 
  #finally return the new list with odd indexes elements 
  return new_mapper  

# Execution
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
#function calling
result=check_odd_ind(org_list=testList)
#finally print result
print("Final Result is :: {} ".format(result))
