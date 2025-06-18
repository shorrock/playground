
SAMPLE_INPUT = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]
DELIMITER = " "


def is_safe_report(line):
    last_datum = None
    first_delta = None
    line_numbers = line.split(DELIMITER)
    for line_number in line_numbers:
        datum = int(line_number)
        if last_datum:
            delta = datum - last_datum
            abs_delta = abs(delta)
            if abs_delta < 1 or abs_delta > 3:
                # Unsafe: delta is too small or too large
                return False
            
            if first_delta:
                #print(f"first_delta: {first_delta}, delta: {delta}")
                if first_delta > 0 and delta < 0:
                    # Unsafe: Was increasing, now decreasing
                    return False
                if first_delta < 0 and delta > 0:
                    # Unsafe: Was decreasing, now increasing
                    return False
            else:
                
                first_delta = delta
                
        last_datum = datum
    return True



safe_report_count = 0

# Test code on given sample inputs
'''
for line in SAMPLE_INPUT:
    if is_safe_report(line):
        #print(f"Safe report: {line}")
        safe_report_count += 1
'''

# Final code on input text file
with open("advent_of_code_2024/2/input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if is_safe_report(line):
            safe_report_count += 1


print(f"Number of safe reports: {safe_report_count}")