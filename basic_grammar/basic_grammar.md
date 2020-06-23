# Basic Grammar

- [Basic Grammar](#basic-grammar)
  - [1 data types](#1-data-types)
    - [1.1 common data types](#11-common-data-types)
    - [1.2 others](#12-others)
  - [2 judge and loop](#2-judge-and-loop)
    - [2.1 judge](#21-judge)
    - [2.2 loop](#22-loop)
  - [3 string](#3-string)
    - [3.1 operation](#31-operation)
    - [3.2 function](#32-function)
    - [3.3 format](#33-format)
  - [4 list](#4-list)
    - [4.1 operation](#41-operation)
    - [4.2 index and fragmentation](#42-index-and-fragmentation)
    - [4.3 common function](#43-common-function)
      - [4.3.1 not change list](#431-not-change-list)
      - [4.3.2 change list](#432-change-list)
  - [5 dict](#5-dict)
    - [5.1 insert, index and update](#51-insert-index-and-update)
    - [5.2 function](#52-function)
  - [6 tuple](#6-tuple)
  - [7 function](#7-function)
    - [7.1 the definition and usage of function](#71-the-definition-and-usage-of-function)
    - [7.2 parameters](#72-parameters)
      - [7.2.1 parameters default values](#721-parameters-default-values)
      - [7.2.2 indefinite number of parameters](#722-indefinite-number-of-parameters)
    - [7.3 return](#73-return)
    - [7.4 function of map](#74-function-of-map)
    - [7.5 lambda](#75-lambda)
  - [8 iterator](#8-iterator)
    - [8.1 introduction](#81-introduction)
    - [8.2 custom iterator](#82-custom-iterator)
  - [9 generator](#9-generator)
    - [9.1 compare to while loop and iterator](#91-compare-to-while-loop-and-iterator)
  - [10 decorator](#10-decorator)
  - [11 module and package](#11-module-and-package)
    - [11.1 module](#111-module)
    - [11.2 package](#112-package)
  - [12 Exception handling](#12-exception-handling)
    - [12.1 try & except](#121-try--except)
    - [12.2 custom exception](#122-custom-exception)
  - [13 read and write file](#13-read-and-write-file)
    - [13.1 read file](#131-read-file)
    - [13.2 write file](#132-write-file)
    - [13.3 binary file](#133-binary-file)
    - [13.4 with](#134-with)
  - [14 object-oriented](#14-object-oriented)
  - [14 regular expression](#14-regular-expression)
  - [15 process and thread](#15-process-and-thread)

- read and write file

- object-oriented

- regular expression

- network programming

- processes and threads

## 1 data types

### 1.1 common data types

| type   | example               | is mutable    |
| ---    | ---                   | ---           |
| int    |  -100                 | **immutable** |
| float  | 3.1416                | **immutable** |
| string | 'hello'               | **immutable** |
| list   | [1, 1.2, 'hello']     | **mutable**   |
| dict   | {"dogs": 5, "pigs":3} | **mutable**   |

### 1.2 others

| type  | example        | is mutable    |
| ---   | ---            | ---           |
| long  | 1000000000000L | **immutable** |
| bool  | True/False     | **immutable** |
| tuple | ('ring', 1000) | **immutable** |
| set   | {1, 2, 3}      | **mutable**   |

## 2 judge and loop

### 2.1 judge

grammar:  

```python
if <condition 1>:  
  <statements>
elif <condition 2>:  
  <statements>
# ...  
else:  
  <statements>
```

except None, 0, False, empty string, empty list,  
empty dict and empty set, other value will be True.

### 2.2 loop

(1) while  
grammar:  
while `<condition>`:  
&nbsp; `<statements>`  
[else:  
&nbsp; statements]

(2) for  
grammar:  
for `<variable>` in `<sequence>`:  
&nbsp; `<statements>`  
[else:  
&nbsp; statements]

(3) continue and break  
'continue' in loop's statements will make program go back  
to the begin of the loop, which means the loop go to next  
step ignoring the statements below the 'continue'.

'break' means stop loop and go to next code block.

## 3 string

string will created by single quote (') or double quote (").  

multiline string can be created by three single quotes (''') or three  
double quotes (""").  

### 3.1 operation

the '+' operation will concatenate two strings. example:  
'a'+'b' is equal to 'ab'. and the '*'  operation will make  
string concatenate itself some times. example: 'a'*3 is equal  
to `'aaa'`.

### 3.2 function

here are some common function of string:split(), join(), replace(),  
upper(), lower(), strip(), lstrip(), rstrip(). use these function  
in string.function().  

convert the whole to different types of strings according to different  
binaries. hex( int ), oct( int ), bin( int ). int(str, 16/8/2) can convert  
str to int in hex or oct or bin.

when the data type of s is string, dir(s) will show all function s has.

### 3.3 format

format string:

```python
print('{} {} {}'.format('a', 'b', 'c'))
# 'a b c'

print('{2} {1} {0}'.format('a', 'b', 'c'))
# 'c b a'

print('{color} {n} {x}'.format(n=10, x=1.5, color='blue'))
# 'blue 10 1.5'

print('{color} {0} {x} {1}'.format(10, 'foo', x = 1.5, color='blue'))
# 'blue 10 1.5 foo'

# 可以用{<field name>:<format>}指定格式：
from math import pi
print('{0:10} {1:10d} {2:10.2f}'.format('foo', 5, 2 * pi))
# 'foo                 5       6.28'

s = "some numbers:"
x = 1.34
y = 2
# 用百分号隔开，括号括起来
print("%s %f, %d" % (s, x, y))
# 'some numbers: 1.340000, 2'
```

## 4 list

list is ordered sequence.

### 4.1 operation

'+' '*':  

```python
a = [1, 2, 3]
b = [3.2, 'hello']
print(a + b)
# [1, 2, 3, 3.2, 'hello']

print(b * 2)
# [3.2, 'hello', 3.2, 'hello']
```

### 4.2 index and fragmentation

index starts at 0. and can be fragmented by ':'.examples:

```python
a = [1, 2, 3]
print(a[0], a[1], a[-1])
# 1 2 3
print(a[0:2])
# [1, 2]
print(a[2::-1])
# [3, 2, 1]
print(a[2::-2])
# [3, 1]
print(a[::-1])
# [3, 2, 1]

# modify
a[:2] = [5, 4]
print(a)
# [5, 4, 3]

# test is in or not
print(3 in a)
# True
print(6 in a)
# False
```

### 4.3 common function

most used:  
len(l) return the length of l(data type is list).
del(a[0]) will remove the first element in list.
sorted(l) will sort the list and return the result.  

#### 4.3.1 not change list

count(e): the counter of e  
index(e): the index of e  

```python
a = [1, "a", 2, "a"]
print(a.count("a"))
# 2
print(a.index("a"))
# 1
```

#### 4.3.2 change list

append(e): append element e  
extend(l): append list l  
insert(index, e): insert element e into list at index.  
remove(e): remove the first element e  
pop(index): remove the element at index and return it.
sort(): sort list without return  
reverse(): reverse the list  

```python
a = [1, 2, 3, 4]

a.append(5)
print(a)
# [1, 2, 3, 4, 5]

a.extend([6, 7, 8])
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8]

a.insert(0, 0)
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

a.remove(8)
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7]

print(a.pop(0))
# 0
print(a)
# [1, 2, 3, 4, 5, 6, 7]

a.sort(reverse=True)
print(a)
# [7, 6, 5, 4, 3, 2, 1]
```

## 5 dict

created by {} or dict()  

```python
a = {0:'zer0', 1:'one'}
print(type(a))
# dict

b = dict(
    (1, 'one'),
    (2, 'tow')
)
print(type(b))
# dict
```

### 5.1 insert, index and update

used like list, keys are the index of list, and values are the elements of list.  
**the key of dictionary must be immutable, and value can be anything.**  
example:  

```python
a = {'one': 'this is number 1', 'two': 'this is number 2'}
print(a)
# {'one': 'this is number 1', 'two': 'this is number 2'}
print(type(a))
# dict

a['three'] = "this is number 3"
print(a)
# {'one': 'this is number 1', 'two': 'this is number 2', 'three': "this is number 3"}

print(a['two'])
# 'this is number 2'

a['one'] = 1
a['two'] = 2
print(a)
# {'one': 1, "two": 2, 'three': "this is number 3"}
```

### 5.2 function

get(key, default=None): return the corresponding value if exists, or None.
pop(key, default=None): remove the corresponding value if exists and return it, or return None.
update(new_dict): if key of new_dict not in the dict, then add it to the dict;  
else modify the corresponding value of dict to the corresponding of new_dict.
keys(): return all keys of dict in list as the order in dict.
values(): return all values of dict in list as the order in dict.
items(): return all item of dict in list, and the element of the list is tuple(key, value)

```python
a = {0: "zero", 1: "one"}
print(a.get(0), a.get(2))
# "zero" None
print(a.pop(1), a.pop(1, default="not exist"))
# "one" "not exist"

a.update({0: '0', 1: '1'})
print(a)
# {0: '0', 1: "1"}

print(a.keys())
# [0, 1]
print(a.values())
# ['0', '1']
print(a.items())
# [(0, '0'), (1, '1')]

# about the in
print(0 in a)
# True
print('0' in a)
# False
```

## 6 tuple

created by () or tuple(list), and it is immutable.  

tuple support index and fragmentation.  

(10) is equal to 10. (10, ) is type of tuple.  

besides, tuple has function of count(e) and index(e), similar to list.

## 7 function

### 7.1 the definition and usage of function

- keyword is **def**
  
- function name follows the keyword **def**. the function parameters are in parentheses, different parameters are separated by ','. example: def foo():
  
- use indentation to divide the contents of a function.
  
- docstring: use """ to contain the string used to explain the purpose of the function, can be omitted

when using a function, only need to change the parameter to a specific value and pass it to the function.
example:

```python
def add(x, y):
    """Add two numbers"""
    a = x + y
    return a

print(add(2, 3))
# 5
print(add("color", y="bar"))
# "colorbar"
print(add(y="bar", x="color"))
# "colorbar"
```

### 7.2 parameters

#### 7.2.1 parameters default values

example:  

```python
def quad(x, a=1, b=0, c=0):
    return a*x**2 + b*x + c

print(quad(2))
# 4

print(quad(2, b=2))
# 8

print(quad(2, b=2, c=1))
# 9
```

#### 7.2.2 indefinite number of parameters

here are two methods can achieve this, `*args` and `**kwargs`.  
`*args` in the function is a tuple, and `**kwargs` in the function is a dict.  

example:  

```python
def add(x, *args):
    total = x
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4))
# 10

def add(x, **kwargs):
    total = x
    for arg, value in kwargs.intems():
        print("adding ", arg)
        total += value
    return total

print(add(10, y=11, z=12, w=13))
# adding y
# adding z
# adding w
# 46

def foo(*args, **kwargs):
    print(args, kwargs)

foo(2, 3, x='color', y=255)
# (2, 3) {"x": "color", "y": 255}
```

### 7.3 return

example:  

```python
def add(x, y):
    return x**2-y**2, x**2+y**2

x, y = [2, 4]  # the same as x, y = (2, 4)
print(add(x, y))
# (-12, 20)

z = [2, 4]  # the same as z = (2, 4)
print(add(*z))
# (-12, 20)

d = {'x': 2, 'y': 4}
print(add(**d))
# (-12, 20)
```

### 7.4 function of map

usage of map is map(function, sequence1 [, sequence2]), and this will create a sequence consisted of return.  

example:  

```python
def add(x, y):
    return x+y
a = (2, 3, 4)
b = (6, 5, 4)
print(map(add, a, b))
# [8, 8, 8]
```

### 7.5 lambda

[python lambda](https://realpython.com/python-lambda/)

## 8 iterator

### 8.1 introduction

explicitly created by iter().  

An iterator is an object that can remember the position of traversal.  

The iterator object is accessed from the first element of the collection until all elements are accessed. The iterator can only go forward without going backward.  

Iterator has two basic methods: iter() and next().  

String, list or tuple objects can be used to create iterators  

example:  

```python
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
# 1
print (next(it))
# 2
```

traverse:  

```python
l=[1,2,3,4]
it = iter(l)    # 创建迭代器对象

# method 1
for x in it:
    print (x, end=" ")
# 1 2 3 4

# method 2
while True:
    try:
        print (next(it), end=" ")
    except StopIteration:
        sys.exit()
# 1 2 3 4
```

enumerate(iteration or iterable object) will return a tuple consist of (index, value):

```python
l = [2, 4, 6]

for i, n in enumerate(l):
  print("pos", i, "is", n)
# pos 0 is 2
# pos 1 is 4
# pos 2 is 6
```

### 8.2 custom iterator

must implement two methods `__iter__`() and `__next__`().

```python
class ReverseListIterator(object):

    def __init__(self, list):
        self.list = list
        self.index = len(list)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.list[self.index]
        else:
            raise StopIteration

x = range(10)
for i in ReverseListIterator(x):
    print(i, end=" ")
# 9 8 7 6 5 4 3 2 1 0
```

The StopIteration exception is used to mark the completion of the iteration and prevent the occurrence of an infinite loop. In the `__next__`() method, we can set the StopIteration exception to be triggered after the specified number of cycles is completed to end the iteration.

another example which exposes a problem about iterator and iteration.

```python
class Collatz(object):

    def __init__(self, start):
        self.value = start

    def __iter__(self):
        return self

    def next(self):
        if self.value == 1:
            raise StopIteration
        elif self.value % 2 == 0:
            self.value = self.value / 2
        else:
            self.value = 3 * self.value + 1
        return self.value

for x in Collatz(7):
    print(x, end=" ")
# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
i = Collatz(7)
for x, y in zip(i, i):
    print x, y
# 22 11
# 34 17
# 52 26
# 13 40
# 20 10
# 5 16
# 8 4
# 2 1
```

[the solution reference](https://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/05-advanced-python/05.09-iterators.ipynb)

## 9 generator

### 9.1 compare to while loop and iterator

```python
# while loop
<do setup>
result = []
while True:
    <generate value>
    result.append(value)
    if <done>:
        break

# iterator
class GenericIterator(object):
    def __init__(self, ...):
        <do setup>
        # 需要额外储存状态
        <store state>
    def next(self):
        <load state>
        <generate value>
        if <done>:
            raise StopIteration()
        <store state>
        return value

# generator
def generator(...):
    <do setup>
    while True:
        <generate value>
        # yield 说明这个函数可以返回多个值！
        yield value
        if <done>:
            break
```

the generator uses the yield keyword to output the value, and the iterator returns the value through the next return; unlike the iterator, the generator automatically records the current state, and the iterator requires additional operations to record the current status.

```python
# collatz conjecture

# method 1 basic loop
def collatz(n):
    sequence = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence

for x in collatz(7):
    print(x, end=" ")
# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

# method 2 iterator
class Collatz(object):
    def __init__(self, start):
        self.value = start

    def __iter__(self):
        return self

    def next(self):
        if self.value == 1:
            raise StopIteration()
        elif self.value % 2 == 0:
            self.value = self.value/2
        else:
            self.value = 3*self.value + 1
        return self.value

for x in Collatz(7):
    print( x, end=" ")
# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

# method 3 generator
def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        yield n
# generator will return a iterator

for x in collatz(7):
    print(x, end=" ")
# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

# generator support __next__() and __iter__().
```

## 10 decorator

[read reference](https://www.cnblogs.com/huchong/p/7725564.html)  
question: decorating class will have different activation.  
detail:  

```python
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo　　# bar = Foo(bar)
def bar():
    print('bar')


bar()　　# Foo(bar)()

# class decorator runing
# bar
# class decorator ending

class Foo(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def _call(*args, **kw):
            print('class decorator runing')
            return func(*args, **kw)

        return _call


class Bar(object):
    @Foo()
    def bar(self, test, ids):   # bar = Foo()(bar)
        print('bar')


Bar().bar('aa', 'ids')
```

## 11 module and package

### 11.1 module

a py file can be a module, and when use this module, just import it like this  
"import xxx". in jupyter, while import a module, this module will be run.  
when import a module secondly, the module will not be run at the last time.  

about distinct script and module:  

the property of `__name__` will be `__main__`, only when the file is used as script.  

### 11.2 package

example of package:  
folder:foo/  
files in foo:  

- `__init__`.py
- bar.py
- baz.py

requirements of import package:  

- the folder of foo in the search path of Python.
- `__init__.py`  is used to indicate the foo is a package, and it can be empty.  

common stand library:

- re
- copy
- math, cmath
- decimal, fraction
- sqlite3
- os, os.path
- gzip, bz2, zipfile, tarfile
- csv, netrc
- xml
- htmllib
- ftplib, socket
- cmd
- pdb
- profile, cProfile, timeit
- collections, heapq, bisect
- mmap
- threading, Queue
- multiprocessing
- subprocess
- pickle, cPickle
- struc

## 12 Exception handling

### 12.1 try & except

once there is an exception in the content of the try block, the content behind  
the try block will be ignored, and Python will find if there is no corresponding  
content in the except. If it is found, the corresponding block will be executed.  
If not, the exception will be thrown.  
__note__: catch maybe not exist.

except:  

```python
import math

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = math.log10(x)
        print "log10({0}) = {1}".format(x, y)
    except ValueError:
        print "the value must be greater than 0"
# > -1
# the value must be greater than 0
# > 0
# the value must be greater than 0
# > 1
# log10(1.0) = 0.0
# > q
```

'except Exception :' means catching all exception.  
'except (ValueError, ZeroDivisionError): ' will catch 'ValueError' and 'ZeroDivisionError'.
'except (ValueError, ZeroDivisionError)' is equal to  
'except ValueError:  
&nbsp; `statements`  
except ZeroDivisionError:  
&nbsp; `statements`'  

class Exception has 'message' property, and this property have the detail of  
this exception.

try/catch has a optional keyword finally. No matter there is exception in try block,  
finally will be run.  

```python
try:
    print 1 / 0
except ZeroDivisionError:
    print 'divide by 0.'
finally:
    print 'finally was called.'
# divide by 0.
# finally was called.
```

### 12.2 custom exception

```python
class CommandError(ValueError):
    pass
# class 'CommandError' inherits 'ValueError'.

valid_commands = {'start', 'stop', 'pause'}

while True:
    command = raw_input('> ')
    try:
        if command.lower() not in valid_commands:
            raise CommandError('Invalid commmand: %s' % command)
    except CommandError:
        print 'Bad command string: "%s"' % command

# class 'Exception' get string as message.
```

## 13 read and write file

create test.txt in jupyter and input something.  

```jupyter
%%writefile test.txt
this is a test file.
hello world!
python is good!
today is a good day.
```

### 13.1 read file

- there are two methods to read file:  

1. f = open('test.txt')
2. f = file('test.txt')

these two functions open files by default by reading. if file not exists, throw error.  

- after open file, there are several methods to read.

1. f.read() will read all content of the file.
2. f.readlines() will return a list consisted of all lines of the file.

- at the end, after using file, close it is required.  
__f.close()__  

__note__: if file is used as iteration, it will be equal to f.readlines().  

- remove file

```python
import os
os.remove('test.txt')
```

### 13.2 write file

commonly, the steps to write file are as following:

```python
# 1. open file by write
f = open('myfile.txt', 'w')

# 2. use write function to write
f.write('hello world!')

# 3. close file
f.close()

print(open('myfile.txt').read())
# hello world!
```

- 'w'
when we open file by write, if file does not exist, the file will be created.  
if file exists, the file will be __overwrite__.  

```python
f = open('myfile.txt', 'w')
f.write('another words!')
f.close()
print(open('myfile.txt').read())
# another words!
```

- 'a'
'a' means appending. this will avoid overwriting.

```python
f = open('myfile.txt', 'a')
f.write('... and more')
f.close()
print(open('myfile.txt').read())
# another words!... and more
```

- 'w+'
'w+' means read and write.

```python
f = open('myfile.txt', 'w+')
f.write('hello world!')
f.seek(6)
print f.read()
f.close()
# world!

import os
os.remove('myfile.txt')
```

f.seek(6) means moving to sixth character, and then, f.read() will read the rest.

in different OS, the line break character may be different:

- \r
- \n
- \r\n

using U param will treat these three as \n.

### 13.3 binary file

- `'wb'`
write in binary

- `'rb'`
read in binary

```python
import os
f = open('binary.bin', 'wb')
f.write(os.urandom(16))
f.close()

f = open('binary.bin', 'rb')
print(f.read())
# '\x86H\x93\xe1\xd8\xef\xc0\xaa(\x17\xa9\xc9\xa51\xf1\x98'
f.close()

import os
os.remove('binary.bin')
```

__note__: while write file, if exception happens, the writing may be not correct.  
under this condition, use try/catch/finally. and it will make sure write file correctly  
put the action of closing file in block finally.

### 13.4 with

when open file with keyword 'with', the file will be closed after the code block run.  
this has the same effect as try/catch/finally, and easier.  

## 14 object-oriented

reference:  

- [1. `Eva-J`](https://www.cnblogs.com/Eva-J/articles/7293890.html#_label3)
- [2. `日上百万`](https://blog.csdn.net/weixin_44239490/article/details/86357989)

note:  

1. namespace
create a class will create its namespace used to store it properties.  
class has two different types of property:

- static property
  the variable defined in class.  
  the variable will be shared among all objects.
- dynamic property
  the method defined in class.  
  the method will be bunded to all objects.

## 14 regular expression

[regular expression](https://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/05-advanced-python/05.04-regular-expression.ipynb)

## 15 process and thread

[1.0 `廖雪峰python3`](https://www.liaoxuefeng.com/wiki/1016959663602400/1017627212385376)

__note__:  
multithreading only use one core of CPU in python. multiprocessing is not.  
considering stability, multiprocessing is better.  
model: Master/Worker  
