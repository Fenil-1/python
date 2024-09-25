# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    # Print the first half of the pattern (increasing order)
    for j in range(1, i + 1):
        print(j, end='')
    
    # Print the second half of the pattern (decreasing order)
    for j in range(i - 1, 0, -1):
        print(j, end='')
    
    # Move to the next line
    print()
