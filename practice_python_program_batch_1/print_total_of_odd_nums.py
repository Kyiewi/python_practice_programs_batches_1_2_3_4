# Get 10 numbers from the user
nums = []
for num in range(10):
    number = int(input("Enter a number: "))
    nums.append(number)
  
# Count the odd numbers in the list
odd_count = sum(1 for num in nums if num % 2 != 0)

# Print the total count of odd numbers
print("The count of odd numbers is:", odd_count)

