import re

with open('day05.txt') as input_file:
    puzzle_input = [line.strip() for line in input_file]

puzzle_input.append('')
seeds = list(map(int, puzzle_input[0].split(':')[-1].strip().split(' ')))

start = None
map_map = {}
seed_maps = {}
map_buffer = []
for line in puzzle_input[2:]:
    if line == '':
        seed_maps[start] = map_buffer
        start = None
        map_buffer = []
    elif ':' in line:
        first, _, second = line.split(' ')[0].split('-')
        start = first
        map_map[first] = second
    else:
        line_map = line.split(' ')
        map_buffer.append((int(line_map[0]), int(line_map[1]), int(line_map[2])))

lowest = float('inf')
seeds = iter(seeds)
mins = []
for chunk_start in seeds:
    chunk_range = next(seeds)
    current = 'seed'
    chunks = [(chunk_start, chunk_start + chunk_range - 1)]
    while current != 'location':
        seed_map = seed_maps[current]
        current = map_map[current]
        mapped_chunks = []

        # visualized like ####CL#####L######R######CR####
        # with L/R representing the range defined in the map
        # if it is not between CL and CR, then the chunk is maintained
        # otherwise, the chunk must be split apart into new chunks
        # and the unchanged parts must still be processed in the next
        # line of the seed_map

        for seed_dst, seed_src, seed_rng in seed_map:
            unmapped_chunks = []
            for chunk_left, chunk_right in chunks:
                left = seed_src
                right = seed_src + seed_rng - 1
                if chunk_left > right or chunk_right < left: # the seed_map is out of the range of the current chunk
                    unmapped_chunks.append((chunk_left, chunk_right))
                else:
                    if chunk_left < left:
                        unmapped_chunks.append((chunk_left, left - 1))
                    left = max(left, chunk_left)
                    if chunk_right > right:
                        unmapped_chunks.append((right + 1, chunk_right))
                    right = min(right, chunk_right)
                    mapped_chunks.append((left + (seed_dst - seed_src), right + (seed_dst - seed_src)))
            chunks = unmapped_chunks
        chunks += mapped_chunks
    min_vals = [val[0] for val in chunks]
    mins.append(min(min_vals))
print(min(mins))


