'''4. Write a function to take a list, number X,Y,Z as arguments.
 From the list pick the elements that are <er than (X+Y+Z). Add those elements to new list. Finally return the new list.
    Example : 
        org_list=[1,2,300,4,5,6,7,8,9,100,11,120,200,400]
        numX=10
        numy=20
        numZ=25
        result=func_exec(org_list,numX,numY,numZ)
        print(result)
        Expected Output : [1,2,4,5,6,7,8,9,11]
        :param org_list: Original list passed by the User
        :param numX: Number X passed by the User. Type is INT.
        :param numY: Number Y passed by the User. Type is INT.
        :param numY: Number Z passed by the User. Type is INT
        :return: New list with filtered values ONLY'''

# This function is define From the list pick the elements that are <er than (X+Y+Z)
def pick_less(org_list,numx,numy,numz):

    # #define an empty new list
    new_mapper=[] 
    # itarate the list
    for i in org_list:
        # checking condition list of the elements lessthen sum of numx+numy+numz
        if (i<(numx+numy+numz)): 
            # elements add to new list
            new_mapper.append(i) 
    # finally returns a new list
    return new_mapper  

# Execution
test_list=[1,2,300,4,5,6,7,8,9,100,11,120,200,400]
numx=10
numy=20
numz=25
result=pick_less(org_list=test_list,numx=numx,numy=numy,numz=numz)
print("Final Result is :: {} ".format(result))              