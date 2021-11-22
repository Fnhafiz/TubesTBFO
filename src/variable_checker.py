import string

def variable_checker(var):
    alphabet_string = string.ascii_letters
    alphabet_list = list(alphabet_string)
    digit_string = string.digits
    digit_list = list(digit_string)
    underscore = '_'

    is_variable = True
    var_list = list(var)
    
    i = 0
    if ((var_list[i] in alphabet_list) or (var_list[i] == underscore)):
        i += 1   
    else :
        is_variable = False
        return is_variable
    
    while (i<len(var_list)):
        if ((var_list[i] in alphabet_list) or (var_list[i] == underscore) or (var_list[i] in digit_list)):
            i += 1
        else :
            is_variable = False
            break
    
    return is_variable


'''Test Case Variable Checker'''

var  = "AKU_sayang_kAmU"
var2 = "_Halo"
var3 = "123Test"
var4 = "Hello_World_999"
var5 = "yuhuu+yes"
var6 = "-TBFO"

is_variable = variable_checker(var3)
if (is_variable == True):
    print("yes")
else :
    print("No")


