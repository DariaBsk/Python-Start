import model_math as model
import view


def button_click():
    type = view.get_type()
    operator = view.get_operator(type)
    value_a = view.get_value(type)
    value_b = view.get_value(type)
    model.init(value_a, value_b)
    match operator ###???
    case (-):  result = model.sub()
    case +: result = model.sum()
    case "*": result = model.mult()
    case "/": result = model.div()
    case "//": result = model.divv()
    case "%": result = model.mod()

    # result = model.do_it()
    view.view_data(result, "resul")