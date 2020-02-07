# Conditionals 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 3a5dfe0d-e0ea-49b3-a9b1-d7e973f03133
* title: checkAge

### !question

Write a function called "checkAge".
Given a person's name and age, "checkAge" returns one of two messages:
"Go home, :insert_name_here!", if they are younger than 21.
"Welcome, :insert_name_here!", if they are 21 or older.
Naturally, replace ":insert_name_here" with the given name. :)

```
output = checkAge('Adrian', 22)
print(output) # --> 'Welcome, Adrian!'
```

### !end-question

### !placeholder

```python
def checkAge(name, age):
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
        self.assertIs(type(main.checkAge("Dan",24)),str,"it should return a string")

    def test2(self):
        #it should welcome someone over 21
        self.assertEqual(main.checkAge("Dan",24), "Welcome, Dan!",
        "it should welcome someone over 21")

    def test3(self):
        self.assertEqual(main.checkAge("Toni",21), "Welcome, Toni!",
        "it should welcome a 21 year old")

    def test4(self):
        #it should bounce someone under 21
        self.assertEqual(main.checkAge("Rad",4), "Go home, Rad!",
        "it should bounce someone under 21")
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 9f1f81f6-8067-40a8-82ce-c9de9c13bcae
* title: isGreaterThanTen

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

### !end-explanation

### !end-challenge


### !challenge

* type: code-snippet
* language: python3.6
* id: 49586ccf-27da-4265-abb8-7ba92a2202cc
* title: isLessThan30

### !question

Write a function called "isLessThan30".
Given a number, "isLessThan30" returns whether the given number is less than 30.

```
output = isLessThan30(9)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isLessThan30(num):
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
        self.assertIs(type(main.isLessThan30(40)), bool, "it should return a boolean")

    def test2(self):
        #it should return True for a number less than 30
        self.assertTrue(main.isLessThan30(10), "it should return True for  a number less than 30")

    def test3(self):
        #it should return False for a number greater than 30
        self.assertFalse(main.isLessThan30(40), "it should return False for a number greater than 30")

    def test4(self):
        #it should return False for the number 30
        self.assertFalse(main.isLessThan30(30), "it should return False for the number 30")
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge


### !challenge

* type: code-snippet
* language: python3.6
* id: 1fa21321-c02b-43c3-b6b9-0bf633486f6f
* title: equalsTen

### !question

Write a function called "equalsTen".
Given a number, "equalsTen" returns whether or not the given number is 10.

```python
output = equalsTen(9)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def equalsTen(num):
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
        self.assertIs(type(main.equalsTen(40)), bool, "it should return a boolean")

    def test2(self):
        #it should return False for a number less than 10
        self.assertFalse(main.equalsTen(0), "it should return False for a number less than 10")

    def test3(self):
        #it should return False for a number greater than 10
        self.assertFalse(main.equalsTen(11), "it should return False for a number greater than 10")

    def test4(self):
        #it should return True for the number 10
        self.assertTrue(main.equalsTen(10), "it should return True for the number 10")

```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
