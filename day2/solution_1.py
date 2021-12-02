import os

input_file = open("./input.txt", "r")
instructions = [line for line in input_file.readlines()]

depth: int = 0
position: int = 0

for instruction in instructions:
    command, amount = tuple(instruction.split(" "))
    
    amount = int(amount)

    if command == "forward":
        position += amount
    if command == "down":
        depth += amount
    if command == "up":
        depth -= amount

print(f"depth: {depth}")
print(f"position: {position}")
print(f"multiplied: {depth * position}")
