import os

input_file = open("./input.txt", "r")
depth_measurements = [int(line) for line in input_file.readlines()]

increased = 0

for index, measurement in enumerate(depth_measurements):
    if index == 0:
        continue
    sum_b = sum(depth_measurements[index:index+3])
    sum_a = sum(depth_measurements[index-1:index+2])

    if sum_b > sum_a:
        increased += 1

print(increased)
