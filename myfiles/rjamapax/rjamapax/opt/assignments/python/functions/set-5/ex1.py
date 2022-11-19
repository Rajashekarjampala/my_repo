'''1. Write a function to take a list. Reverse and return the new list.
    Example :
        listA=[10,20,30,40,50,60,100]
        result=func_exec(listA)
        print(result)
        Expected Output : [100,60,50,40,30,20,10]
        :param org_dict: Original dictionary passed by the User
'''
# function define the reverse the list
def reverse_list(org_list):

  # define empty list
  new_mapper = [] 
  # itearate the orginal list
  for i in reversed(org_list): 
    # add elements in to new list
    new_mapper.append(i) 
  # finally return the new list
  return new_mapper 

# Execution
testList=[10,20,30,40,50,60,100]
#function calling
result=reverse_list(org_list=testList)
# print the result
print("Final Result is :: {} ".format(result))
