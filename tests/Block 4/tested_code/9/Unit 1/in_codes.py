

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
