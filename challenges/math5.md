# Math 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 5daa1fba-b275-4f89-a5f5-fafd4f9604d1
* title: calculate_bill_total

### !question

Write a function called "calculate_bill_total".

Given the amount of a meal before tax and tip, "calculate_bill_total" returns the total amount due after tax and tip.

Notes:
* Assume that sales tax is 9.5% and tip is 15%.
* Do NOT tip on the sales tax, only on the given amount.

```
output = calculate_bill_total(20)
print(output) # --> 24.9
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
        self.assertIsInstance(main.calculate_bill_total(20), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the bill total, including tax and tip
        self.assertEqual(main.calculate_bill_total(20), 24.9,
        msg = 'should return the bill total, including tax and tip')


```
### !end-tests

### !explanation
```python
def calculate_bill_total(amount):
    tax = 0.095
    tip = 0.15
    return amount*(1+tax+tip)


```
### !end-explanation

### !end-challenge
