#Get 10 numbers from user
nums = []
for num in range(10):
    number = float(input("Enter a number: "))
    nums.append(number)
    
#Subtract the sum of the remaining numbers from the first number
difference = nums[0] - sum(nums[1:])

# Print result
print("Result:", difference)
