




def main():
    degreeStart, degreeEnd, degreeStartTemp = getTempAndSystem() 
    print(convertDegrees(degreeStart, degreeEnd, degreeStartTemp))
    

def getTempAndSystem(): 
    degreeStart = input('''What system is your tempurature in? Type "kelvin" for kelvin, "celsius" for celsius, "fahrenheight"
for fahrenheight. ''')
    degreeEnd = input('''What system is the temperature you want to convert it into? Type "kelvin" for kelvin, "celsius"
for celsius, "fahrenheight" for fahrenheight. ''')
    degreeStartTemp = input('Enter in a temperature you want to convert. ')

    return degreeStart, degreeEnd, float(degreeStartTemp)


def cToF(temp):
    return 32 + temp * 9.0/5
def fToC(temp):
    return (temp-32) * 5/9
def cToK(temp):
    return temp+273.15
def kToC(temp):
    return temp-273.15
def kToF(temp):
    return cToF(kToC(temp))
def fToK(temp):
    return cToK(fToC(temp))
def identity(temp):
    return temp



converters = {
    ('f', 'c') : fToC,
    ('c', 'f') : cToF,
    ('k', 'c') : kToC,
    ('c', 'k') : cToK,
    ('f', 'k') : fToK,
    ('k', 'f') : kToF,
    ('f', 'f') : identity,
    ('c', 'c') : identity,
    ('k', 'k') : identity,
}

def convertDegrees(degreeStart, degreeEnd, degreeStartTemp):

    fromScale = degreeStart.lower()[0]
    toScale = degreeEnd.lower()[0]
    converter = converters[fromScale, toScale]
    result = converter(degreeStartTemp)
    return result


if __name__ == '__main__':
    main()
