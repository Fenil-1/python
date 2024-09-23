def find_smallest_m(n):
    left, right = 1, n
    while left < right:
        m = (left + right) // 2
        sum_m = m * (m + 1) // 2
        
        if sum_m >= n:
            right = m
        else:
            left = m + 1
    
    return left

# Test the function
test_cases = int(input("Enter to check"))
print(find_smallest_m(test_cases))