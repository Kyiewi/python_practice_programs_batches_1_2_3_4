# Get 10 numbers from the user
nums = []
for num in range(10):
    number = int(input("Enter a number: "))
    nums.append(number)

# Display all numbers, keeping only the first occurrence of duplicates
print("Numbers displayed:", end=" ")
seen = set()  # To track numbers already displayed
for num in nums:
    if num not in seen:
        print(num, end=" ")
        seen.add(num)  # Mark number as displayed
