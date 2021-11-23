from variable_checker import variable_checker

def cyk_algorithm(line, rules):
    n = len(line)

    # Deklarasi tabel untuk cyk algorithm
    table = [[set([]) for j in range(n)] for i in range(n)]

    for i in range(0, n):
        for j in range(0, n-i):
            # Untuk case pada baris pertama, kita cek terminal
            if i == 0:
                for lhs, rule in rules.items():
                    for rhs in rule:
                        # cek apabila berupa terminal
                        if len(rhs) == 1:
                            if rhs[0] == 'var':
                                if(variable_checker(line[j])):
                                    table[i][j].add(lhs)
                            elif rhs[0] == line[j]:
                                table[i][j].add(lhs)

            # Untuk case pada baris selain baris pertama, kita cek variabel
            else:
                for k in range(0, i):
                    for l in range(0, n-k):
                        for m in range(k, i):
                            for n in range(l+1, n-m):
                                # cek syarat
                                if k+m+1 == i:
                                    for lhs, rule in rules.items():
                                        for rhs in rule:
                                            # Cek apabila berupa variabel
                                            if len(rhs) == 2:
                                                is_var1 = rhs[0] in table[k][l]
                                                is_var2 = rhs[1] in table[m][n]

                                                # Jika dapat dibentuk
                                                if is_var1 and is_var2:
                                                    table[i][j].add(lhs)

    # Cek jika line bisa dibentuk berdasarkan rule
    if len(table[n-1][0]) != 0:
        return True
    else:
        return False
