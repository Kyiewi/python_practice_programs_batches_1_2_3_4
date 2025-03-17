# Initialize total and count to 0
total = 0
count = 0

# Keep asking user to enter number until invalid
while True:
    user_input = input("Enter a number: ")

    try:
        # Try to change input to number
        number = float(user_input)
        
        # Add number to total and count +1
        total += number
        count += 1
    except ValueError:
        # If input not a number, stop program
        print("Invalid input! Exiting the program.")
        break

# Check if we got valid numbers
if count > 0:
    # Calculate and show the average
    average = total / count
    print("The average of the entered numbers is:", average)
