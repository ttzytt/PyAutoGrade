'''
alkanes = ['methane','ethane','propane','butane','pentane']
carbohydrates = ['methane','lipids','butane','sugar','protein']

for alkane in alkanes:
    if (alkane in carbohydrates) is False: # Not in it
        carbohydrates.append(alkane)
print(carbohydrates)
'''
'''
alkanes = ['methane','ethane','propane','butane','pentane']
carbohydrates = ['methane','lipids','butane','sugar','protein','propane']
superimpose = []

for alkane in alkanes:
    if (alkane in carbohydrates) is True: # In it
        superimpose.append(alkane)
print('The elements below are present in both lists:')
print(superimpose)
'''
alkanes = ['methane','ethane','propane','butane','pentane']
alkenes = ['methene','ethylene','butene']
superimpose = []
for alkane in range(len(alkanes)):
    alkanes[alkane] = str(alkanes[alkane][0]+alkanes[alkane][1]+alkanes[alkane][2])
for alkene in range(len(alkenes)):
    alkenes[alkene] = str(alkenes[alkene][0]+alkenes[alkene][1]+alkenes[alkene][2])
for alkane in alkanes:
    if (alkane in alkenes) is True: 
        superimpose.append(alkane)
print(superimpose)
