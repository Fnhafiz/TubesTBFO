def string_checker(line):
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