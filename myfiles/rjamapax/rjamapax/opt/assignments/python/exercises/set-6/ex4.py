'''4. Write a function to take 2 lists and an integer X. Use zip function to iterate the list and pick values that
   are common at both indexes, they must be divisible by X. 
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
        :param org_list: Original list(list1,list2) passed by the User
        :param numX: Number X passed by the User. Type is INT.
        :return: New list with filtered values ONLY
        
Solution Steps:
1. Take two lists and iterate both list using zip
2. From the list pick the comman elelments in both lists
3. To check the condition filter values are divisilble 
4. Return the list     
        
                '''
#This function define comman values and divisible numbers                
def check_comman(org_list1,org_list2,numx):
    # define empty list
    new_mapper=[]
    #iterate the two lists in simantanously using zip
    for listA,listB in zip(org_list1,org_list2):
        #To check the condition value is same in both org_list1,org_list2
        if (listA==listB):
            # checking for condition comman number in lists divisible by numx
            if (listA%numx==0):
                # result is added to the new list
                new_mapper.append(listA)
    #finally return the new list            
    return new_mapper

# Execution
testListA=[100,20,300,40,50,60,100]
testListB=[1100,20,1300,40,50,160,1000]
numx=10
#function calling
result=check_comman(org_list1=testListA,org_list2=testListB,numx=numx)
#finally print result
print("Final Result is :: {} ".format(result))

