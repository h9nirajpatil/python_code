#decorators--->to add new funtionality to the exiting fuction
#rule1=always have parameter in the fuctions
#rule2=use nested fuction and add the new functionally in it
#
# def myfunc(func):
#     def inner():
#         print("Python")
#         return  func()
#     return inner
#
# @myfunc
# def function1():
#     print('Hello')
# function1()


def mydiv(func):
    def inner(n1,n2):
        if(n1<n2):
            n1,n2=n2,n1
        return func(n1,n2)
    return inner
@mydiv
def division(n1,n2):
    print(n1/n2)
division(2,4)