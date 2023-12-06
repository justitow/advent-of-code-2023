import re
import math

def lowest_and_highest(time, distance):
    a = 1
    b = -time
    c = distance

    x_p = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    x_n = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)

    lowest = math.ceil(x_p)
    if (time - lowest) * lowest == distance:
        lowest += 1
    highest = math.floor(x_n)
    if (time - highest) * highest == distance:
        highest -= 1
    return lowest, highest

with open('day06.txt') as input_file:
    puzzle_input = [line.strip() for line in input_file]

time_line = puzzle_input[0]
distance_line = puzzle_input[1]

times = re.findall(r'\d+', time_line)
distances = re.findall(r'\d+', distance_line)


# part 1
ans = 1
for index in range(len(times)):
    time = int(times[index])
    distance = int(distances[index])
    lowest, highest = lowest_and_highest(time, distance)
    ans *= highest - lowest + 1
print(ans)

# part 2
time = ''.join(times)
distance = ''.join(distances)
time = int(time)
distance = int(distance)
lowest, highest = lowest_and_highest(time, distance)
print(highest - lowest + 1)
