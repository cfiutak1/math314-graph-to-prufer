import json

root = False
list_nodes = []

while True:
    value = int(input("Please enter the value of the vertex (enter -1 if done): "))
    if value == -1:
        break
    parent = int(input("Please enter the parent of the vertex (enter -1 if root): "))

    if root and parent == -1:
        print("Can't have 2 roots")
        continue

    if parent == -1:
        root = True

    list_nodes.append(
    {
        "value": value,
        "parent": parent,
    })

val_list = [i["value"] for i in list_nodes]
max_num = max(val_list)

for i in range(max_num):
    if i not in val_list:
        raise Exception("Invalid graph constructed")

file_name = input("Please enter a file name: ")
f = open(file_name, "w")

json.dump(list_nodes, f, indent=4)

f.close()
