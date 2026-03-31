#2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

celsius = float(input('Enter temperatue in celsius:'))
fahrenheit = (celsius * 9/5) + 32
print(f'Temperature in fahrenheit : {fahrenheit}')