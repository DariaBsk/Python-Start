# def view_data(data, title):
#     print(f'{title} = {data}')
# От Артём Микулик всем 08:23 PM
# x = 0
# y = 0
#
# def init(a, b):
#     global x
#     global y
#     x = a
#     y = b
#
# def do_it():
#     return x * y
#
# def get_complex_value():
#     return complex(input("Enter a value: "))
#
# a = get_complex_value()
# print(type(a))
#
# a=complex('1+2j')
# print(a)
##
def view_data(data, title):
    print(f'{title} = {data}')

def get_value(type):
    if type:
        return int(input('int = '))
    else:
        return complex(input("Enter a complex: "))


def get_type():
    return int(input("type - ? 0 - complex, 1 - integer "))

def get_operator(type):
    if type:
        return input("operator - ? * , + , - , / , // , %")
    else:
        return input("operator - ? * , + , -, /  ")


    ####
x = 0
y = 0

def init(a, b):
    global x, y
    x = a
    y = b

def mult():
    return x * y

def add():
    return x + y

def sub():
    return x - y

def div():
    return x / y

def mod():
    return x % y

def divv():
    return x // y

###
import model_math as model
import view


def button_click():
    type = view.get_type()
    operator = view.get_operator(type)
    value_a = view.get_value(type)
    value_b = view.get_value(type)
    model.init(value_a, value_b)
    match operator:
        case "-":
            result = model.sub()
        case "+":
            result = model.sum()
        case "*":
            result = model.mult()
        case "/":
            result = model.div()
        case "//":
            result = model.divv()
        case "%":
            result = model.mod()

    """result = model.do_it()"""
    view.view_data(result, "resul")
#####
От Артём Микулик всем 09:22 PM
import  model_math as model
x = 0
y = 0

def init(a, b):
    global x, y
    x = a
import controller as c
def view_data(data, title):
    print(f'{title} = {data}')

def get_value(type):
    if type:
        return int(input('int = '))
    else:
        return complex(input("Enter a complex: "))


def get_type():
    return int(input("type - ? 0 - complex, 1 - integer "))

def get_operator(type):
    if type:
        return input("operator - ? * , + , - , / , // , % ")
    else:
        return input("operator - ? * , + , -, /  ")
