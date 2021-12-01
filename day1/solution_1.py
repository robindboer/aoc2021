import os

input_file = open("./input.txt", "r")
depth_measurements = [int(line) for line in input_file.readlines()]

increased = 0

for index, measurement in enumerate(depth_measurements):
    if index == 0:
        continue

    if measurement > depth_measurements[index-1]:
        increased += 1

print(increased)
