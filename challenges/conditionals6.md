# Conditionals 6

### !challenge

* type: code-snippet
* language: python3.6
* id: 1f440059-2dd7-472c-8106-c56fa9f75029
* title: is_either_even_or_are_both_7

### !question

Write a function called "is_either_even_or_are_both_7".

Given two numbers, 'is_either_even_or_are_both_7' returns whether at least one of them is even, or, both of them are 7.

```
output = is_either_even_or_are_both_7(3, 7)
print(output) # --> False

output2 = is_either_even_or_are_both_7(2, 3)
print(output2) # --> True

output3 = is_either_even_or_are_both_7(7, 7)
print(output3) # --> True
```

### !end-question

### !placeholder

```python
def is_either_even_or_are_both_7(num1, num2):
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
        self.assertIsInstance(main.is_either_even_or_are_both_7(7, 7), bool,
        msg = 'should return a bool')


    def test_2(self):
        # it "should return True if the first number is even"
        self.assertTrue(main.is_either_even_or_are_both_7(10, -1),
        msg = "should return True if the first number is even")


    def test_3(self):
        # it "should return True if the second number is even"
        self.assertTrue(main.is_either_even_or_are_both_7(-9, 8),
        msg = "should return True if the second number is even")


    def test_4(self):
        # it "should return True if the both numbers are even"
        self.assertTrue(main.is_either_even_or_are_both_7(1000, 50),
        msg = "should return True if both numbers are even")

    def test_5(self):
        # it "should return True if the both numbers are 7"
        self.assertTrue(main.is_either_even_or_are_both_7(7, 7),
        msg = "should return True if both numbers are 7")

    def test_6(self):
        # it "should return False if the both numbers are odd and not both 7"
        self.assertFalse(main.is_either_even_or_are_both_7(3, 7),
        msg = "should return False if the both numbers are odd and not both 7")            
```

### !end-tests

### !explanation
```python
def is_either_even_or_are_both_7(num1, num2):
    return num1 % 2 == 0 or num2 % 2 == 0 or (num1 == 7 and num2 == 7)
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 45e91a10-4d74-4f10-83ef-b7b065d45830
* title: is_either_even_and_both_less_than_9

### !question

Write a function called "is_either_even_and_both_less_than_9".

Given two numbers, 'is_either_even_and_both_less_than_9' returns whether at least one of them is even AND both of them are less than 9.

```
output = is_either_even_and_both_less_than_9(2, 4)
print(output) # --> True

output = is_either_even_and_both_less_than_9(72, 2)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def is_either_even_and_both_less_than_9(num1, num2):
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
        self.assertIsInstance(main.is_either_even_and_both_less_than_9(6, 99), bool,
        msg = 'should return a boolean')


    def test_2(self):
        # it "should return True if the first number is even and both are less than 9"
        self.assertTrue(main.is_either_even_and_both_less_than_9(4, 3),
        msg = "should return True if the first number is even and both are less than 9")


    def test_3(self):
        # it "should return True if the second number is even and both are less than 9"
        self.assertTrue(main.is_either_even_and_both_less_than_9(7, 8),
        msg = "should return True if the second number is even and both are less than 9")


    def test_4(self):
        # it "should return True if the both numbers are even and both are less than 9"
        self.assertTrue(main.is_either_even_and_both_less_than_9(2, 4),
        msg = "should return True if the both numbers are even and both are less than 9")

    def test_5(self):
        # it "should return False if the both numbers are greater than 9"
        self.assertFalse(main.is_either_even_and_both_less_than_9(12,14),
        msg = "should return False if the both numbers are greater than 9")

    def test_6(self):
        # it "should return False if the left number is greater than 9"
        self.assertFalse(main.is_either_even_and_both_less_than_9(222, 8),
        msg = "should return False if the left number is greater than 9")

    def test_6(self):
        # it "should return False if the right number is greater than 9"
        self.assertFalse(main.is_either_even_and_both_less_than_9(4,221),
        msg = "should return False if the right number is greater than 9")    

    def test_7(self):
        # it "should return False if neither number is even"
        self.assertFalse(main.is_either_even_and_both_less_than_9(-3,-1),
        msg = "should return False if neither number is even")
```

### !end-tests

### !explanation
```python
def is_either_even_and_both_less_than_9(num1, num2):
    return (num1 % 2 == 0 or num2 % 2 == 0) and (num1 < 9 and num2 < 9)
```
### !end-explanation

### !end-challenge
