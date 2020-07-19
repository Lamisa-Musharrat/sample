Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums=[33,7,89,98,0009]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> nums=[78,98,897,890]
>>> nums
[78, 98, 897, 890]
>>> nums[0:4]
[78, 98, 897, 890]
>>> nums[0:2]
[78, 98]
>>> nums[-2:-3]
[]
>>> nums[2:]
[897, 890]
>>> names=['mici','kaki','pipi','pupi']
>>> names
['mici', 'kaki', 'pipi', 'pupi']
>>> names[1:3]
['kaki', 'pipi']
>>> x=names[1:3]
>>> x
['kaki', 'pipi']
>>> nums.append[24]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    nums.append[24]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums
[78, 98, 897, 890]
>>> nums.insert[2,90]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    nums.insert[2,90]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.insert(2,90)
>>> nums
[78, 98, 90, 897, 890]
>>> nums.append(40)
>>> nums
[78, 98, 90, 897, 890, 40]
>>>  