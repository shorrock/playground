
SAMPLE_INPUT = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]
DELIMITER = " "



def are_datum_outside_range(datum, last_datum):
    delta = abs(datum - last_datum)
    if delta < 1 or delta > 3:
        return True
    return False


def is_safe_report(line_numbers):
    #print(line_numbers)
    last_datum = None
    first_delta = None
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

# A truly naive approach might brute force checking if the deltas are all positive or all negative,
# and that each delta is in the range of 1 to 3, and if not iterating through deleting one index from
# the line's deltas one at a time and re-checking and only returning False if no single deletion then
# returns True as safe.
# What might less naive approaches be?
# - For the range check, this is simple, we can just count the number of range violations in one pass
#   and return True if the number of range violations is 0 or 1.
# - For the increasing/decreasing check, this seems harder. For each violation, in the previous logic,
#   the violation could be cured either by recalculating deltas by omitting the first datum or the 
#   "current" datum.
#   - Would it be valid, operating on these deltas, to remove up to any two consecutive deltas?
#   - A single bad report violation should express one bad delta if the first report, or two in a row.

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
    #lines = ['75 76 77 80 82 85 84',]
    for line in lines:
        #print(line)
        line_numbers = line.split(DELIMITER)
        index = 0
        if is_safe_report(line_numbers):
            safe_report_count += 1
            continue
        
        line_length = len(line_numbers)
        #print(line_length)
        # Try removing one item from the line at a time to see if we can then have a safe report.
        while index < line_length:
            #print(index)
            removed_number = line_numbers.pop(index)
            if is_safe_report(line_numbers):
                safe_report_count += 1
                break
            line_numbers.insert(index, removed_number)
            index += 1
        #print(f"Unsafe line: {line_numbers}")



print(f"Number of safe reports: {safe_report_count}")