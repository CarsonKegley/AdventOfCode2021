file = open("./input.txt", "r")

content = file.read()
content_list = content.split("\n")
vector_list= []

for line in content_list:
    vector_list.append([line.split(" ")])

print(vector_list[0])