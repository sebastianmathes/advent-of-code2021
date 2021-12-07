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
        gamma[i] = str(get_highest_bit(lines, i))
        epsilon[i] = str(get_lowest_bit(lines, i))
    consumption = int("".join(gamma), 2) * int("".join(epsilon), 2)

    return consumption


def get_highest_bit(values, position):
    temp_sum = 0
    for x in range(len(values)):
        temp_sum += int(values[x][position])

    return 1 if temp_sum >= len(values) / 2 else 0


def get_lowest_bit(values, position):
    temp_sum = 0
    for x in range(len(values)):
        temp_sum += int(values[x][position])

    return 0 if temp_sum >= len(values) / 2 else 1


def find_o2_rating(values, i=0):
    if len(values) == 1:
        return values[0]

    else:
        high_bit = get_highest_bit(values, i)
        new_values = list()
        for value in values:
            if int(value[i]) == high_bit:
                new_values.append(value)
        return find_o2_rating(new_values, i + 1)


def find_co2_rating(values, i=0):
    if len(values) == 1:
        return values[0]

    else:
        high_bit = get_lowest_bit(values, i)
        new_values = list()
        for value in values:
            if int(value[i]) == high_bit:
                new_values.append(value)
        return find_co2_rating(new_values, i + 1)


def calculate_life_rating():
    o2_rating = find_o2_rating(lines)
    co2_rating = find_co2_rating(lines)
    life_rating = int("".join(o2_rating), 2) * int("".join(co2_rating), 2)

    return life_rating


if __name__ == "__main__":
    print(f"Answer to part one is: {calculate_consumption()}")
    print(f"Answer to part two is: {calculate_life_rating()}")
