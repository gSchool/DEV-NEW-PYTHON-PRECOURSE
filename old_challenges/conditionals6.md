# Conditionals 6

### !challenge

* type: code-snippet
* language: python3.6
* id: 17849d44-37ff-4fde-a81f-884838cdb8f5
* title: or

### !question

Write a function called "special_or".

Given 2 boolean expressions, "special_or" returns True or False, corresponding to the 'or' operator.
Notes:
* Do not use the or operator.
* Use 'not' and 'and' operators instead.

```
output = special_or(True, False)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def special_or(expression1, expression2):
    # your code here
    pass
```

### !end-placeholder

### !tests

```python
import main
import unittest
import inspect
import re

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should not use the logical OR operator
        source = inspect.getsource(main.special_or)
        self.assertIsNone(re.search(r'\bor\b', source),
        msg = 'should not contain the word "or" anywhere in function body ')


    def test_1(self):
        # it should return a boolean
        self.assertIsInstance(main.special_or(True, False), bool,
        msg = 'should return a bool')


    def test_2(self):
        # it should return True if the first value is True
        self.assertTrue(main.special_or(True, False),
        msg = 'should return True if the first value is True')


    def test_3(self):
        # it should return True if the second value is True
        self.assertTrue(main.special_or(False, True),
        msg = 'should return True if the second value is True')


    def test_4(self):
        # it 'should return False if both values are False'
        self.assertFalse(main.special_or(False, False),
        msg = 'should return False if both values are False')

    def test_5(self):
        # it should return True if both values are True
        self.assertTrue(main.special_or(True, True),
        msg = 'should return True if both values are True')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 1f440059-2dd7-472c-8106-c56fa9f75029
* title: isEitherEvenOrAreBoth7

### !question

Write a function called "isEitherEvenOrAreBoth7".

Given two numbers, 'isEitherEvenOrAreBoth7' returns whether at least one of them is even, or, both of them are 7.

```
output = isEitherEvenOrAreBoth7(3, 7)
print(output) # --> False

output = isEitherEvenOrAreBoth7(2, 3)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isEitherEvenOrAreBoth7(num1, num2):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):


    def test_1(self):
        # it should return a boolean
        self.assertIsInstance(main.isEitherEvenOrAreBoth7(7, 7), bool,
        msg = 'should return a bool')


    def test_2(self):
        # it "should return True if the first number is even"
        self.assertTrue(main.isEitherEvenOrAreBoth7(10, -1),
        msg = "should return True if the first number is even")


    def test_3(self):
        # it "should return True if the second number is even"
        self.assertTrue(main.isEitherEvenOrAreBoth7(-9, 8),
        msg = "should return True if the second number is even")


    def test_4(self):
        # it "should return True if the both numbers are even"
        self.assertTrue(main.isEitherEvenOrAreBoth7(1000, 50),
        msg = "should return True if both numbers are even")

    def test_5(self):
        # it "should return True if the both numbers are 7"
        self.assertTrue(main.isEitherEvenOrAreBoth7(7, 7),
        msg = "should return True if both numbers are 7")

    def test_6(self):
        # it "should return False if the both numbers are odd and not both 7"
        self.assertFalse(main.isEitherEvenOrAreBoth7(3, 7),
        msg = "should return False if the both numbers are odd and not both 7")            
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 45e91a10-4d74-4f10-83ef-b7b065d45830
* title: isEitherEvenAndLessThan9

### !question

Write a function called "isEitherEvenAndLessThan9".

Given two numbers, 'isEitherEvenAndLessThan9' returns whether at least one of them is even AND both of them are less than 9.

```
output = isEitherEvenAndLessThan9(2, 4)
print(output) # --> True

output = isEitherEvenAndLessThan9(72, 2)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def isEitherEvenAndLessThan9(num1, num2):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_1(self):
        # it should return a boolean
        self.assertIsInstance(main.isEitherEvenAndLessThan9(6, 99), bool,
        msg = 'should return a boolean')


    def test_2(self):
        # it "should return True if the first number is even and both are less than 9"
        self.assertTrue(main.isEitherEvenAndLessThan9(4, 3),
        msg = "should return True if the first number is even and both are less than 9")


    def test_3(self):
        # it "should return True if the second number is even and both are less than 9"
        self.assertTrue(main.isEitherEvenAndLessThan9(7, 8),
        msg = "should return True if the second number is even and both are less than 9")


    def test_4(self):
        # it "should return True if the both numbers are even and both are less than 9"
        self.assertTrue(main.isEitherEvenAndLessThan9(2, 4),
        msg = "should return True if the both numbers are even and both are less than 9")

    def test_5(self):
        # it "should return False if the both numbers are greater than 9"
        self.assertFalse(main.isEitherEvenAndLessThan9(12,14),
        msg = "should return False if the both numbers are greater than 9")

    def test_6(self):
        # it "should return False if the left number is greater than 9"
        self.assertFalse(main.isEitherEvenAndLessThan9(222, 8),
        msg = "should return False if the left number is greater than 9")

    def test_6(self):
        # it "should return False if the right number is greater than 9"
        self.assertFalse(main.isEitherEvenAndLessThan9(4,221),
        msg = "should return False if the right number is greater than 9")    

    def test_7(self):
        # it "should return False if neither number is even"
        self.assertFalse(main.isEitherEvenAndLessThan9(-3,-1),
        msg = "should return False if neither number is even")
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
