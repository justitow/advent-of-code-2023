from collections import deque


def reduce_delta(sequence):
    if sequence[0] == 0 and all(x == sequence[0] for x in sequence):
        return 0
    else:
        new_sequence = deque()
        curr = sequence.popleft()
        while sequence:
            prev = curr
            curr = sequence.popleft()
            new_sequence.append(curr - prev)
        ans = curr + reduce_delta(new_sequence)
        return ans


with open('day09.txt') as input_file:
    puzzle_input = [deque([int(number) for number in line.strip().split(' ')]) for line in input_file]

ans_1 = 0
for line in puzzle_input:
    ans_1 += reduce_delta(line)
print(ans_1)

with open('day09.txt') as input_file:
    puzzle_input = [deque([int(number) for number in line.strip().split(' ')][::-1]) for line in input_file]

ans_1 = 0
for line in puzzle_input:
    ans_1 += reduce_delta(line)
print(ans_1)
