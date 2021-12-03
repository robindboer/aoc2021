import os

input_file = open("./input.txt", "r")
values = [line for line in input_file.readlines()]

grid = [[bit for bit in num] for num in values]
columns = list(zip(*grid))
gamma = "".join([max(set(col), key=col.count) for col in columns])
epsilon = "".join([min(set(col), key=col.count) for col in columns])

print(f"Gamma: {gamma}, {int(gamma,2)}")
print(f"Epsilon: {epsilon}, {int(epsilon,2)}")
print(f"Multiplied: {int(gamma,2)*int(epsilon,2)}")
