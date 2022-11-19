'''
Write a function to take a number numX, numY followed by any number of integer arguments.
    You need to find all numbers divisible by numX and numY
    Filter all the numbers from the list that are divisible numX and numY and add to new list.
    Finally return the new list.
    Note: You must use *args in your function implementation
    *********************************************************
    Example :
        numX=20
        numY=10
        result=func_exec(numX,20,40,50,60,80,90,100,70)
        print(result)
        Expected Output : [20,40,60,80,100]
    Example :
        numX=25
        numY=5        
        result=func_exec(numX,50,60,80,90,100,70)
        print(result)
        Expected Output : [50,100]
    Example :
        numX=7
        numY=12        
        result=func_exec(numX,20,40,50,70)
        print(result)
        Expected Output : []
'''
# Define function
def check_num(numx,numy,*numbers):
    # Define new list
    new_list=[]
    # Iterate the numbers 
    for i in numbers:
        # Check numbers are divisible by numx and numy
        if (i%numx==0 and i%numy==0):
            # Add to new list
            new_list.append(i)
    # Finally return new listS        
    return new_list

print(check_num(20,10,20,40,50,60,80,90,100,70))            