FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    celcius= (fahrenheit- 32) *FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celcius):
    fahrenheit = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if scale == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F")
        elif scale == 'F':
            result = convert_to_celcius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C")
        else:
            print("Invalid temperature scale. Please enter'C' for Celcius or 'F' for fahrenheit.")
    except ValueError:
        print("Invalid temperature scale. Please enter a numeric value.")

if __name__ == "__main__":
    main()
