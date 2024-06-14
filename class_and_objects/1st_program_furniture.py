class Furniture:

    dimension="200X200"
    color="brown"

    #self is aparameter which points to the same class variables
    #and allow you o accesses them inside the function

    def display(self):
        print(self.dimension," ",self.color)

table=Furniture()   #creates object of furniture class
table.display()