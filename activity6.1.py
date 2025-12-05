class Temprature:

    def celsius_to_fahrenheit(self, celsius):
        """Converts a temperature from Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """Converts a temperature from Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9


def main():
    req_input = input("Enter 'C' for Celsius prefix, or 'F' for Fahrenheit prefix followed by temprature: ")
    
    if len(req_input) < 2:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
        return
    
    prefix = req_input[0].capitalize()   # First character captialize(C or F)
    number_part = req_input[1:]  # Remaining part (should be a number)

    obj = Temprature()

    # Ensure temperature is numeric
    if not number_part.isdigit():
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
        return
    
    number_part = float(number_part)
     # Fahrenheit to Celsius
    if prefix == "F":
        resp =  obj.fahrenheit_to_celsius(number_part)
        print(round(resp, 2))
       

    # Celsius to Fahrenheit
    elif prefix == "C":
        resp =  obj.celsius_to_fahrenheit(number_part)
        print(round(resp, 2))
       
    
    # Invalid prefix
    else:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")
        return

   
if __name__ == "__main__":
    main()