# Get 10 numbers from the user
nums = []
for num in range(10):
    number = int(input("Enter a number: "))
    nums.append(number)

# Print label before checking for unique numbers
print("Numbers that don't have duplicates:", end=" ")

# Check and print numbers that appear only once
for num in nums:
    if nums.count(num) == 1:  # Check if the number appears only once
        print(num, end=" ")  # Print the unique number
