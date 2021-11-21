RULE = {}


def read_rules ():
    lines = []
    global RULE
    with open('CNF_GABUNGAN.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.replace("->","")
        words = line.split(" ")
#        words = line.replace("->", "").split()
        print(words)
        if words[0] not in RULE:
            RULE[words[0]] = []
        RULE[words[0]].append(words[2:])

read_rules()
print(RULE)