# Get 10 numbers from the user
numbers = [int(input("Enter a number: ")) for num in range(10)]

# Count the odd numbers in the list
odd_count = sum(1 for num in numbers if num % 2 != 0)

# Print the total count of odd numbers
print("The count of odd numbers is:", odd_count)

