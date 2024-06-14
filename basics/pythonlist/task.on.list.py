name=input("Enter your name:-")
age=int(input("Enter your age:-"))
gender=input("Enter your gender:-")

personaldetails=[name,age,gender]
print("personaldetails=",personaldetails)

email=input("Enter your email:-")
ContactNo=int(input("Enter your contactno."))
Address=input("Enter your address:-")

contactdetails=[email,ContactNo,Address]
print("contactdetails=",contactdetails)

persondetails=personaldetails+contactdetails
print("PersonDetails:-",persondetails)



