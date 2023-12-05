def find_score(line):
    card_id, card_contents = line.split(':')
    card_id = card_id.split(' ')[-1]
    left_side, right_side = card_contents.split('|')
    left_numbers = {int(number) for number in left_side.split(' ') if number != ''}
    right_numbers = {int(number) for number in right_side.split(' ') if number != ''}
    total = 0
    for number in left_numbers:
        if number in right_numbers:
            total += 1
    return total


with open('day04.txt') as input_file:
    puzzle = [line.strip() for line in input_file]

ans_1 = 0
for line in puzzle:
    total = find_score(line)
    if total > 0:
        ans_1 += pow(2, total - 1)
print(ans_1)

winning_array = [1 for line in puzzle]
for i, line in enumerate(puzzle):
    total = find_score(line)
    for offset in range(total):
        winning_array[i + 1 + offset] += (winning_array[i])
print(sum(winning_array))