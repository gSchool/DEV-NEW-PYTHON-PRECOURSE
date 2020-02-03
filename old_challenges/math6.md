# Math 6

### !challenge

* type: code-snippet
* language: python3.6
* id: 2cbdc32a-d1bb-4538-9dcb-eb64072cae56
* title: computeCompoundInterest

### !question

Write a function called "computeCompoundInterest".

Given a principal, an interest rate, a compounding frequency, and a time (in years), "computeCompoundInterest" returns the amount of compound interest generated.

```
output = computeCompoundInterest(1500, 0.043, 4, 6)
print(output) # --> 438.8368221341061
```

Reference:
(Compound_interest)[https://en.wikipedia.org/wiki/Compound_interest#Calculation_of_compound_interest]
This shows the formula used to calculate the total compound interest generated.

### !end-question

### !placeholder

```python

def computeCompoundInterest(principal, interestRate, compoundingFrequency, timeInYears):
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
        self.assertIsInstance(main.computeCompoundInterest(1500, .043, 4, 6), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the amount of compound interest generated
        self.assertAlmostEqual(main.computeCompoundInterest(1500, .043, 4, 6), 438.8368221341061, places=2,
        msg = 'should return the amount of compound interest generated')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
