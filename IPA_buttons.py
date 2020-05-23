import IPA_classes as ipa_c

expression = ""

def ipa_key(elem, user_input):
    global expression
    expression = expression + str(elem)
    user_input.set(expression)

def done_key(user_input):
    try:
        global expression
        result = ipa_c.sounds_to_obj(expression)
        user_input.set(result)
        expression = ""
    except:
        user_input.set(" error ")
        expression = ""

def clear_key(user_input):
    global expression
    user_input.set("")
    expression = ""