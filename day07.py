from collections import Counter
import functools

CARD_KEY = {'A': 14,
            'K': 13,
            'Q': 12,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
            'J': 1}


def rank_by_order(left, right):
    for i in range(len(left)):
        if left[i] != right[i]:
            if CARD_KEY[left[i]] > CARD_KEY[right[i]]:
                return 1
            else:
                return -1
    return 0


# numbers here are arbitrary, just needed a quick compare for the rank_by_card_count function
def find_type_rank(hand_counter):
    counts = hand_counter.values()
    if 5 in counts:
        return 10
    if 4 in counts:
        return 9
    if 3 in counts and 2 in counts:
        return 8
    if 3 in counts:
        return 7
    if 2 in counts:
        # forgot how to read and didn't realize that '2 pair' wasn't '2 of a kind'
        if list(counts).count(2) == 2:
            return 6
        return 5
    return 0


def rank_by_card_count(left, right):
    left_val, left_counter = left[0]
    right_val, right_counter = right[0]
    left_count = find_type_rank(left_counter)
    right_count = find_type_rank(right_counter)
    if left_count > right_count:
        return 1
    if right_count > left_count:
        return -1
    return rank_by_order(left_val, right_val)


with open('day07.txt') as input_file:
    puzzle_input = [line.strip() for line in input_file]

hands = []
for line in puzzle_input:
    hand, bid = line.split(' ')
    # Counter very quickly breaks apart a list into a dictionary of the count of items
    # efficient, much wow
    hand_counter = Counter(hand)
    # with the wildcard, it will always be better for the next-highest count to inherit the count
    del hand_counter['J']
    wild_cards = 5 - sum(hand_counter.values())
    # 5 wildcards
    if not hand_counter:
        hand_counter['J'] = 5
    else:
        # add the wildcard to the highest count
        hand_counter[max(hand_counter, key=hand_counter.get)] += wild_cards
    hands.append(((hand, hand_counter), int(bid)))
hands.sort(key=functools.cmp_to_key(rank_by_card_count))

ans = 0
for i in range(1, len(hands) + 1):
    ans += i * hands[i-1][1]
print(ans)
