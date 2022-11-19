'''
Write a function to take a list argument. Find the element that has greatest length.
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

        :param org_list: Original list passed by the User
        :return: New list with filtered values ONLY.  

    Solution Steps:  
    **************
    Take original list and iterate
        Store sizes of words in a list 
        checking if the word size is greater than remaining words
        if yes:
            add to new list
        else:
            continue loop
	Finally return the greater length lenth of list					
'''
# Define function
def check_word(org_list):
	# Maximun length is start from 0 
    max_len=0
	# Iterate the original list
    for i in org_list:
		# Check condition for length of the list is greater than 0
        if (len(i)>max_len):
			# max length of element from the list
            max_len=len(i)
			# result is Assign to variable 
            gre_len=i
	# Finally return the greatest length word from list			
    return gre_len        
            
#calling function  
#Testcase 1
result=check_word(["hello","world","science","maths","Python"])
print("\n")
print('Testcase 1 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 2
result=check_word(["hello","world","science","maths","Pythonics"])
print("\n")
print('Testcase 2 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 3
result=check_word(["hello","world","today","comming"])
print("\n")
print('Testcase 3 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 4
result=check_word(["prashanth","shekar","sravan","goutham","prasad","sraavi"])
print("\n")
print('Testcase 4 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#Testcase 5
result=check_word(["airtel","vodafone","idea","jio","bsnl","mahesh"])
print("\n")
print('Testcase 5 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
#TestCase 6
result=check_word(["india","srilanka","america","south africa","afganisthan"])
print("\n")
print('Testcase 6 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 7
result=check_word(["cat","dog","elephant","fox","rabbit"])
print("\n")
print('Testcase 7 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 8
result=check_word(["hyderabad","miyapur","kukatpally_vvnagr","sangareddy","patancheru"])
print("\n")
print('Testcase 8 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 9
result=check_word(["mobile","laptop","redmi","realme","vivo","nokiamobile"])
print("\n")
print('Testcase 9 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
# TestCase 10
result=check_word(["book","pen","pencile","niddle","writtingstory"])
print("\n")
print('Testcase 10 Output : {}'.format(result))
print("\n")
print("-"*50)
print("\n")
# ------------------------------------------------------------------#
        
