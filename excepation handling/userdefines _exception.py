# class MarksOutofRange(Exception):
#     pass
#
# class Student:
#
#     def validateMarks(self,marks):
#         if(marks>100):
#             raise  MarksOutofRange("Invalid marks")
#
#         else:
#             print("valid marks")
#
# s=Student()
#
# try:
#     s.validateMarks(190)
# except MarksOutofRange as e:
#     print(e)



#create a ageexception

class AgeAboveBelow(Exception):
    pass

class Age:
    def validAge(self):
        age = int(input("Enter The Age:"))
        if(age<18):
            raise AgeAboveBelow("Inavlid Age For Votting")
        else:
            print("Valid Age For Votting YOu Can Vote Now")

a=Age()
try:
    a.validAge()
except AgeAboveBelow as e:
    print(e)


