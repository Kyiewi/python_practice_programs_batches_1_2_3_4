# Get numbers from user  
nums = []  
seen = set()  
# Loop until invalid input  
while True:  
    try:  
        number = int(input("Enter a number: ")) 
        
# Check if number is already on the list  
        if number in seen:  
            # Print "Duplicate" if entered before
            print("Duplicate")    
        else:  
            # Print "Unique" if first time entered  
            print("Unique")  
            seen.add(number)   
        # Store all entered numbers 
        nums.append(number)  

    # Stop when input is not a number  
    except ValueError:  
        print("Invalid input, stopping...")  
        # End program  
        break  
