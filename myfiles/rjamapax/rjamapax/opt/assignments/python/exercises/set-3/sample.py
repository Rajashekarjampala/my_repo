def funcDict(orgDict,numX,numY):
  newMapper={}
  totSum=numX + numY
  for _key,_val in orgDict.items():
    if (_key*_val)>(totSum):
        newMapper[_key]=_val
  return newMapper

# Execution
testDict={1:2,3:4,5:6,7:8,9:10}
numX=20
numY=25
result=funcDict(orgDict=testDict,numX=numX,numY=numY)
print("Final Result is :: {} ".format(result))
-----------------------------------------------------
def funcDict(orgDict,numX,numY):
  '''
    If the prod of (dict key * dict val) is > sum of number (X+Y), 
    then add it to new dict. Finally iterate and return the new dict.
    Example : 
      testDict={1:4,10:2,3:4,4:7,6:11,12:9}
      numX=20
      numY=30
      result=func_exec(testDict,numX,numY)
      print(result)
      Expected Output : {6:11,12:9}}
  :param orgDict: Original dictionary passed by the User
  :param numX: Number X passed by the User. Type is INT.
  :param numY: Number Y passed by the User. Type is INT.
  :return: New dictionary with filtered values ONLY.
  '''
  # Define an empty new mapper
  newMapper={}
  # Sum of numX & numY
  totSum=numX + numY
  # Iterate the original dictionary and filter the values
  for _key,_val in orgDict.items():
    if (_key*_val)>(totSum):
        # IF the condition is satisfied, add the key & value to the new dictionary
        newMapper[_key]=_val
  # Finally return the new dictionary
  return newMapper

# Execution
testDict={1:2,3:4,5:6,7:8,9:10}
numX=20
numY=25
result=funcDict(orgDict=testDict,numX=numX,numY=numY)
print("Final Result is :: {} ".format(result))