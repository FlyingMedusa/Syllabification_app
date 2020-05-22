
expression = ""


def ipa_key(elem, user_input):
    global expression
    expression = expression + str(elem)
    user_input.set(expression)