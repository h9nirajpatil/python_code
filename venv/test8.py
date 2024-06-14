
age = int(input('Enter your age : '))
if  age>=0 and age<=12:
  c = 12 - age
  print("You should come after",c,("years"))
elif  age>=13 and age<=64:
  print("You are eligible. WE WELCOME YOU")
elif age>=65 and age<=100:
  d = age - 65
  print("You should come before",d,("years"))

