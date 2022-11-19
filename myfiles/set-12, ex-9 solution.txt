'''Write a function to calculate the employee hike based on appraisal rating.
   
   Note: 
       1. You must use **kwargs
       2. If the rating score is >100 for any employee you must raise exception since max allowed score is 100 ONLY
       3. If the input score is non-integer, you must raise exception since scores can be in integers ONLY
       4. Formula for new salary calculation:
           new_salary= ((hike/100)*old_salary)+old_salary
           Example:
           ---------
               curr_salary=100000
               hike=30
               new_salary=((30/100)*100000)+100000
               new_salary=130000
               curr_salary=50000
               hike=10
               new_salary=((10/100)*50000)+50000
               new_salary=55000
   ----------------------------------------------------------------------------------------------------------------
   Here's the table to calculcate the hike
       Total       Hike%
       ------      ------
        100         30
        90-100      24
        80-90       17
        70-80       12
        60-70       8
        50-60       4
        <50         1
    Example :
        result=func_exec(rating=100,curr_salary=100000)
        print(result)
        Expected Output : {"hike":"30","new_salary":"130000"}
    Example :
        result=func_exec(rating=49,curr_salary=100000)
        print(result)
        Expected Output : {"hike":"1","new_salary":"101000"}
    Example :
        result=func_exec(rating=200,curr_salary=50000)
        print(result)
        Expected Output : Raise Exception since rating score is 200, max allowed rating score is 100 ONLY
    Example :
        result=func_exec(rating="100",curr_salary=50000)
        print(result)
        Expected Output : Raise Exception since rating score is a string "100", rating scores can be integers ONLY
'''
def check_hike(**appr):
  
  rate=appr['rating']
  salary=appr['curr_salary']
  
  if (type(rate)==str or type(salary)==str):
    return ("Scores can be in integers Only")
  elif (rate>100):
    return ("Max allowed score is 100 Only")
  elif (rate==100):
    return 'hike:{},new_salary:{}'.format(rate,salary+(salary*30/100))
  elif (rate>=90 and rate<100):
    return 'hike:{},new_salary:{}'.format(rate,salary+(salary*24/100))
  elif (rate>=80 and rate<90):
    return 'hike:{},new_salary:{}'.format(rate,salary+(salary*17/100))  
  elif (rate>=70 and rate<80):
    return 'hike:{},new_salary:{}'.format(rate,salary+(salary*12/100))
  elif (rate>=60 and rate<70):
    return 'hike:{},new_salary:{}'.format(rate,salary+(salary*8/100))
  elif (rate>=50 and rate<60):
    return 'hike:{},new_salary:{}'.format(rate,salary+(salary*4/100)) 
  elif (rate<50):
    return 'hike:{},new_salary:{}'.format(rate,salary+(salary*1/100))

print(check_hike(rating=100,curr_salary=100000))
print(check_hike(rating=49,curr_salary=100000))
print(check_hike(rating=200,curr_salary=50000))
print(check_hike(rating='200',curr_salary=50000))


  



