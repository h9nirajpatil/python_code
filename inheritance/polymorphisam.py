class Fruit:

    def eat(self,taste):
        print("Eatting Fruits",taste)

class Apple(Fruit):

    def eat(self,color):
        super().eat("sweet")
        print("eatting apple",color)

obj=Apple()
obj.eat("red")