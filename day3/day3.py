#!/usr/bin/env python3

infile = "./day3/input.txt"
lines = list()
with open(infile, "r") as f:
    for line in f:
        lines.append(list(line.rstrip("\n")))


def calculate_consumption():
    gamma = 12 * [0]
    epsilon = 12 * [0]

    for i in range(12):
        tmp_sum = 0
        for x in range(len(lines)):
            tmp_sum += int(lines[x][i])
        gamma[i] = "1" if tmp_sum > len(lines) / 2 else "0"
        epsilon[i] = "0" if tmp_sum > len(lines) / 2 else "1"

    return int("".join(gamma), 2) * int("".join(epsilon), 2)


if __name__ == "__main__":
    print(f"Answer to part one is: {calculate_consumption()}")
