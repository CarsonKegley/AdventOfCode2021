file = open("./input.txt", "r")

content = file.read()
content_list = content.split("\n")
content_list_int = []
depthIncreases = 0
depthIncreasesTripple = 0



for index in range(1,len(content_list)):
    if content_list[index] > content_list[index-1]:
        depthIncreases += 1 

for index in range(0,len(content_list)-3):
    primaryTripple = int(content_list[index]) + int(content_list[index+1]) + int(content_list[index+2])
    secondaryTripple = int(content_list[index+1]) + int(content_list[index+2]) + int(content_list[index+3])
    if primaryTripple < secondaryTripple:
        depthIncreasesTripple += 1

print(depthIncreases)
print(depthIncreasesTripple)

