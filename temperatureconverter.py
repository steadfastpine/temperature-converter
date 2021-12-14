


class TemperatureConverter:


	def __init__(self,temperature_input,temperature_from,temperature_to):

		self.temperature_input=temperature_input
		self.temperature_from=temperature_from
		self.temperature_to=temperature_to
		self.temp=''


		if self.temperature_from == 'c':

			if self.temperature_to == 'f':
				self.temp = self.temperature_input * (9/5) + 32

			if self.temperature_to == 'k':
				self.temp = self.temperature_input + 273.15

			if self.temperature_to == 'r':
				self.temp= (self.temperature_input + 273.15) * (9/5)

			if self.temperature_to == 'de':
				self.temp = (100 - self.temperature_input) * (3/2)

			if self.temperature_to == 'n':
				self.temp = self.temperature_input * (33/100)

			if self.temperature_to == 're':
				self.temp = self.temperature_input * (4/5)

			if self.temperature_to == 'ro':
				self.temp = self.temperature_input * (21/40) + 7.5 



		if self.temperature_from == 'f':

			if self.temperature_to == 'c':
				self.temp = (self.temperature_input - 32) * (5/9)  

			if self.temperature_to == 'k':
				self.temp = (self.temperature_input + 459.67) * (5/9) 

			if self.temperature_to == 'r':
				self.temp = self.temperature_input + 459.67 

			if self.temperature_to == 'de':
				self.temp = (212 - self.temperature_input) * (5/6) 

			if self.temperature_to == 'n':
				self.temp = (self.temperature_input - 32) * (11/60)

			if self.temperature_to == 're':
				self.temp = (self.temperature_input - 32) * (4/9) 

			if self.temperature_to == 'ro':
				self.temp = (self.temperature_input - 32) * (7/24) + 7.5 


		if self.temperature_from == 'k':

			if self.temperature_to == 'c':
				self.temp =  self.temperature_input - 273.15 

			if self.temperature_to == 'f':
				self.temp = self.temperature_input * (9/5) - 459.67 

			if self.temperature_to == 'r':
				self.temp= self.temperature_input * (9/5) 

			if self.temperature_to == 'de':
				self.temp = (373.15 - self.temperature_input) * (3/2)

			if self.temperature_to == 'n':
				self.temp = (self.temperature_input - 273.15) * (33/100)

			if self.temperature_to == 're':
				self.temp = (self.temperature_input - 273.15) * (4/5) 

			if self.temperature_to == 'ro':
				self.temp = (self.temperature_input - 273.15) * (21/40) + 7.5 


		if self.temperature_from == 'r':

			if self.temperature_to == 'c':
				self.temp =  (self.temperature_input - 491.67) * (5/9)

			if self.temperature_to == 'f':
				self.temp = self.temperature_input - 459.67 

			if self.temperature_to == 'k':
				self.temp = self.temperature_input * (5/9) 

			if self.temperature_to == 'de':
				self.temp = (671.67 - self.temperature_input) * (5/6) 

			if self.temperature_to == 'n':
				self.temp = (self.temperature_input - 491.67) * (11/60) 

			if self.temperature_to == 're':
				self.temp = (self.temperature_input - 491.67) * (4/9) 

			if self.temperature_to == 'ro':
				self.temp = (self.temperature_input - 491.67) * (7/24) + 7.5 



		if self.temperature_from == 'de':

			if self.temperature_to == 'c':
				self.temp = 100 - self.temperature_input * (2/3) 

			if self.temperature_to == 'f':
				self.temp = 212 - self.temperature_input * (6/5)

			if self.temperature_to == 'k':
				self.temp = 373.15 - self.temperature_input * (2/3) 

			if self.temperature_to == 'r':
				self.temp = 671.67 - self.temperature_input * (6/5) 

			if self.temperature_to == 'n':
				self.temp = 33 - self.temperature_input * (11/50) 

			if self.temperature_to == 're':
				self.temp =80 - self.temperature_input * (8/15) 

			if self.temperature_to == 'ro':
				self.temp = 60 - self.temperature_input * (7/20) 


		if self.temperature_from == 'n':

			if self.temperature_to == 'c':
				self.temp = self.temperature_input * (100/33)

			if self.temperature_to == 'f':
				self.temp = self.temperature_input * (60/11) + 32 

			if self.temperature_to == 'k':
				self.temp = self.temperature_input * (100/33) + 273.15 

			if self.temperature_to == 'de':
				self.temp = (33 - self.temperature_input) * (50/11) 

			if self.temperature_to == 'r':
				self.temp= self.temperature_input * (60/11) + 491.67 

			if self.temperature_to == 're':
				self.temp = self.temperature_input * (80/33)

			if self.temperature_to == 'ro':
				self.temp = self.temperature_input * (35/22) + 7.5 


		if self.temperature_from == 're':

			if self.temperature_to == 'c':
				self.temp = self.temperature_input * (5/4) 

			if self.temperature_to == 'f':
				self.temp = self.temperature_input * (9/4) + 32 

			if self.temperature_to == 'k':
				self.temp = self.temperature_input * (5/4) + 273.15 

			if self.temperature_to == 'de':
				self.temp = (80 - self.temperature_input) * (15/8) 

			if self.temperature_to == 'r':
				self.temp = self.temperature_input * (9/4) + 491.67

			if self.temperature_to == 'n':
				self.temp =self.temperature_input * (33/80) 

			if self.temperature_to == 'ro':
				self.temp =  self.temperature_input * (21/32) + 7.5 


		if self.temperature_from == 'ro':

			if self.temperature_to == 'c':
				self.temp = (self.temperature_input - 7.5) * (40/21) 

			if self.temperature_to == 'f':
				self.temp = (self.temperature_input - 7.5) * (24/7) + 32 

			if self.temperature_to == 'k':
				self.temp = (self.temperature_input - 7.5) * (40/21) + 273.15

			if self.temperature_to == 'de':
				self.temp = (60 - self.temperature_input) * (20/7) 

			if self.temperature_to == 'r':
				self.temp=  (self.temperature_input - 7.5) * (24/7) + 491.67

			if self.temperature_to == 'n':
				self.temp = (self.temperature_input - 7.5) * (22/35)

			if self.temperature_to == 're':
				self.temp = (self.temperature_input - 7.5) * (32/21) 




