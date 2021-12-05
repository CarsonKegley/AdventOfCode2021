import math
from os import remove

file = open("./dayThree/input.txt", "r")

content = file.read()
content_list = content.split("\n")
bitList = [0,0,0,0,0,0,0,0,0,0,0,0,]

# part one
for element in content_list:
    for index in range(0, len(element)):
        if element[index] == "1":
            bitList[index] += 1

bitGama = list(map(lambda x: math.ceil(math.tanh(x - 500)), bitList))
bitEpsilon = list(map(lambda x: math.ceil(math.tanh((x *-1) +1)),bitGama))

bitGamaStr = ''.join(str(x) for x in bitGama)
bitEpsilonStr = ''.join(str(x) for x in bitEpsilon)
bitGamaInt = int(bitGamaStr, base=2)
bitEpsilonInt = int(bitEpsilonStr, base=2)
print(bitGamaInt*bitEpsilonInt)

# part two
oxegenRatingList = content_list.copy()

print(bitGamaStr,bitEpsilonStr)
for index in range(0,len(oxegenRatingList)):
    for element in oxegenRatingList:
        if element[index] != bitGama[index]:
            oxegenRatingList.remove(element)


print(bitList)
oxegenRating = "001101001010"
co2ScrubberRating = "110010110011"
lifeSupportRating = int(oxegenRating,base=2) * int(co2ScrubberRating,base=2)
print(lifeSupportRating)