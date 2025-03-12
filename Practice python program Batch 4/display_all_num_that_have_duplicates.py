# Get 10 numbers from the user
nums = []
for num in range(10):
    number = int(input("Enter a number: "))
    nums.append(number)

# Print label before checking for duplicate numbers
print("Numbers have duplicates:", end=" ")

# Check and print numbers that appear only once
printed = set()
for num in nums:
    if nums.count(num)>1 and num in printed:  
        printed.add(num)  


   
