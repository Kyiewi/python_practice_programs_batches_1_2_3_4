# Get numbers from user  
nums = []  
# Loop until invalid input  
while True:  
    try:  
        number = int(input("Enter a number: "))    
        nums.append(number)   

        # Check if number is already in the list  
        if nums.count(number) == 1:  
            # Print "Unique" if first time entered  
            print("Unique")    
        else:  
            # Print "Duplicate" if entered before  
            print("Duplicate")  

    # Stop when input is not a number  
    except ValueError:  
        print("Invalid input, stopping...")  
        # End program  
        break  
