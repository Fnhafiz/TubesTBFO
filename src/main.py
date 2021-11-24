from rules_parser import rules_parser
from line_parser import symbols_parser
from cyk_algorithm import cyk_algorithm
from checker import replace_operator
from checker import string_checker
from checker import comment_checker
from checker import multicomment_checker
from checker import joining_line_checker
import sys

symbols = ['(', ')', '[', ']', '{', '}',
           ',', ':', '\'', '"',
           '+','-','*','/','%','@',
           '<', '>', '=', '\\']

# condition indeks 1 untuk kondisi if elif dan else
# condition indeks 2 untuk kondisi apakah masuk fungsi atau tidak
condition = [[], False,]

filename = sys.argv[1]
lines = []
with open(filename) as file:
    lines = file.readlines()
    lines = multicomment_checker(lines)
    lines = joining_line_checker(lines)

formatted_lines = []
for i in range(len(lines)):
    lines_checked = lines[i]
    lines_checked = comment_checker(lines_checked)
    lines_checked = string_checker(lines_checked)
    lines_checked = replace_operator(lines_checked)
    temp = symbols_parser(lines_checked, symbols)
    formatted_lines.append(temp)

rules = rules_parser('CNF_GABUNGAN.txt')

isCorrect = True
i = 0
while isCorrect and i < len(formatted_lines):
    line = formatted_lines[i]

    if (line[0] == ''):
        i += 1
        continue
    isCorrect, condition = cyk_algorithm(line, rules, condition)
    if (isCorrect):
        i += 1

if (isCorrect):
    print("Accepted")
else:
    print("Syntax Error")
    errorLine = "".join(lines[i])
    errorLine = errorLine.strip("\n")
    print(f'Terjadi kesalahan ekspresi pada line {i+1}: "{errorLine}"')
