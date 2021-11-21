# Python implementation for the
# CYK Algorithm

# Non-terminal symbols
'''
non_terminals1 = ["NP", "Nom", "Det", "AP",
				"Adv", "A"]
terminals1 = ["book", "orange", "man",
			"tall", "heavy",
			"very", "muscular"]
non_terminals2 = ["FOR", "For", "A", "B",
				"C", "D","E","Kon","In","Ran","Var","Tutup"
                ,"Titik","Range","Buka"]
terminals2 = ["for", "in", "range",
			"x", "15",
			"(", ")",":"]
non_terminals = ["IF", "If", "A", "B",
				"Kon","Titik"]
terminals = ["if", "var",":"]
'''

# Rules of the grammar
R = {
	"NP": [["Det", "Nom"]],
	"Nom": [["AP", "Nom"], ["book"],
			["orange"], ["man"]],
	"AP": [["Adv", "A"], ["heavy"],
			["orange"], ["tall"]],
	"Det": [["a"]],
	"Adv": [["very"], ["extremely"]],
	"A": [["heavy"], ["orange"], ["tall"],
		["muscular"]]
	}
R1 = {
	"FOR": [["For", "A"]],
	"A": [["Kon", "B"],["Xar","B"]],
	"Kon": [["Xar","B1"]],
	"B1" : [["B2","B1"],["Koma","Xar"]],
	"B2" : [["Koma","Xar"]],
	"B": [["In","C"],["In","D"]],
    "C" : [["Ran","D"]],
    "Ran" : [["Range","Buka"],["Range"]],
    "D" : [["Var","E"],["Var","Titik"],["Var","D1"]],
	"D1" : [["D2","E"],["D2","D3"]],
	"D2" : [["Koma","Var"]],
	"D3" : [["D2","E"]],
    "E" : [["Tutup","Titik"],["Titik"]],
    "For": [["for"]],
	"Xar" : [["x"]],
	"Koma": [[","]],
	"In": [["in"]],
    "Range" : [["range"]],
    "Buka" : [["("]],
    "Var" : [["15"],["var"]],
    "Tutup" : [[")"]],
    "Titik" : [[":"]]
	}
R2 = {
	"IF": [["If", "A"]],
	"A": [["Kon", "Titik"],["Var","Titik"]],
	"Kon": [["Var","OP1"]],
	"OP1" : [["OP","OP1"],["Op","Var"]],
	"OP" :[["Op","Var"]],
	"If": [["if"]],
	"Op" : [[">"]],
	"Var" :[["var"]],
	"Titik": [[":"]]
	}
R2A = {
	"ELIF": [["Elf", "A"]],
	"A": [["Kon", "Titik"]],
	"Elf": [["elif"]],
	"Kon": [["var"]],
	"Titik": [[":"]]
	}
R2B = {
	"ELSE": [["Else", "A"]],
	"A": [["Kon", "Titik"]],
	"Else": [["else"]],
	"Kon": [["var"]],
	"Titik": [[":"]]
	}

R3 = {
	"DEF": [["Def", "A"]],
	"A": [["Fun", "B"]],
	"B": [["B1","D"],["Par","D"]],
	"B1" : [["Par","B2"]],
	"B2" : [["C","B2"],["Koma","Par"]],
	"C" : [["Koma","Par"]],
    "D" : [["Tutup","Titik"]],
    "Def": [["def"]],
    "Fun": [["Fungsi","Buka"]],
	"Fungsi" :[["function"]],
	"Buka": [["("]],
    "Par" : [["var"]],
	"Koma" : [[","]],
    "Tutup" : [[")"]],
    "Titik" : [[":"]]
	}
R4 = {
	"CLS": [["Cls", "A"]],
	"A": [["Name", "Titik"]],
	"Cls": [["class"]],
	"Name": [["var"]],
	"Titik": [[":"]]
	}
R5 = {
	"FRO": [["From", "A"]],
	"A": [["Var", "B"]],
	"B": [["Imp","Func"]],
	"From": [["from"]],
	"Var": [["var"]],
	"Imp" : [["import"]],
	"Func" : [["function"]]
	}
R6 = {
	"IMP": [["Imp","Var"]],
	"Imp": [["import"]],
	"Var": [["var"]]
	}

# Function to perform the CYK Algorithm
def cykParse(w):
	n = len(w)
	
	# Initialize the table
	T = [[set([]) for j in range(n)] for i in range(n)]

	# Filling in the table
	for j in range(0, n):

		# Iterate over the rules
		for lhs, rule in R2.items():
			for rhs in rule:
				
				# If a terminal is found
				if len(rhs) == 1 and \
				rhs[0] == w[j]:
					T[j][j].add(lhs)

		for i in range(j, -1, -1):
			
			# Iterate over the range i to j + 1
			for k in range(i, j + 1):	

				# Iterate over the rules
				for lhs, rule in R2.items():
					for rhs in rule:
						
						# If a terminal is found
						if len(rhs) == 2 and \
						rhs[0] in T[i][k] and \
						rhs[1] in T[k + 1][j]:
							T[i][j].add(lhs)

	# If word can be formed by rules
	# of given grammar
	if len(T[0][n-1]) != 0:
		print("True")
	else:
		print("False")
	
# Driver Code

# Given string
w = "for x , x , x , x in range ( var , var , var ) :".split()
x = "if var > var > var :".split()
z = "def function ( var , var , var , var , var ) :".split()
a = "class var :".split()
b = "from var import function".split()
c = "import var".split()
# Function Call
cykParse(x)
"aku,kamu"
