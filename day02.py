
def game_possible(game):
    for color in game:
        if game[color] > limit[color]:
            return False
    return True

def fewest_possible(game):
    ans = 1
    for color in game:
        ans *= game[color]
    return ans


with open('day02.txt') as input_file:
    puzzle_input = [line.strip() for line in input_file]

limit = {'red': 12, 'green': 13, 'blue': 14}

games = {}
for line in puzzle_input:
    game_tag, game_matches_string = line.split(':')
    game_id = int(game_tag.split(' ')[-1])
    game_matches = game_matches_string.split(';')
    games[game_id] = {}
    for match in game_matches:
        colors = [color.strip().split(' ') for color in match.split(',')]
        for count_str, color in colors:
            count = int(count_str)
            if color not in games[game_id] or count > games[game_id][color]:
                games[game_id][color] = count

ans_1 = 0
for game_id in games:
    if game_possible(games[game_id]):
        ans_1 += game_id
print(f'The answer to part one is: {ans_1}')

ans_2 = 0
for game_id in games:
    ans_2 += fewest_possible(games[game_id])
print(f'The answer to part two is: {ans_2}')
