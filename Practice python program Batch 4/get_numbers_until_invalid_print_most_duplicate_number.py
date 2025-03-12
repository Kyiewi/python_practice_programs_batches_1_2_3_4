#empty list to save numbers
numbers = []

#Keep asking the user for a number until invalid input
while True:
    user_input = input("Enter a number: ")

    try:
        #Try to change input to a number
        number = float(user_input)
        
        #Add the number to the list
        numbers.append(number)
    except ValueError:
        #Print message when input is not a valid number
        print("Invalid input! Exiting the program.")
        #End the loop 
        break

# Check if there are numbers in the list
if numbers:
    # Find the number with the most duplicates
    most_frequent_number = max(set(numbers), key=numbers.count)
    # Print the number with the most duplicates
    print("The number with the most duplicates is:", most_frequent_number)
