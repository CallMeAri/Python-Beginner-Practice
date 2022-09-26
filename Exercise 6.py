with open("Python Text.txt", "r") as file:
    lines = file.readlines()

with open("New File.txt", "w") as file:
    count = 0
    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            file.write(line)
        count += 1

print("The count of the lines is " + str(count) + ".")