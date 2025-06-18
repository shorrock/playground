DELIMITER = "   "
similarity_score = 0
left_numbers = []
right_number_frequencies = {}
with open("advent_of_code_2024/1/input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split(DELIMITER)
        left_numbers.append(int(numbers[0]))
        right_number = int(numbers[1])
        right_number_frequencies[right_number] = right_number_frequencies.get(right_number, 0) + 1

#print(left_numbers)
#print(right_number_frequencies)
for left_number in left_numbers:
    similarity_multiplier = right_number_frequencies.get(left_number, 0)
    similarity_score += left_number * similarity_multiplier
print(f"Final similarity score: {similarity_score}")