Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=
SyntaxError: invalid syntax
>>> a=
SyntaxError: invalid syntax
>>> a = ['she','sea','sheels','by','the','sea','shore']
>>> b="selfish
SyntaxError: EOL while scanning string literal
>>> b="selfish shellfish"
>>> a
['she', 'sea', 'sheels', 'by', 'the', 'sea', 'shore']
>>> c=[1,1,2,3,5,8,13]
>>> c
[1, 1, 2, 3, 5, 8, 13]
>>> b[3:4]
'f'
>>> a[1]
'sea'
>>> a = ['sells','she','sea','sheels','by','the','sea','shore']
>>> a[1]
'she'
>>> a
['sells', 'she', 'sea', 'sheels', 'by', 'the', 'sea', 'shore']
>>> a[1]
'she'
>>> a = ['she','sells','sea','sheels','by','the','sea','shore']
>>> a[1]
'sells'
>>> c[8]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c[8]
IndexError: list index out of range
>>> c[6]
13
>>> c[5]
8
>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[2]
'sea'
>>> a[2:4]
['sea', 'sheels']
>>> a = ['she','sells','sea','shells','by','the','sea','shore']
>>> a[[3]0:5]
SyntaxError: invalid syntax
>>> "aliens are coming"[0:5]
'alien'
>>> a[3][0:5]
'shell'
>>> b[6:13]
'h shell'
>>> b[7:13]
' shell'
>>> c[1]+c[2]
3
>>> c[2]
2
>>> 'by' in a
True
>>> "self"in b
True
>>> a[2]==a[6]
True
>>> [1,2,5] in c
False
>>> 'sh'in c
False
>>> a[3]==b[8:13]
False
>>> dog='dalmatian'
>>> len(dog)
9
>>> dogs=[dog,'poodle','boxer']
>>> len(dogs)
3
>>> dogs
['dalmatian', 'poodle', 'boxer']
>>> def string_test(s):
	len(s)>2 and s[1]==s[-1]
string_test(potatop)
SyntaxError: invalid syntax
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
Traceback (most recent call last):
  File "/home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py", line 3, in <module>
    string_test(superdogs)
NameError: name 'superdogs' is not defined
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
give me a string:superdogs
>>> string_test(potatop)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    string_test(potatop)
NameError: name 'potatop' is not defined
>>> string_test("potatop")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    string_test("potatop")
  File "/home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py", line 6, in string_test
    print(false)
NameError: name 'false' is not defined
>>> 
>>> 
>>> string_test("Potato")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    string_test("Potato")
  File "/home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py", line 4, in string_test
    print(True)
NameError: name 'true' is not defined
>>> string_test("potatop")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    string_test("potatop")
  File "/home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py", line 6, in string_test
    print("False")
NameError: name 'false' is not defined
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
False
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
true
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
true
False
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
true
true
>>> a
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> string_test()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    string_test()
TypeError: string_test() missing 1 required positional argument: 's'
>>> string_test("aaa")
true
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
true
true
False
Traceback (most recent call last):
  File "/home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py", line 11, in <module>
    add_x(s)
NameError: name 's' is not defined
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
true
true
False
>>> 
==== RESTART: /home/student/moheeeldin19_lab5/meet2017y1lab5/stringfun.py ====
true
true
False
Xpax
>>> 
