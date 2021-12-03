import os

input_file = open("./input.txt", "r")
values = [line for line in input_file.readlines()]


def most_common(values, position):
    column = [val[position] for val in values]
    return "0" if column.count("1") < len(column) / 2 else "1"


oxygen = values
co2 = values

for i in range(len(oxygen[0])):
    if len(oxygen) == 1:
        break
    criteria = most_common(oxygen, i)
    oxygen = list(filter(lambda x: x[i] == criteria, oxygen))

for i in range(len(co2[0])):
    if len(co2) == 1:
        break
    criteria = most_common(co2, i)
    co2 = list(filter(lambda x: x[i] != criteria, co2))

oxygen = oxygen[0]
co2 = co2[0]

print(f"Oxygen: {oxygen}, {int(oxygen,2)}")
print(f"Co2: {co2}, {int(co2,2)}")
print(f"Multiplied: {int(oxygen,2)*int(co2,2)}")
