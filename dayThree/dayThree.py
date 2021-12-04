import math

file = open("./dayThree/input.txt", "r")

content = file.read()
content_list = content.split("\n")
bitList = [0,0,0,0,0,0,0,0,0,0,0,0,]


for element in content_list:
    for index in range(0, len(element)):
        if element[index] == "1":
            bitList[index] += 1

bitGama = list(map(lambda x: math.ceil(math.tanh(x - 500)), bitList))
bitEpsilon = list(map(lambda x: math.ceil(math.tanh((x *-1) +1)),bitGama))

bitGama = ''.join(str(x) for x in bitGama)
bitEpsilon = ''.join(str(x) for x in bitEpsilon)
bitGama = int(bitGama, base=2)
bitEpsilon = int(bitEpsilon, base=2)
print(bitGama*bitEpsilon)