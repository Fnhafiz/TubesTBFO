lines = []
with open('grammarConverter.py') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip('\n')
    words = line.split(" ")
    print(words)

print(lines[0])
