file = open("./dayTwo/input.txt", "r")

content = file.read()
content_list = content.split("\n")
vector_list = []
xValue = 0
yValue = 0

# Part one
for line in content_list:
    vector_list.append(line.split(" "))

for vector in vector_list:
    if vector[0] == "forward":
        xValue += int(vector[1])
    elif vector[0] == "down":
        yValue += int(vector[1])
    elif vector[0] == "up":
        yValue -= int(vector[1])

print(xValue*yValue)

# Part two
aim = 0
xValue = 0
yValue = 0

for vector in vector_list:
    if vector[0] == "forward":
        xValue += int(vector[1])
        yValue += int(vector[1]) * aim
    elif vector[0] == "down":
        aim += int(vector[1])
    elif vector[0] == "up":
        aim -= int(vector[1])

print(xValue*yValue)
