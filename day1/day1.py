#!/usr/bin/env python3

infile = "./day1/input.txt"
lines = list()
with open(infile, "r") as f:
    for line in f:
        lines.append(int(line))


def count_increase():
    increases = 0
    for x in range(len(lines) - 1):
        if lines[x + 1] > lines[x]:
            increases += 1

    return increases


def count_increase_sum():
    sum_increases = 0
    for x in range(len(lines) - 3):
        if lines[x + 3] > lines[x]:
            sum_increases += 1

    return sum_increases


if __name__ == "__main__":
    print(f"Answer to part one is: {count_increase()}")
    print(f"Answer to part two is: {count_increase_sum()}")
