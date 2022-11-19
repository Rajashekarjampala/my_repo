'''
Write a function to take 2 lists and integers numX,numY .
    From the listA find all elements that are >er sum(numX+numY). Append those elements to listB.
    Remove all duplicates from listB.
    Finally sort and return listB.
   -------------------------------------------------------------------------------------
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=100
        numY=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [20,40,50,160,300,1000,1100,1300]
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=10
        numY=10
        result=func_exec(listA,listB)
        print(result)
        Expected Output : [20,40,50,60,100,160,300,1100,1300]
    Example :
        listA=[100,20,300,40,50,60,100]
        listB=[1100,20,1300,40,50,160,1000]
        numX=300
        numY=100
        result=func_exec(listA,listB)
        print(result)
        Expected Output : []
'''
# define function
def check_num(listA,listB,numx,numy):
    # Iterate the list
    for i in listA:
        # check listA all elements that are >er sum(numX+numY)
        if (i>(numx+numy)):
            # Remove duplicate from listB
            if (i not in listB):

                # Add to the listB
                listB.append(i)            
    # Finally return listB
    return sorted(listB)

print(check_num([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],100,10))  
print(check_num([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],10,10))
print(check_num([100,20,300,40,50,60,100],[1100,20,1300,40,50,160,1000],300,100))              