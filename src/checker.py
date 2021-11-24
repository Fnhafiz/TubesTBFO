import string

''' LINE '''
# Mengatasi kasus string
def string_checker(line):
    # Mengatasi kasus string menggunakan 1 petik
    is_apostrophe = False
    is_apostrophe_done = False
    first_apostrophe = 0
    second_apostrophe = 0
    i = 0
    while i < len(line):
        if is_apostrophe and line[i] == "'":
            if (line[i-1] != '\\'):
                second_apostrophe = i
                is_apostrophe_done = True
        elif line[i] == "'":
            first_apostrophe = i
            is_apostrophe = True
    
        if is_apostrophe and is_apostrophe_done:
            front_word = line[:first_apostrophe+1]
            back_word = line[second_apostrophe:]
            line = front_word + back_word

            is_apostrophe = False
            is_apostrophe_done = False

            i = first_apostrophe + 1
        
        i += 1
    
    # Mengatasi kasus string menggunakan 2 petik
    is_ditto = False
    is_ditto_done = False
    first_ditto = 0
    second_ditto = 0
    i = 0
    while i < len(line):
        if is_ditto and line[i] == '"':
            if (line[i-1] == '\\'):
                i += 1
                continue
            second_ditto = i
            is_ditto_done = True
        elif line[i] == '"':
            first_ditto = i
            is_ditto = True
    
        if is_ditto and is_ditto_done:
            front_word = line[:first_ditto+1]
            back_word = line[second_ditto:]
            line = front_word + back_word

            is_ditto = False
            is_ditto_done = False
            
            i = first_ditto + 1

        i += 1
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


# Cek number
def number_checker(num):
    number_string = string.digits
    number_list = list(number_string)

    is_number = True
    num_list = list(num)
    minus = "-"

    i = 0
    if ((num_list[i] in number_list) or (num_list[i] == minus)):
        i += 1   
    else :
        is_number = False
        return is_number

    while(i<len(num_list)):
        if (num_list[i] in number_list) :
            i += 1
        else :
            is_number = False
            break
    
    return is_number

# Cek Float
def float_checker(line):
    number_string = string.digits
    number_list = list(number_string)
    dot = '.'
    is_dot = False

    i = 0
    while (i<len(line)) :
        if (line[i] in number_list):
            j = i+1
            while (j<len(line)) and (not is_dot):
                if (line[j] in number_list):
                    j += 1
                elif (line[j] == dot):
                    front_num = line[:j]
                    back_num = line[j+1:]
                    line = front_num + back_num
                    is_dot = True
                    return line
                    break
                else :
                    break
            break
        elif (line[i] == dot):
            j = i+1
            if (line[j] in number_list):
                front_num = line[:i]
                back_num = line[j:]
                line = front_num + back_num
                return line
                break
            else : 
                i+=1
        else :
            i += 1
    
    return line

# Cek variabel
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

# Replace operator dengan 2 char menjadi 1 char
def replace_operator (line):
    line = line.replace(">=",">")
    line = line.replace("<=","<")
    line = line.replace("!=","<")
    line = line.replace("==","<")
    line = line.replace("**","*")
    line = line.replace("<>","<")
    line = line.replace("+=","+")
    line = line.replace("-=","-")
    line = line.replace("*=","*")
    line = line.replace("/=","/")
    line = line.replace("%=","/")
    line = line.replace("//=","/")
    line = line.replace("**=","*")
    line = line.replace("n","a")
    return line


''' LINES '''
# Mengatasi kasus comment multiple line
def multicomment_checker(lines):
    # Cek untuk comment dengan petik 1
    is_apostrophe = False
    is_apostrophe_done = False
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]):
            # Mengambil indeks ketika menemukan multiple line comment kedua
            if (lines[i][j] == "'") and (j < len(lines[i]) - 2) and is_apostrophe:
                if lines[i][j-1] == "\\":
                    j += 1 
                    continue
                if lines[i][j+1] == "'":
                    if lines[i][j+2] == "'":
                        second_apostrophe_i = i            
                        second_apostrophe_j = j
                        is_apostrophe_done = True
                        j += 2
            # Mengambil indeks ketika menemukan multiple line comment pertama
            elif (lines[i][j] == "'") and (j < len(lines[i]) - 2):
                if lines[i][j+1] == "'":
                    if lines[i][j+2] == "'":
                        first_apostrophe_i = i
                        first_apostrophe_j = j
                        is_apostrophe = True
                        j += 2
            # Apabila multiple line comment pertama dan kedua telah ditemukan
            if is_apostrophe and is_apostrophe_done:
                front_word = lines[first_apostrophe_i][:first_apostrophe_j]
                back_word = lines[second_apostrophe_i][second_apostrophe_j+3:]

                # Menghapus baris diantara kedua komen
                for k in range(first_apostrophe_i+1, second_apostrophe_i):
                    lines[k] = ""
                
                # Menangani per kasus
                if (first_apostrophe_i == second_apostrophe_i):         # dalam satu baris
                    lines[first_apostrophe_i] = front_word + back_word
                else:                                                   # tidak dalam satu baris
                    lines[first_apostrophe_i] = front_word
                    lines[second_apostrophe_i] = back_word
                
                is_apostrophe = False
                is_apostrophe_done = False

                j = first_apostrophe_j + 5
            
            j += 1

    # Cek untuk komen dengan petik 2
    is_ditto = False
    is_ditto_done = False
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]):
            # Mengambil indeks ketika menemukan multiple line comment kedua
            if (lines[i][j] == '"') and (j < len(lines[i]) - 2) and is_ditto:
                if lines[i][j-1] == '\\':
                    j += 1
                    continue
                if lines[i][j+1] == '"':
                    if lines[i][j+2] == '"':
                        second_ditto_i = i
                        second_ditto_j = j
                        is_ditto_done = True
                        j += 2
            # Mengambil indeks ketika menemukan multiple line comment pertama
            elif (lines[i][j] == '"') and (j < len(lines[i]) - 2):
                if lines[i][j+1] == '"':
                    if lines[i][j+2] == '"':
                        first_ditto_i = i
                        first_ditto_j = j
                        is_ditto = True
                        j += 2

            # Apabila multiple line comment pertama dan kedua telah ditemukan
            if is_ditto and is_ditto_done:
                front_word = lines[first_ditto_i][:first_ditto_j]
                back_word = lines[second_ditto_i][second_ditto_j+3:]

                # Menghapus baris diantara kedua komen
                for k in range(first_ditto_i+1, second_ditto_i):
                    lines[k] = ""

                # Menangani per kasus   
                if (first_ditto_i == second_ditto_i):               # dalam satu baris
                    lines[first_ditto_i] = front_word + back_word
                else:                                               # tidak dalam satu baris
                    lines[first_ditto_i] = front_word
                    lines[second_ditto_i] = back_word

                is_ditto = False
                is_ditto_done = False

                j = first_ditto_j + 5

            j += 1
    
    return lines

# Mengatasi kasus joining line
def joining_line_checker(lines):
    for i in range(len(lines)-1, -1, -1):
        j = 0
        while j < len(lines[i]):
            if (lines[i][j] == '\\'):
                front_word = lines[i][:j]
                back_word = lines[i+1].strip(" ")

                lines[i] = front_word + " " + back_word

                # # Kasus apabila spasi antara huruf lebih dari satu
                # if (front_word[j-1] == " "):
                #     lines[i] = front_word + back_word
                # else:
                #     lines[i] = front_word + " " + back_word
                lines[i+1] = ""
            j += 1

    return lines

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

'''Test Case Number Checker'''
'''
num  = "1234"
num2 = "-999"
num3 = "_102"
is_number = number_checker(num)
if (is_number == True):
    print("yes")
else :
    print("No")
'''

'''Test Case Float Checker'''
'''
line = "import var34A "
line_new = float_checker(line)
print(line_new)
'''

'''Test Case Replace Operator'''

'''
line  = "100>=10"
line2 = "if (j>=10) : "
line3 = "if (A**2) == (B**3) :"
line_new = replace_operator(line3)
print(line_new)
'''

