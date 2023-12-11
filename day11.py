import numpy as np


def expand(expansion_factor):
    galaxies = []
    row_adder = 0
    for row_index, row in enumerate(puzzle_input):
        if '#' not in row:
            row_adder += expansion_factor - 1
        else:
            col_adder = 0
            for col_index, column_val in enumerate(row):
                if '#' not in puzzle_input[:, col_index]:
                    col_adder += expansion_factor - 1
                if column_val == '#':
                    galaxies.append((row_index + row_adder, col_index + col_adder))
    return galaxies


def sum_distances(galaxies):
    ans = 0
    for galaxy_index, galaxy in enumerate(galaxies):
        for pairing in galaxies[galaxy_index + 1:]:
            ans += abs(pairing[0] - galaxy[0]) + abs(pairing[1] - galaxy[1])
    return ans


with open('day11.txt') as file_input:
    puzzle_input = np.array([list(line.strip()) for line in file_input])

galaxies = expand(2)
print(sum_distances(galaxies))

galaxies = expand(1000000)
print(sum_distances(galaxies))