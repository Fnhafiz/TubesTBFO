# Python implementation for the
# CYK Algorithm

# Non-terminal symbols
non_terminals1 = ["NP", "Nom", "Det", "AP",
				"Adv", "A"]
terminals1 = ["book", "orange", "man",
			"tall", "heavy",
			"very", "muscular"]
non_terminals = ["FOR", "For", "A", "B",
				"C", "D","E","Kon","In","Ran","Var","Tutup"
                ,"Titik","Range","Buka"]
terminals = ["for", "in", "range",
			"x", "15",
			"(", ")",":"]

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
R2 = {
	"AS" : [["Import", "A"]],
	"A"  : [["Module", "B"]],
	"B"  : [["As", "Name"]],
	"Import" : [["import"]],
	"Module" : [["module"]],
	"As" : [["as"]],
	"Name"   : [["var"]]
	}
R3 = {
	"S" : [["Break"]],
	"S" : [["Continue"]],
	"Break" : [["break"]],
	"Continue" : [["continue"]]
	}
R4 = {
	"AND_OR" : [["Var", "A"]],
	"A"  : [["B", "Var2"]],
	"B"  : [["and"],["or"]],
	"Var": [["var"]],
	"Var2" :[["var2"]]
	}
R5 = {
	"NOT" : [["Not", "Var"]],
	"Not" : [["not"]],
	"Var" : [["var"]]
}
R6 = {
	"TRUE" : [["Var", "A"]],
	"A" : [["Equal", "True"]],
	#"Equal" : [["Assign"],["Compare"]],
	"Equal" : [["="],["=="]],
	"Assign" : [["="]],
	"Compare" : [["=="]],
	"True" : [["True"]],
	"Var" : [["var"]]
}
R7 = {
	"FALSE" : [["Var", "A"]],
	"A" : [["Equal", "False"]],
	#"Equal" : [["Assign"],["Compare"]],
	"Equal" : [["="],["=="]],
	"Assign" : [["="]],
	"Compare" : [["=="]],
	"False" : [["False"]],
	"Var" : [['var']]
}
R8 = {
	"NONE" : [["Var", "A"]],
	"A" : [["Equal", "None"]],
	#"Equal" : [["Assign"],["Compare"]],
	"Equal" : [["="],["=="]],
	"Assign" : [["="]],
	"Compare" : [["=="]],
	"None" : [["None"]],
	"Var" : [['var']]
}

# Function to perform the CYK Algorithm
def cykParse(w):
	n = len(w)
	
	# Initialize the table
	T = [[set([]) for j in range(n)] for i in range(n)]

	# Filling in the table
	for j in range(0, n):

		# Iterate over the rules
		for lhs, rule in R7.items():
			for rhs in rule:
				
				# If a terminal is found
				if len(rhs) == 1 and \
				rhs[0] == w[j]:
					T[j][j].add(lhs)

		for i in range(j, -1, -1):
			
			# Iterate over the range i to j + 1
			for k in range(i, j + 1):	

				# Iterate over the rules
				for lhs, rule in R7.items():
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

p = "for x in range ( 15 ) :".split()
q = "import module as var".split()
r = "break".split()
s = "continue".split()
t = "var and var2".split()
u = "var or var2".split()
v = "not var".split()
w = "var = True".split()
x = "var == False".split()

# Function Call
cykParse(x)
