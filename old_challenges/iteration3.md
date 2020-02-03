# Iteration 3

### !challenge

* type: code-snippet
* language: python3.6
* id: 8c8e3983-9ea7-403f-abaf-4df141fef106
* title: computeSummationToN

### !question

Write a function called "computeSummationToN".

Given a number, "computeSummationToN" returns the sum of sequential numbers leading up to the given number, beginning at 0.

Notes:
* If n = 4, it should calculate the sum of 1 + 2 + 3 + 4, and return 10.

```
output = computeSummationToN(6)
print(output) # -> 21  
```

### !end-question

### !placeholder

```python
def computeSummationToN(n):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return an int
        self.assertIsInstance(main.computeSummationToN(7), int,
        msg = 'should return a number')


    def test_1(self):
        # it should return the summation of numbers up to and including 'n'
        self.assertEqual(main.computeSummationToN(4), 10,
        msg = "should return the summation of numbers up to and including 'n'")


    def test_2(self):
        # it should return the summation of 0
        self.assertEqual(main.computeSummationToN(0), 0,
        msg = 'should return the summation of 0')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
