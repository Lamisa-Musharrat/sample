Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cities=["tokyo","berlin","denver","moscow"]
>>> cities[2]
'denver'
>>> cities(2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    cities(2)
TypeError: 'list' object is not callable
>>> cities
['tokyo', 'berlin', 'denver', 'moscow']
>>> cities_tuple=("tokyo","berlin","denver","moscow")
>>> cities_tuple[2]
'denver'
>>> cities[2]="stockholm"
>>> cities
['tokyo', 'berlin', 'stockholm', 'moscow']
>>> cities_tuple[2]="stockholm"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    cities_tuple[2]="stockholm"
TypeError: 'tuple' object does not support item assignment
>>> #we can assign value in list ,but not in tuple.
>>> #list starts with [],tuple()
>>> #in python to pop up any data we use []
>>> #if we do not want to change our data we use tuple
>>> #sets
>>> A={"sansa","danny","mike","el"}
>>> B={"mike","El","Max","lucas"}
>>> print(A | B)
{'Max', 'danny', 'sansa', 'mike', 'lucas', 'el', 'El'}
>>> #this is set uninon
>>> print(A & B)#set intersection
{'mike'}
>>> print(A - B)#set substraction
{'sansa', 'el', 'danny'}
>>> #xor
>>> #xor is to substract intersection from union like (A | B)-(A & B)
>>> #xor sign is ^
>>> A^B
{'Max', 'danny', 'sansa', 'lucas', 'el', 'El'}
>>> (A | B)- (A & B)
{'Max', 'danny', 'sansa', 'lucas', 'el', 'El'}
















