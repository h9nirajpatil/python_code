
class Book:

    book=''
    publisher=''
    author=''

    def __init__(self,book,publisher,author):
        self.book = book
        self.publisher = publisher
        self.author = author

    def display(self):
        print("**************** Book Details   ***************")
        print("\ttitle:",self.book,"\n","Publisher name:",self.publisher,"\n","Author name:",self.author)
        print("________________________________________________")


limit=int(input("Enter no of object you want:-"))
list=[]

for i in range(0,limit):
    t= input("Enter  the  title:-")
    p=input("Enter publisher:-")
    a=input("Enter the author:-")
    obj=Book(t,p,a)
    list.append(obj)

for i in list:
    i.display()




