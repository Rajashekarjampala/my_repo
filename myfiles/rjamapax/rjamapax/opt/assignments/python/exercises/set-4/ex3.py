'''3. Write a function to take a list as an argument. Find all the elements that occur in EVEN indexes &
   remove all duplicates.
    Example : 
        org_list=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10,300]
        result=func_exec(org_list)
        print(result)
        Expected Output : [1,300,5,7,8,19,11,200]
        :param orgList: Original list passed by the User
        :return: EVEN indexes from list ONLY'''

#This function gives new list with even index elements from original list
def check_eve_ind(org_list):

  #define new empty list
  new_mapper=[] 
  #loop i value contains even numbers and step number is 2
  for i in range(0,len(org_list),2):
    #even index elements from original list is adds to new list
    new_mapper.append(org_list[i]
  #finally returns new list  
  return new_mapper 

# Execution
testList=[1,2,300,4,5,6,7,2,8,9,10,100,11,2,200,10]
# function calling
result=check_eve_ind(org_list=testList)
# finally print the result
print("Final Result is :: {} ".format(result))