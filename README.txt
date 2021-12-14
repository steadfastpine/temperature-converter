                      
                      
    ___               
  ,--.'|_             
  |  | :,'            
  :  : ' :            
.;__,'  /     ,---.   
|  |   |     /     \  
:__,'| :    /    / '  
  '  : |__ .    ' /   
  |  | '.'|'   ; :__  
  ;  :    ;'   | '.'| 
  |  ,   / |   :    : 
   ---`-'   \   \  /  
             `----'   



Temperature Converter



# Contact: https://www.linkedin.com/in/steadfastpine/

# Release Date: 2019-06-17
# Version: .2



Description

	Convert temperatures between standard units including Celsius, Fahrenheit, Kelvin, Rankine, Delisle, Newton, Réaumur, and Rømer

Prerequisites

	Python 3



Installation

	Download and unzip the program files, then change working directory to them:
	
		# cd temperature-converter


		# Import the temperatureconverter.py file
		from temperatureconverter import *


		# Create an object with a temp property equalling the converted
		# value of 50 Celsius to Rømer units
		test1 = TemperatureConverter(50,'c','ro')


		# Supported units:

		c   Celsius (centigrade)
		f   Fahrenheit
		k   Kelvin
		r   Rankine
		d   Delisle
		n   Newton
		re  Réaumur
		ro  Rømer


		# Print the converted temperature
		print(test1.temp)

		#33.75



License 

	This program is licensed under the GPL License, view the LICENSE.md file for more information.














