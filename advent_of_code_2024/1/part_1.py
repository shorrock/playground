DELIMITER = "   "
difference_total = 0
left_numbers = []
right_numbers = []
with open("advent_of_code_2024/1/input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split(DELIMITER)
        left_numbers.append(int(numbers[0]))
        right_numbers.append(int(numbers[1]))
#print(len(left_numbers))
#print(len(right_numbers))
#print(left_numbers[0])
#print(right_numbers[0])
left_sorted = sorted(left_numbers)
right_sorted = sorted(right_numbers)
assert len(left_sorted) == len(right_sorted)
for i in range(len(left_sorted)):
    difference = abs(left_sorted[i] - right_sorted[i])
    difference_total += difference
print(f"Total diference: {difference_total}")
