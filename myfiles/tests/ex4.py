'''
   Write a function to calculate the student's grade based on marks obtained in various subjects.
   There are 4 subjects Maths, Physics, Chemistry, CSE
   You need to find the sum of all of the marks obtained above and calcuate grade.
   Here's the table to calculcate the grade
   Note: 
       1. You must use **kwargs
       2. If the input score is >100 for any subject you must raise exception since max allowed score is 100 ONLY
       3. If the input score is non-integer, you must raise exception since scores can be in integers ONLY
   ----------------------------
       Total       Grade
       ------      ------
        400         A+
        350-400     A
        300-350     B+
        250-300     B
        200-250     C
        150-200     E
        <150        F
        
'''
#define Function with **kwargs
def check(**Subject_marks):
    #define sum variable
    sum=0
    #iterates values using **kwargs
    for marks in Subject_marks.values():
        #checking whether the value is non-integer type
        if(type(marks)==str):
            return ('Scores can be in integers only')
        #checking whether marks greater than 100
        elif(marks>100):
            return ('Max allowed score is 100 ONLY')
        else:
            #adding marks to sum
            sum=sum+marks
    #checking whether the sum equals to 400
    if(sum==400):
        return ('A+')
    #checking whether the sum less than 400 and greater than or equals to 350
    elif(sum>=350 and sum<400):
        return ('A')
    #checking whether the sum less than 350 and grater than or equals to 300
    elif(sum>=300 and sum<350):
        return('B+')
    #checking whether the sum less than 300 and greater than or equals to 250
    elif(sum>=250 and sum<300):
        return('B')  
    #checking whether the sum less than 250 and greater than equal t0 200 
    elif(sum>=200 and sum<250):
        return('C') 
    #checking whether the sum less than 200 and grater than or equals to 150
    elif(sum>=150 and sum <200):
        return('E')
    #checking whether the sum less than 150
    elif(sum<150):
        return('F')  

#Calling function
result=check(maths=100,physics=100,chemistry=100,cse=100)
print(result)