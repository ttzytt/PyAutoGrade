'''
This program will automatically decide the unsaturation number
of an organic compound
'''
'''
# Through chemical formula
formula = input('Input the formula of the compound: ')
C = 0
H = 0
O = 0
N = 0
for count in range(len(formula)):
    if formula[count] == 'H':
        H = int(formula[count+1])
    elif formula[count] == 'N':
        N = int(formula[count+1])
    elif formula[count] == 'O':
        O = int(formula[count+1])
    elif formula[count] == 'C':
        C = int(formula[count+1])
unsat = ((2*C+2)-H)/2
print('The unsaturation number is ' + str(unsat))
print()
'''


cn = 0

unsat = 0
name = input('What\'s the name of chemical? ')
if name[0] == 'c' and name[1] == 'y' and name[2] == 'c': # cyclo-compound
    unsat += 1
if name[len(name)-3] == 'e': # methane & propene
    unsat += 1
if name[len(name)-3] == 'y': # methane & propene
    unsat += 2
if name[0] != 'c':
    if name[0] == 'm':
        cn = 1
    elif name[0] == 'e':
        cn = 2
    elif name[0] == 'p' and name[1] == 'r':
        cn = 3
    elif name[0] == 'b':
        cn = 4
    elif name[0] == 'p' and name[1] == 'e':
        cn = 5
    elif name[0] == 'h' and name[2] == 'x':
        cn = 6
    elif name[0] == 'h' and name[2] == 'p':
        cn = 7
    elif name[0] == 'o':
        cn = 8
    elif name[0] == 'n':
        cn = 9
    elif name[0] == 'd' and name[2] != 'd':
        cn = 10
    elif name[0] == 'd' and name[2] == 'd':
        cn = 12
elif name[0] == 'c': # cyclopropane
    if name[5] == 'm' or name[5] == 'e':
        cn = -1
    elif name[5] == 'p' and name[6] == 'r':
        cn = 3
    elif name[5] == 'b':
        cn = 4
    elif name[5] == 'p' and name[6] == 'e':
        cn = 5
    elif name[5] == 'h' and name[7] == 'x':
        cn = 6
    elif name[5] == 'h' and name[7] == 'p':
        cn = 7
    elif name[5] == 'o':
        cn = 8
    elif name[5] == 'n':
        cn = 9
    elif name[5] == 'd' and name[7] != 'd':
        cn = 10
    elif name[5] == name[7] == 'd':
        cn = 12
if cn >= 2:
    print('The chemical formula is C' + str(cn) + 'H' + str(2*(cn-unsat)+2))
elif cn == 1:
    print('The chemical formula is CH' + str(2*(cn-unsat)+2))
elif cn == -1:
    print('Cyclo-compound must contain at least 3 carbons')


