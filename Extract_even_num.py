def extract_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 76, 12, 22, 11]
print(extract_even_numbers(numbers))