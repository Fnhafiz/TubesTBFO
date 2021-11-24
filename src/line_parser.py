# Proses pemisahan
def symbols_parser(line, symbols):
    line = ' '.join(line.split())
    list_line = line.split(" ")
    i = 0
    while(i < len(list_line)):
        j = 0
        # diubah jadi list agar bisa diiterasi
        list_word = list(list_line[i])

        while(j < len(list_word)):           # iterasi per huruf
            char = list_word[j]
            if char in symbols:             # apabila char berupa simbol
                front_word = "".join(list_word[:j])
                back_word = "".join(list_word[j+1:])

                # Diatur per case
                if(j == 0 and j+1 == len(list_word)):
                    list_line[i] = char
                elif(j == 0):
                    list_line[i] = char
                    list_line.insert(i+1, back_word)
                elif(j+1 == len(list_word)):
                    list_line[i] = front_word
                    list_line.insert(i+1, char)
                else:
                    list_line[i] = front_word
                    list_line.insert(i+1, char)
                    list_line.insert(i+2, back_word)
                break
            j = j + 1
        i = i + 1
    return list_line


''' TEST CASE '''
# # Symbol yang ingin dipisah
# symbol = ['(', ')', ',', ':']

# # Testcase string
# test = "Aku sedang(akmal,23123,dasd):"


# list_line = symbols_parser(test, symbol)
# # output
# print(list_line)
# for i in list_line:
#     print(i)
