def c_to_f(celsius):
  return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in C"))

farenheit = c_to_f(celsius)

print("Temperature in Farenheit: ",farenheit)
