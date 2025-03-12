# Get numbers from user  
nums = []  

# Loop keep asking number  
while True:  
    try:  
        number = int(input("Enter a number: "))  
        nums.append(number)   

    # If not valid number, print stop message
    except ValueError:  
        print("Invalid input, stopping...")  
        # End loop  
        break  

# Find and print highest number  
if nums:  
    highest = max(nums)  
    print("Highest number:", highest)
