def rules_parser(filename):
    RULE = {}
    lines = []
    with open(filename) as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.replace("->", "")
        words = line.split(" ")
#        words = line.replace("->", "").split()
        # print(words)
        if words[0] not in RULE:
            RULE[words[0]] = []
        RULE[words[0]].append(words[2:])
    return RULE


''' TEST CASE'''
# rule = read_rules()

# for k, v in rule.items():
#     print(k, v)
