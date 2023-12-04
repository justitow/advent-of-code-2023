import re


def adj_coord(x, y, x_lim, y_lim, length):
    output = []
    for extra_length in range(length):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (0 <= x + j + extra_length < x_lim) and (0 <= y + i < y_lim) and ((x + j + extra_length, y + i) != (x, y)):
                    if (x + j + extra_length, y + i) not in output:
                        output.append((x + j + extra_length, y + i))
    return output


non_operators = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}
def check_adj(x, y, puzzle, length, connections, part_num):
    x_limit = len(puzzle[0])
    y_limit = len(puzzle)
    touching_flag = False
    adj_coords = adj_coord(x, y, x_limit, y_limit, length)
    for coord in adj_coords:
        if puzzle[coord[1]][coord[0]] == '*':
            if (coord[0], coord[1]) not in connections:
                connections[(coord[0], coord[1])] = [part_num]
            else:
                connections[(coord[0], coord[1])].append(part_num)
        if puzzle[coord[1]][coord[0]] not in non_operators:
            touching_flag = True
    return touching_flag



with open('day03.txt') as input_file:
    puzzle_input = [line.strip() for line in input_file]


ans = 0
connections = {}
for y_val, line in enumerate(puzzle_input):
    results = [(m.group(), m.start()) for m in re.finditer('\\d+', line)]
    for result in results:
        if check_adj(result[1], y_val, puzzle_input, len(result[0]), connections, result[0]):
            ans += int(result[0])

ans_2 = 0
for connection in connections:
    if len(connections[connection]) == 2:
        ans_2 += int(connections[connection][0]) * int(int(connections[connection][1]))
print(ans)
print(ans_2)


