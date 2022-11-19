'''1. Write a function to take 2 lists and an integer numX.
   Use zip function to iterate the list.
   Pick values if 
           :they are common at both indexes AND 
           :they ARE be divisible by numX. 
   
   Duration for Dev & Execution: 10 minutes
   -----------------------------------------
   
   *** Note: You must iterate the lists only if the lengths of the lists are equal. *** 
   -------------------------------------------------------------------------------------
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : []
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[100,20,300,40,50,60,100]
        numX=20
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [100,20,300,40,50,60,100]
    Example :
        listA=[100,21,300,41,50,63,100]
        listB=[100,21,300,41,50,63,100]
        numX=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [100,300,50,100]

Solution Steps:
**************
Iterate the orginal lists Using zip function
    Check the comman elements in both indexes in listA and listB
    Check the comman value is divisible by numberX
        If yes:
            Add to new list
        else:
            continue the loop
    Finally return the new list
'''

# Define the function
def check_num(org_list1,org_list2,numx):
    # Define the empty list
    new_list=[]
    # Iterate the both list by using zip function
    for listA,listB in zip(org_list1,org_list2):
        #To check the condition value is same in both org_list1,org_list2
        if (listA==listB):
            # checking for condition comman number in lists divisible by numx
            if (listA%numx==0 and listB%numx==0):
                # result is added to the new list
                new_list.append(listA)
    # Finally return the new list            
    return new_list

# Execution
#calling function
#Testcase 1
result=check_num([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],10)
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_num([100,20,300,40,50,60,100],[100,20,300,40,50,60,100],20)
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_num([100,21,300,41,50,63,100],[100,21,300,41,50,63,100],10)
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_num([1,10,8,7,4,3,6,2,9,5],[32,12,8,23,27,3,62,32,21,5],5)
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_num([1000,800,300,500,700,100,600,400,900],[77,42,67,500,787,100,672,48,900],100)
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_num([21,34,57,87,54,32,23,29,55,80],[21,13,72,87,54,43,78,90,55,88],500)
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_num([90,100,98,93,95,91,96,92,97,99],[76,42,67,66,34,59,42,57,63,48],4)
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_num([1,100,300,800,50,39,75,67,894],[1,88,76,82,35,39,75,79,86],5)
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_num([25,45,65,75,95,105,25,15,85],[14,35,75,88,95,78,25,71,85],3)
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_num([121,22,456,2337,980,432,666,77,9],[34,75,78,64,980,463,777,72,48],143)
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#    
