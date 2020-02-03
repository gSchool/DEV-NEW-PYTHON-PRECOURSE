# Math 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 5daa1fba-b275-4f89-a5f5-fafd4f9604d1
* title: calculateBillTotal

### !question

Write a function called "calculateBillTotal".

Given the pre tax and pre tip amount of a meal, "calculateBillTotal" returns the total amount due after tax and tip.

Notes:
* Assume that sales tax is 9.5% and tip is 15%.
* Do NOT tip on the sales tax, only on the pre tip amount.

```
output = calculateBillTotal(20)
print(output) # --> 24.9
```

### !end-question

### !placeholder

```python
def calculateBillTotal(preTaxAndTipAmount):
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
        # it should return a number
        self.assertIsInstance(main.calculateBillTotal(20), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the bill total, including tax and tip
        self.assertEqual(main.calculateBillTotal(20), 24.9,
        msg = 'should return the bill total, including tax and tip')


```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
