# This example demonstrates usage of the temperature conversion classes.


# Import the temperatureconverter.py file

from temperatureconverter import *


# Format: (temperature_input,temperature_from,temperature_to)

#   c   Celsius (centigrade)
#   f   Fahrenheit
#   k   Kelvin
#   r   Rankine
#   d   Delisle
#   n   Newton
#   re  Réaumur
#   ro  Rømer


# create an object with a a temp property equalling the converted
# value of 50 Celsius to Rømer units
test1 = TemperatureConverter(50,'c','ro')


# Print the converted temperature
print(test1.temp)

#33.75
