# Iteration 3

### !challenge

* type: code-snippet
* language: python3.6
* id: 8c8e3983-9ea7-403f-abaf-4df141fef106
* title: compute_summation_to_n

### !question

Write a function called "compute_summation_to_n".

Given a number, "compute_summation_to_n" returns the sum of sequential numbers leading up to the given number, beginning at 0.

Notes:
* If n = 4, it should calculate the sum of 1 + 2 + 3 + 4, and return 10.

```
output = compute_summation_to_n(6)
print(output) # -> 21  
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
        # it should return an int
        self.assertIsInstance(main.compute_summation_to_n(7), int,
        msg = 'should return a number')


    def test_1(self):
        # it should return the summation of numbers up to and including 'n'
        self.assertEqual(main.compute_summation_to_n(4), 10,
        msg = "should return the summation of numbers up to and including 'n'")


    def test_2(self):
        # it should return the summation of 0
        self.assertEqual(main.compute_summation_to_n(0), 0,
        msg = 'should return the summation of 0')


```

### !end-tests

### !explanation
```python
def compute_summation_to_n(n):
    return sum([x for x in range(n+1)])
```
### !end-explanation

### !end-challenge
