# Conditionals 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 3a5dfe0d-e0ea-49b3-a9b1-d7e973f03133
* title: check_age

### !question

Write a function called "check_age".
Given a person's name and age, "check_age" returns one of two messages:
"Go home, :insert_name_here!", if they are younger than 21.
"Welcome, :insert_name_here!", if they are 21 or older.
Naturally, replace ":insert_name_here" with the given name. :)

```
output = check_age('Adrian', 22)
print(output) # --> 'Welcome, Adrian!'
```

### !end-question

### !placeholder

```python
def check_age(name, age):
    # your code here
    pass



```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should  return a string
        self.assertIs(type(main.check_age("Dan",24)),str,"it should return a string")

    def test2(self):
        #it should welcome someone over 21
        self.assertEqual(main.check_age("Dan",24), "Welcome, Dan!",
        "it should welcome someone over 21")

    def test3(self):
        self.assertEqual(main.check_age("Toni",21), "Welcome, Toni!",
        "it should welcome a 21 year old")

    def test4(self):
        #it should bounce someone under 21
        self.assertEqual(main.check_age("Rad",4), "Go home, Rad!",
        "it should bounce someone under 21")
```

### !end-tests

### !explanation
```python
def check_age(name, age):
    if age >= 21:
        return f'Welcome, {name}!'
    else:
        return f'Go home, {name}!'


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 9f1f81f6-8067-40a8-82ce-c9de9c13bcae
* title: is_greater_than_ten

### !question

Write a function called "isGreaterThan10".
Given a number, "isGreaterThan10" returns whether the given number is greater than 10.

```
output = isGreaterThan10(11)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isGreaterThan10(num):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return a bool
        self.assertIs(type(main.isGreaterThan10(40)),bool,"it should return a bool")

    def test2(self):
        #it should return False for a number less than 10
        self.assertFalse(main.isGreaterThan10(4), "it should return False for a number less than 10")

    def test3(self):
        #it should return True for a number greater than 10
        self.assertTrue(main.isGreaterThan10(40),"it should return True for a number greater than 10")

    def test4(self):
        #it should return False for the number 10
        self.assertFalse(main.isGreaterThan10(10),"it should return False for the number 10")
```

### !end-tests

### !explanation
```python
def isGreaterThan10(num):
    return num > 10

```
### !end-explanation

### !end-challenge


### !challenge

* type: code-snippet
* language: python3.6
* id: 49586ccf-27da-4265-abb8-7ba92a2202cc
* title: is_less_than30

### !question

Write a function called "is_less_than30".
Given a number, "is_less_than30" returns whether the given number is less than 30.

```
output = is_less_than30(9)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def is_less_than30(num):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return a boolean
        self.assertIs(type(main.is_less_than30(40)), bool, "it should return a boolean")

    def test2(self):
        #it should return True for a number less than 30
        self.assertTrue(main.is_less_than30(10), "it should return True for  a number less than 30")

    def test3(self):
        #it should return False for a number greater than 30
        self.assertFalse(main.is_less_than30(40), "it should return False for a number greater than 30")

    def test4(self):
        #it should return False for the number 30
        self.assertFalse(main.is_less_than30(30), "it should return False for the number 30")
```


### !end-tests

### !explanation
```python

def is_less_than30(num):
    return num < 30


```

### !end-explanation

### !end-challenge


### !challenge

* type: code-snippet
* language: python3.6
* id: 1fa21321-c02b-43c3-b6b9-0bf633486f6f
* title: equals_ten

### !question

Write a function called "equals_ten".
Given a number, "equals_ten" returns whether or not the given number is 10.

```python
output = equals_ten(9)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def equals_ten(num):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return a boolean
        self.assertIs(type(main.equals_ten(40)), bool, "it should return a boolean")

    def test2(self):
        #it should return False for a number less than 10
        self.assertFalse(main.equals_ten(0), "it should return False for a number less than 10")

    def test3(self):
        #it should return False for a number greater than 10
        self.assertFalse(main.equals_ten(11), "it should return False for a number greater than 10")

    def test4(self):
        #it should return True for the number 10
        self.assertTrue(main.equals_ten(10), "it should return True for the number 10")

```


### !end-tests

### !explanation
```python

def equals_ten(num):
    return num == 10


```
### !end-explanation

### !end-challenge
