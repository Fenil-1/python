def process_file(input_file, output_file):
    name_sums = {}

    # Read the file and process each line
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.split()
            name = parts[0]  # The first part is the name
            numbers = map(int, parts[1:])  # Convert the rest to integers
            total = sum(numbers)  # Calculate the sum of integers

            # Store the sum in the dictionary
            if name in name_sums:
                name_sums[name] += total
            else:
                name_sums[name] = total

    # Identify the name with the highest sum
    highest_name = None
    highest_sum = -1

    for name, total in name_sums.items():
        if total > highest_sum:
            highest_sum = total
            highest_name = name

    # Output the name and the corresponding sum to a new file
    with open(output_file, 'w') as outfile:
        outfile.write(f"{highest_name} {highest_sum}\n")

# Example usage
input_file = 'largefile.txt'  # Replace with your input file name
output_file = 'result.txt'  # Replace with your desired output file name
process_file(input_file, output_file)
