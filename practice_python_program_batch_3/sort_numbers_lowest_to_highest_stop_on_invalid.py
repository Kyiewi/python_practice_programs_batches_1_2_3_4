# Get numbers from user  
nums = []  

# Loop until invalid input  
while True:  
    try:  
        number = int(input("Enter a number: "))    
        nums.append(number)  

    # Stop when input is not a number  
    except ValueError:  
        print("Invalid input, stopping...")  
        # End program  
        break  

# Sort numbers from lowest to highest
nums.sort()    

# Print sorted numbers  
print("Numbers from lowest to highest:", nums) 
