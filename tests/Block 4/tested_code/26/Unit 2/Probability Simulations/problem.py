import random
random.seed()


def one_trial(nums=1000000):
    position = []
    for i in range(dimension):
        position.append(0)
    for j in range(nums):
        feature = random.randint(1,2)
        direction = random.randint(0,dimension-1)
        magnitude = 0
        if feature %2 ==0:
            magnitude = -1
        else:
            magnitude = 1
        position[direction] += magnitude   
        if position == origin:
            return 1
    return 0


def calculate(times = 100):
    record = []
    for i in range(times):
        record.append(one_trial())
    return sum(record)/times
dimension = int(input("Dimension: "))
origin = []
for i in range(dimension):
    origin.append(0)
print(calculate())
