'''
    Write a function to calculate the employee hike based on appraisal rating.
   
    Note: 
       1. You must use **kwargs
       2. If the rating score is >100 for any employee you must raise exception since max allowed score is 100 ONLY
       3. If the input score is non-integer, you must raise exception since scores can be in integers ONLY
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
        Expected Output : {"hike":"30","new_dic_salary":"130000"}
    Example :
        result=func_exec(rating=49,curr_salary=100000)
        print(result)
        Expected Output : {"hike":"1","new_dic_salary":"101000"}
    Example :
        result=func_exec(rating=200,curr_salary=50000)
        print(result)
        Expected Output : Raise Exception since rating score is 200, max allowed rating score is 100 ONLY
    Example :
        result=func_exec(rating="100",curr_salary=50000)
        print(result)
        Expected Output : Raise Exception since rating score is a string "100", rating scores can be integers ONLY
'''
#define a function with arguments **kwargs
def check(**appraisal_rating):
    #define new_dic dict
    new_dic={}
    #iterates argumnts using **kwargs
    for key,value in appraisal_rating.items():
      #adding key and  values to new_dic dict
      new_dic[key]=value
    #assigined rate from new_dic dict
    rate=new_dic['rating']
    #assigned salary from new_dic dict
    salary=new_dic['cur_salary']
    #checking whether the rate is NON-integer type
    if(type(rate)==str):
            return ('Scores can be in integers only')
    #checking whether the rate is greater than 100
    elif(rate>100):
      return 'Max allowed score is 100 ONLY'
    #checking whetehr tht rate is 100
    elif(rate==100):
    #reurn new_dic salary with extra 30%
      return 'hike:{},new_dic_salary:{}'.format(rate,salary+(salary*30/100))
    #checking whether the rate is less than 100 and greater than or equal to 90
    elif(rate<100 and rate>=90):
      #return new_dic salary with extra 24%
      return 'hike:{},new_dic_salary:{}'.format(rate,salary+(salary*24/100))
    #checking whether the rate is less than 90 and greater than or equals to 80
    elif(rate<90 and rate>=80):
      #return new_dic salary with extra 17%
      return 'hike:{},new_dic_salary:{}'.format(rate,salary+(salary*17/100))
    #checking whether the rate less than 80 and greater than or equals to 70
    elif(rate<80 and rate>=70):
      #return new_dic salary with extra 12%
      return 'hike:{},new_dic_salary:{}'.format(rate,salary+(salary*12/100))
    #checking whether the rate less than 70 and greater than or equals to 60
    elif(rate<70 and rate>=60):
      #return new_dic salary with extra 8%
      return 'hike:{},new_dic_salary:{}'.format(rate,salary+(salary*8/100))
    #checking whether the rate is less than 60 and greaater than or equals to 50
    elif(rate<60 and rate>=50):
      #return new_dic salary with extra 4%
      return 'hike:{},new_dic_salary:{}'.format(rate,salary+(salary*4/100))
    #checking whether the rate is less than 50
    elif(rate<50):
        #return new_dic salary with extra 1%
      return 'hike:{},new_dic_salary:{}'.format(rate,salary+(salary*1/100))

#Calling Function       
result=check(rating=100,cur_salary=100000)
print(result)

result=check(rating=49,cur_salary=100000)
print(result)

result=check(rating=200,cur_salary=50000)
print(result)

result=check(rating='100',cur_salary=100000)
print(result)