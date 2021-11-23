def replace_operator (line):
    line = line.replace(">=",">")
    line = line.replace("<=","<")
    line = line.replace("==","=")
    line = line.replace("**","*")
    return line

'''Test Case Replace Operator'''

'''
line  = "100>=10"
line2 = "if (j>=10) : "
line3 = "if (A**2) == (B**3) :"
line_new = replace_operator(line3)
print(line_new)
'''