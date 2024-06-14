####################mamda############################

sq=lambda n:n**2
print("square is",sq(3))

#Write a lamda fuction to calculate the simple interest

SI=lambda P,R,T:(P*R*T/100)
print("Simple Interest",SI(100,2.1,3))

#create a normal fuction with two parameter as num1 and num2
#and calculate the sum,difference,product,quotient and remainder
#using lambda fuction...

def calculator(num1,num2):
    sum=lambda : num1+num2
    print("Sum is",sum())

    diff = lambda: num1 - num2
    print("Diff is", diff())

    prod = lambda: num1 * num2
    print("Prod is", prod())

    quot = lambda: num1 / num2
    print("Quot is", quot())

    rem = lambda: num1 % num2
    print("Rem is", rem())

calculator(20,10)


#filter--->is a function which allows you to filter values in list

mylist=[1,2,3,4,5,6,7,8,9,10]
even_list=list(filter(lambda n:n%2==0,mylist))
print(even_list)

#map()----> tp manipulate the values in the list
double_list=list(map(lambda n:n*2,mylist))
print(double_list)

#print the square of all the values in the list 
square_list=list(map(lambda n:n**2,mylist))
print(square_list)
















