import collections
import math

with open('day08.txt') as input_file:
    puzzle_input = [line.strip() for line in input_file]


instructions = puzzle_input[0]


maps = {}
for line in puzzle_input[2:]:
    node, directions = (x.strip() for x in line.split('='))
    left, right = (x.strip() for x in directions.split(','))
    left = left[1:]
    right = right[:-1]
    maps[node] = (left, right)
'''
count = 0
current = 'AAA'
while current != 'ZZZ':
    turn = instructions[count % (len(instructions))]
    if turn == 'L':
        current = maps[current][0]
    else:
        current = maps[current][1]
    count += 1
print(count)
'''

def keep_going(depend_dict):
    if len(depend_dict) < 6:
        return True
    for node_ref in depend_dict:
        if len(depend_dict[node_ref]) < 2:
            return True
    return False

list_of_starts = [node for node in maps if node[-1] == 'A']
nodes = collections.deque()
for node in list_of_starts:
    nodes.append(node)

traveled = {}
next_nodes = collections.deque()
count = 0
all_target = False
true_count = 0
cycles = {}
while keep_going(cycles):
    all_target = True
    count = count % (len(instructions))
    next_nodes.clear()
    while nodes:
        current_node = nodes.pop()
        turn = instructions[count]
        if turn == 'L':
            next_node = maps[current_node][0]
        else:
            next_node = maps[current_node][1]
        next_nodes.append(next_node)
        if next_node[-1] != 'Z':
            all_target = False
        else:
            node_ref = len(next_nodes)
            if node_ref not in cycles:
                cycles[node_ref] = [true_count]
            else:
                cycles[node_ref].append(true_count)
        traveled[(current_node, count)] = next_node
    while next_nodes:
        nodes.append(next_nodes.pop())
    count += 1
    true_count += 1


reps = []
for node_ref in cycles:
    cycles[node_ref].sort()
    reps.append(cycles[node_ref][1] - cycles[node_ref][0])

lcm = 1
for i in reps:
    lcm = math.lcm(lcm, i)
print(lcm)
