weather_data  =  [
    {'city':  'New York',  'temp_celsius':  22,  'humidity':  65},
    {'city':  'London',  'temp_celsius':  15,  'humidity':  80},
    {'city':  'Tokyo',  'temp_celsius':  28,  'humidity':  70},
    {'city':  'Sydney',  'temp_celsius':  18,  'humidity':  60},
    {'city':  'Dubai',  'temp_celsius':  35,  'humidity':  45}
]

# TODO: Use map() with lambda or user defined function to add Fahrenheit and Kelvin temperatures
# Formula: Fahrenheit = (Celsius × 9/5) + 32
# Formula: Kelvin = Celsius + 273.15

weather_converted  =  list(map(lambda  data:  {'city': data['city'],'temp_celsius': data['temp_celsius'], 'temp_fahrenheit': (data['temp_celsius']* (9/5)) + 32, 'temp_kelvin': data['temp_celsius'] + 273.15, 'humidity': data['temp_celsius'], }, weather_data))

# Test your result
print("Temperature Conversions:")
for  data  in  weather_converted:
    print(f"{data['city']}:")
    print(f"  Celsius: {data['temp_celsius']}°C")
    print(f"  Fahrenheit: {data['temp_fahrenheit']:.1f}°F")
    print(f"  Kelvin: {data['temp_kelvin']:.1f}K")