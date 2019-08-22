def main():
    temperature = 45
    fahrenheit = convert_celsius_to_fahrenheit(temperature)
    celsius = convert_fahrenheit_to_celsius(temperature)
    print("Temperature: {} fahrenheit".format(fahrenheit))
    print("Temperature: {:.2f} celsius".format(celsius))


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


main()
