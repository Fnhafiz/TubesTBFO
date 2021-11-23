from rules_parser import rules_parser
from symbols_parser import symbols_parser
from cyk_algorithm import cyk_algorithm
from cykalg import cykParse
from replace_operator import replace_operator

import sys

symbols = ['(', ')', '[', ']', '{', '}',
           ',', ':', '\'', '"',
           '+','-','*','/','%','@',
           '<', '>', '=']

filename = sys.argv[1]
lines = []
with open(filename) as file:
    lines = file.readlines()

formatted_lines = []
for i in range(len(lines)):
    temp = symbols_parser(lines[i], symbols)
    formatted_lines.append(temp)

rules = rules_parser('CNF_GABUNGAN.txt')

isCorrect = True
i = 0
while isCorrect and i < len(formatted_lines):
    line = formatted_lines[i]
    if (line[0] == ''):
        i += 1
        continue
    elif (not cykParse(line, rules)):
        isCorrect = False
    else:
        i += 1

if (isCorrect):
    print("Accepted")
else:
    print("Syntax Error")
    errorLine = "".join(lines[i])
    errorLine = errorLine.strip("\n")
    print(f'Terjadi kesalahan ekspresi pada line {i+1}: "{errorLine}"')
