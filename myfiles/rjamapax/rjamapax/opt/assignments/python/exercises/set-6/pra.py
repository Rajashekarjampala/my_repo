
'''
1. Write a function to take a list. Filter all the even numbers from the ODD indexes. Remove duplicates.

    Example :        listA=[10,20,30,40,50,60,100,11,12,13]        result=func_exec(listA)        print(result)        Expected Output : [20,40,60]

    Example :        listA=[10,21,30,41,50,50,100,11,12,13]        result=func_exec(listA)        print(result)        Expected Output : [50]

  :param listA: List passed by the User  :return: Even Elements from ODD indexes without    duplicates

Solution Steps :
----------------

1. From the list, filter all elements from the ODD index and save it in listODDIndexes array.
2. Iterate listODDIndexes array and filter all even elements and append to new array listEven.
3. Remove duplicates from array listEven.
4. Return listEven.
'''


