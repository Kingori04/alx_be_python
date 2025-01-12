# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt the user for the temperature
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius_temp}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit_temp}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle invalid temperature input
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
