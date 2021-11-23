import string

# Mengatasi kasus string
def string_checker(line):
    # Mengatasi kasus string menggunakan 1 petik
    is_apostrophe = False
    for i in range(len(line)):
        if is_apostrophe and line[i] == "'":
            if (line[i-1] == '\\'):
                continue
            second_apostrophe = i
        elif line[i] == "'":
            first_apostrophe = i
            is_apostrophe = True
    
    if is_apostrophe:
        front_word = line[:first_apostrophe+1]
        back_word = line[second_apostrophe:]
        line = front_word + back_word
    
    # Mengatasi kasus string menggunakan 2 petik
    is_ditto = False
    for i in range(len(line)):
        if is_ditto and line[i] == '"':
            if (line[i-1] == '\\'):
                continue
            second_ditto = i
        elif line[i] == '"':
            first_ditto = i
            is_ditto = True
    
    if is_ditto:
        front_word = line[:first_ditto+1]
        back_word = line[second_ditto:]
        line = front_word + back_word
    
    return line

# Mengatasi kasus comment
def comment_checker(line):
    is_comment = False

    i = 0
    while i < len(line) and not is_comment:
        if line[i] == '#':
            first_comment = i
            is_comment = True
        else:
            i += 1
    
    if is_comment:
        front_word = line[:first_comment]
        line = front_word
    
    return line

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

def replace_operator (line):
    line = line.replace(">=",">")
    line = line.replace("<=","<")
    line = line.replace("==","=")
    line = line.replace("**","*")
    return line


'''Test Case Variable Checker'''

'''
var  = "AKU_sayang_kAmU"
var2 = "_Halo"
var3 = "123Test"
var4 = "Hello_World_999"
var5 = "yuhuu+yes"
var6 = "-TBFO"
var7 = "akmal[akmal"

is_variable = variable_checker(var7)
if (is_variable == True):
    print("yes")
else :
    print("No")
'''

'''Test Case Replace Operator'''

'''
line  = "100>=10"
line2 = "if (j>=10) : "
line3 = "if (A**2) == (B**3) :"
line_new = replace_operator(line3)
print(line_new)
'''
