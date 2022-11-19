# Question on List Extend
listA=[1,2,3,4]
listB=[4,5,6,7]
listA.extend(listB)
print(listA)

# Question on List append
listA=[1,2,3,4]
listB=[4,5,6,7]
listA.append(listB)
print(listA)

# Question on List append
listA=[1,2,3,4]
listB=[4,5,6,7]
listC=[10,20,30]
listA.extend(listB)
listA.append(listC)
print(listA)

# Q4: Question on List sorting
listA=[1,2,6,7,3,4]
print(sorted(listA))

# Q6: Question on List indexing
listA=[1,2,6,7,3,4]
index=2
listA.insert(2,100)
print(listA)

# Q7: Question on List indexing
listA=[1,2,6,7,3,4]
print(listA[2])
print(listA[-2])
print(listA[3])
print(listA[-1])
print(listA[0])

# Q8: Question on List indexing
listA=[1,2,6,7,3,4]
listB=[14,15,16,17]
listA.extend(listB)
listA.insert(2,100)
print(listA)

# Q9: Question on List indexing
listA=[1,2,6,7,3,4]
listB=[14,15,16,17]
listA.extend(listB)
listA.insert(2,100)
listA.append(listA[3] + listA[-1])
print(listA)

# Q10: Question on List indexing
listA=[1,2,6,7,3,4]
listB=[14,15,16,17]
listA.append(listA[3] + listA[-1])
listA.append(listA[3] + listA[2])
listA.extend(listB)
print(listA)

# Q11: Question on removing item from List 
listA=[1,2,6,7,3,4]
listB=[14,15,16,17,4]
listA.append(listA[3] + listA[-1])
listA.append(listA[3] + listA[2])
listA.extend(listB)
listA.remove(4)
print(listA)

# Q12: Question on removing item from List
listA=[1,2,6,7,3,4]
listB=[14,15,16,17,4]
listA.append(listA[3] + listA[-1])
listA.append(listA[3] + listA[2])
listA.extend(listB)
listA.remove(4)
listA.remove(4)
listA.remove(17)
print(listA)

# Q13: Question on removing item from List
listA=[1,2,6,7,3,4]
listB=[14,15,16,17,4]
listA.append(listA[3] + listA[-1])
listA.append(listA[3] + listA[2])
listA.extend(listB)
listA.remove(40)
print(listA)

# Q14: Question on removing item from List
listA=[1,2,6,7,3,4]
listB=[14,15,16,17,4]
listA.append(listA[3] + listA[-1])
listA.append(listA[3] + listA[2])
listA.extend(listB)#[1,2,6,7,3,4,11,13,14,15,16,17,4]
print(listA[-20])

'''
1. Write a function to take 2 lists and an integer numX.
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
'''        


'''
2. Write a function to take a list argument. Find the element that has greatest length.

	Example :
		listA=["hello","world","science","maths","Python"]
		result=func_exec(listA)
		print(result)
		Expected Output : ["science"]
		Reason: length of science -> 7

	Example :
		listA=["hello","world","science","maths","Pythonics"]
		result=func_exec(listA)
		print(result)
		Expected Output : ["Pythonics"]
		Reason: length of Pythonics -> 9    
'''            