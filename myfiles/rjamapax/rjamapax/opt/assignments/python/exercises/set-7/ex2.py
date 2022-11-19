'''2. Write a function to take a list, number Y as arguments.
    Filter all the numbers from the EVEN indexes, divisible by number Y. Remove duplicates.
    Example :
        listA=[10,20,30,40,50,60,100,11,12,13]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [30,50,100]
    Example :
        listA=[10,21,301,41,501,50,1100,11,12,13]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [1100]
    Example :
        listA=[10,20,30,40,50,60,100,11,120,13,100]
        numY=10
        result=func_exec(listA,numY)
        print(result)
        Expected Output : [30,50,100,120]
        :param org_list: Original list passed by the User
        :param numy: Number y passed by the User. Type is INT.
        :return: New list with filtered values ONLY.  
Solustion steps:
1. itarate the list and pick the Even index
2. From the Even index elements divisible by a number
3. Remove the duplicates
4. Add new list and retun the new list           
'''


# Function define filter the all the even numbers from the ODD indexes
def check_eve_ind(org_list,numy):

  #define new list
  new_list=[]
  #loop produce odd numbers from 1 to size of the original
  for i in range(0,len(org_list),2):    
    #checking for number is even
    if(org_list[i]%numy==0):
      #checking for number is not present in new list
      if(org_list[i] not in new_list):
        #addiing number to new list
        new_list.append(org_list[i])
  #finally reterns new list
  return new_list

# Execution
testorg_list=[10,20,30,40,50,60,100,11,12,13]
numy=10
#function calling
result=check_eve_ind(org_list=testorg_list,numy=numy)
#finally print result
print("Final Result is :: {} ".format(result))    


