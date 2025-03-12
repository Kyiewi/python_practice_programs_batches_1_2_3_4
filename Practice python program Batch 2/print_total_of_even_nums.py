# Get 10 numbers from user
nums = []
for num in range(10):
    number = int(input("Enter a number: "))
    nums.append(number)
    
# Count the even numbers in the list
even_count = sum(1 for num in nums if num % 2 == 0)

# Print the total count of even numbers
print("The count of even numbers is:", even_count)
