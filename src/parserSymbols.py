# Symbol yang ingin dipisah
symbols = ['(', ')', ',', ':']

# Testcase string
test = "Aku sedang(akmal,23123,dasd):"
listTest = test.split(" ")

# Proses pemisahan
i = 0
while(i < len(listTest)):
    j = 0
    listWord = list(listTest[i])        # diubah jadi list agar bisa diiterasi

    while(j < len(listWord)):           # iterasi per huruf
        char = listWord[j]
        if char in symbols:             # apabila char berupa simbol
            frontWord = "".join(listWord[:j])
            backWord = "".join(listWord[j+1:])

            # Diatur per case
            if(j == 0 and j+1 == len(listWord)):
                listTest[i] = char
            elif(j == 0):
                listTest[i] = char
                listTest.insert(i+1, backWord)
            elif(j+1 == len(listWord)):
                listTest[i] = frontWord
                listTest.insert(i+1, char)
            else:
                listTest[i] = frontWord
                listTest.insert(i+1, char)
                listTest.insert(i+2, backWord)
            break
        j = j + 1
    i = i + 1

# output
print(listTest)
for i in listTest:
    print(i)
