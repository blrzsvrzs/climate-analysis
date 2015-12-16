from temp_conversion import fahr_to_kelvin
#from nose.tools import *
from random import randint

#def test_basic_value():
#	assert fahr_to_kelvin(20.0)==266.4833333333

def test_zero_value():
	assert round(fahr_to_kelvin(-459.67),2)==0.00

def test_random_value():
	fahr=randint(0,randint(0,100))
	assert fahr_to_kelvin(fahr)==((fahr - 32) * (5/9))+273.15

#@raises(TypeError)
#def test_temp_string():
#	assert fahr_to_kelvin("SomeTemperature")

#@raises(TypeError)
#def test_null_temp():
#	assert fahr_to_kelvin()