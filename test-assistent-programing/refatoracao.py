def calculate_list_statistics(numbers):
    """
    Calculate the total, mean, maximum, and minimum of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        tuple: (total, mean, maximum, minimum)
    """
    total = 0
    for number in numbers:
        total += number
    mean = total / len(numbers)

    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return total, mean, maximum, minimum

# Example usage
sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total_sum, average, max_value, min_value = calculate_list_statistics(sample_numbers)
print("Total:", total_sum)
print("Mean:", average)
print("Maximum:", max_value)
print("Minimum:", min_value)