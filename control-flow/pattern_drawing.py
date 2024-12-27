def main():
    # Prompt the user for the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks for each column in the current row
        for col in range(size):
            print("*", end="")  # Print an asterisk without a newline
        print()  # Print a newline after each row

        row += 1  # Increment the row counter

# Call the main function to run the program
if __name__ == "__main__":
    main()
