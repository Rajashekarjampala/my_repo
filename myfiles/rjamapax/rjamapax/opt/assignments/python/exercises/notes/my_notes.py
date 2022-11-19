'''1. Write a program to print the ASCII value of a character.'''

x=input('enter a charecter: ')
print(ord(x))


'''2. Write a program that asks two people for their names; stores the names in variables called name1 and
name2; says hello to both of them'''

name1=input('enter a name:')
name2=input('enter a name:')
print('hello ',name1,name2)

'''3.Write a Python program which accepts the radius of a circle from the user and compute the area.'''

r=int(input('enter radius '))
x=3.14*r**2
print(x)


'''3. Write a Python program which accepts the user's first and last name and print them in reverse order
with a space between them..'''
name1=input('enter name: ')
name2=input('enter name: ')
print(name2,name1)


'''Write a Python program that will accept the base and height of a triangle and compute the area.
'''
height=int(input('enter height:'))
base=int(input('enter base:'))
x=0.5*height*base
print('area of triangle is:',x)


'''Write a Python program to solve (x + y) * (x + y). '''
x=int(input('enter number x: '))
y=int(input('enter number y: '))

a=(x + y) * (x + y)
print('final result:',a)


'''Write a python program to sum of the first n positive integers '''
n=int(input('enter number x: '))
sum=0
for i in range(1,n+1):
  sum+=i
print(sum)


'''Write a Python program to swap two variables. '''
a=10
b=20
a,b=b,a
print(b)


'''Write a program to enter two integers and then perform all arithmetic operations on them. '''
a=int(input('enter x: '))
b=int(input('enter y: '))

def check_val(x,y):
  sum=x+y
  return sum
  
print(check_val(a,b))


'''Write a program to perform string concatenation''' 
a='Raj is intelligent '
b='Rak is lover boy '

print(a+'and '+b)


'''Write a program to calculate simple interest.''' 
p=int(input('enter p:'))
t=int(input('enter t:'))
r=int(input('enter r:'))

i=(p*t*r)/100

print('i is :',i)

'''Write a program to calculate simple interest.''' 
p=int(input('enter principle:'))
t=int(input('enter time:'))
r=int(input('enter rate:'))

def simple_int(x,y,z):
  i=(x*y*z)/100
  return i

print('intrest', simple_int(p,t,r))


'''Write a program that prompts users to enter two integers x and y. The program then calculates and
display xy''' 
x=int(input('enter x:'))
y=int(input('enter y:'))

s=x**y
print('result: ',s)


'''Write a program that calculates numbers of seconds in a day.''' 
days=int(input('enter days '))
result=60*60*24*days
print(result)


'''Write a program that calculates numbers of seconds in a day.''' 
day=int(input('enter days '))
result=60*60*24*day
print(result)


'''Write a program to calculate salary of an employee given 
  his basic pay(to be entered by the user), HRA
  =10 percent of basic pay, TA=5 percent of basic pay. 
  Define HRA and TA as constants and use them to
  calculate the salary of the employee''' 

basic_pay=int(input('enter basic pay salary: '))

total_salary=(basic_pay)+(10/100*basic_pay)-(5/100*basic_pay)

print(total_salary)


'''Write a program to print the digit at one’s place of Number.
'''
x=12345
x%=10
print(x)


'''Write a program to calculate average of two numbers
'''
x=int(input('enter first number: '))
y=int(input('enter second number: '))

s=(x+y)/2

print('avarage: ',s)


'''Write a program to calculate area of triangle using Heron’s formula. ( Hint: Heron’s formula is :
area = sqrt(s*(s-a)*(s-b)*(s-c))'''

a=int(input('enter a : '))
b=int(input('enter b : '))
c=int(input('enter c : '))

s=a+b+c
area = ((s*(s-a)*(s-b)*(s-c)))**(1/2)

print('area of triangle: ',area)


'''Distance between two points'''
x1=int(input('enter x1: '))
x2=int(input('enter x2: '))
y1=int(input('enter y1: '))
y2=int(input('enter y2: '))

s=((x2-x1)**2)+((y2-y1)**2)

print('result: ',s)









