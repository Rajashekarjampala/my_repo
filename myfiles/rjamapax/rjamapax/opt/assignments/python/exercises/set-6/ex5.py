'''5. Write a function to take a dict and number X as argument. 
Find the key,value pairs that are both divisible by number X
    Example : 
            testDict={10:20, 3:30, 4:40,90:100,20:30}
            numX=10
            result=func_exec(testDict,numX)
            print(result)
            Expected Output : {10:20,90:100,20:30}
            :param org_dic: Original dictionary passed by the User
            :param numX: Number X passed by the User. Type is INT.
            :return: New dic with filtered values ONLY
            
Solution Steps:
1. From the dictionary to Iterate the keys and values
2. To check the condition for items divisible by numberX
3. Return the new dictionary.'''  

# This function is defines the key and value (item) divisible by a num            
def check_div(org_dic,numx):
  # define new empty dictionary
  new_dic={}
  # iterate the key,and value from the orginal dictionary
  for _key,_value in org_dic.items():
    # To check the condition if key and value divisible by numberx
    if (_key%numx==0 and _value%numx==0):
      # Update to the new ditionary
      new_dic[_key]=_value
  # finally return the new dictionary
  return new_dic

# Execution
testDict={10:20, 3:30, 4:40,90:100,20:30}
numx=10
#function calling
result=check_div(org_dic=testDict,numx=numx)
#finally print the result
print("Final Result is :: {} ".format(result))           
