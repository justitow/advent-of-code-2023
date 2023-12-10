

def is_pipe(curr_node):
    if not 0 <= curr_node[0] < max_x or not 0 <= curr_node[1] < max_y:
        return '.'
    return puzzle_input[curr_node[1]][curr_node[0]]
def traverse_pipe(start, starting_type):
    curr = start
    prev = None
    pipe_type = starting_type
    traversed = set()
    while curr != start or len(traversed) == 0:
        x, y = curr
        left = (x + map_connection[pipe_type][0][0], y + map_connection[pipe_type][0][1])
        left_pipe = puzzle_input[left[1]][left[0]]
        right = (x + map_connection[pipe_type][1][0], y + map_connection[pipe_type][1][1])
        right_pipe = puzzle_input[right[1]][right[0]]
        if left == prev:
            traversed.add(curr)
            prev = curr
            curr = right
            pipe_type = right_pipe
        else:
            traversed.add(curr)
            prev = curr
            curr = left
            pipe_type = left_pipe

    return traversed



map_connection = {'|': ((0, 1), (0, -1)),
                  '-': ((1, 0), (-1, 0)),
                  'L': ((0, -1), (1, 0)),
                  'J': ((0, -1), (-1, 0)),
                  '7': ((0, 1), (-1, 0)),
                  'F': ((1, 0), (0, 1))}

ups_downs = {'|': (1, 1),
              '-': (0, 0),
              'L': (1, 0),
              'J': (1, 0),
              '7': (0, 1),
              'F': (0, 1)}


with open('day10.txt') as input_file:
    puzzle_input = [list(line.strip()) for line in input_file]


starting = None
for y, line in enumerate(puzzle_input):
    if 'S' in line:
        x = line.index('S')
        starting = (x, y)
        break


max_y = len(puzzle_input)
max_x = len(puzzle_input[0])

'''
for connection_type in map_connection:
    puzzle_input[starting[1]][starting[0]] = connection_type
    print(connection_type)
    print(traverse_pipe(starting, connection_type))
'''
puzzle_input[starting[1]][starting[0]] = '-'
path = traverse_pipe(starting, '-')

area = 0
for x in range(len(puzzle_input[0])):
    for y in range(len(puzzle_input)):
        curr_x = x
        if (x, y) not in path:
            ups = 0
            downs = 0
            while curr_x >= 0:
                test_point = (curr_x, y)
                if test_point in path:
                    ups += ups_downs[puzzle_input[y][curr_x]][0]
                    downs += ups_downs[puzzle_input[y][curr_x]][1]
                curr_x -= 1
            print(ups, downs)
            intersections = min(ups, downs)
            if intersections % 2 != 0:
                area += 1

print(area)