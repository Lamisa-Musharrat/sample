Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cities=["tokyo","dhaka","berlin"]
>>> "tokyo" in cities
True
>>> cities_high={"tokyo","dhaka","berlin"}
>>> "ctg" in cities_high
False
>>> cities_high=("tokyo","dhaka","berlin")
>>> "comilla" in  cities_high
False
>>> "han" in "My name is khan."
True
>>> #but in dictionary in can't check this.