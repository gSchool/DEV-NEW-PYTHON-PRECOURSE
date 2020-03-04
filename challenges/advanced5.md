# Advanced 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 0e621f19-ceb1-4565-8f07-e78a7b8a3adb
* title: sum_digits

### !question

Write a function called "sum_digits".

Given an integer, "sum_digits" returns the sum of all its digits.

```
output = sum_digits(1148)
print(output) # --> 14
```

If the number is negative, the first digit should count as negative.

```
output = sum_digits(-316)
print(output) # --> 4
```

### !end-question

### !placeholder

```python
# your code here



```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a number
        self.assertIsInstance(main.sum_digits(2002), int,
        msg = 'should return an int')


    def test_1(self):
        # it should sum the digits of a positive number
        self.assertEqual(main.sum_digits(2002), 4,
        msg = 'should sum the digits of a positive number')


    def test_2(self):
        # it should sum the digits of a negative number
        self.assertEqual(main.sum_digits(-2004), 2,
        msg = 'should sum the digits of a negative number')


    def test_3(self):
        # it should sum return 0 if the number is 0
        self.assertEqual(main.sum_digits(0), 0,
        msg = 'should return 0 if the number is 0')

```

### !end-tests

### !explanation
```python
def sum_digits(number):
    string = str(number)
    
    if number >= 0:
        #positive numbers
        acc = 0
        for char in string:
            acc += int(char)
    else:
        #negative numbers
        acc = -int(string[1])
        for char in (string[2:]):
            acc += int(char)

    return acc

```
### !end-explanation

### !end-challenge
