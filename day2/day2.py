#!/usr/bin/env python3

infile = "./day2/input.txt"
lines = list()
with open(infile, "r") as f:
    for line in f:
        lines.append({line.split()[0]: int(line.split()[1])})


def calculate_position():
    horizontal = 0
    depth = 0

    for line in lines:
        for x, y in line.items():
            if x == "forward":
                horizontal += y
            if x == "down":
                depth += y
            if x == "up":
                depth -= y

    return depth * horizontal


def calculate_aimed_position():
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        for x, y in line.items():
            if x == "forward":
                horizontal += y
                depth += y * aim
            if x == "down":
                aim += y
            if x == "up":
                aim -= y

    return depth * horizontal


if __name__ == "__main__":
    print(f"Answer to part one is: {calculate_position()}")
    print(f"Answer to part two is: {calculate_aimed_position()}")
