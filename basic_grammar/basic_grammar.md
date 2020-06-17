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
    - [introduction](#introduction)

- function

- iterator

- generator

- decorator

- module and package

- Exception

- file read and write

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
to 'aaa'.

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

### introduction
