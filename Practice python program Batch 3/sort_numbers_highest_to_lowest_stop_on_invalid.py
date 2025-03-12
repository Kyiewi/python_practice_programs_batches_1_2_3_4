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

# Sort numbers from highest to lowest  
nums.sort(reverse=True)    

# Print sorted numbers  
print("Numbers from highest to lowest:", nums) 
