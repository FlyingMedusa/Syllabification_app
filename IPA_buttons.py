import IPA_classes as ipa_c

expression = ""

def ipa_key(elem, user_input):
    global expression
    expression = expression + str(elem)
    user_input.set(expression)

def done_key(user_input):
    try:
        global expression
        result = "wait a bit! IN PROGRESS"
        user_input.set(result)
        expression = ""
    except:
        user_input.set(" error ")
        expression = ""