Name=input("Enter you name:")
Marks=int(input("Enter you marks:"))
if(Marks<0 or Marks>100):
    print("INVALID MARKS")
else:

  if(Marks>=90 and Marks<=100):
    print('GRADE A')
  elif(Marks>=80 and Marks<=89):
    print('GRADE B')    
  elif(Marks>=70 and Marks<=79):
    print('GRADE C')  
  elif(Marks>=60 and Marks<=69):
    print('GRADE D')        
  elif(Marks>=0 and Marks<=59):
    print('GRADE F')  
if(Marks>=60):
    print("RESULT:PASS")
else:
    print("RESULT:FAIL")    
