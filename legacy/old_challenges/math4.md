# Math 4

### !challenge

* type: code-snippet
* language: python3.6
* id: bf41eed3-a9de-4e31-9750-a645da0ab576
* title: computePower

### !question

Write a function called "computePower".

Given a number and an exponent, "computePower" returns the given number, raised to the given exponent.

```
output = computePower(2, 3)
print(output) # --> 8
```

### !end-question

### !placeholder

```python
def computePower(num, exponent):
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
        # "it should return a positive number raised to a given exponent"
        self.assertEqual(main.computePower(2, 4), 16,
        msg = "it should return a positive number raised to a given exponent" )

    def test2(self):
        # "it should return a negative number raised to a given exponent"
        self.assertEqual(main.computePower(-2, 4), 16,
        msg = "it should return a negative number raised to a given exponent" )

    def test3(self):
        # "it should return a number raised to a zero exponent"
        self.assertEqual(main.computePower(2, 0), 1,
        msg = "it should return a number raised to a zero exponent" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: d6959c6e-7921-4f3d-9b44-947c99fab887
* title: computeSquareRoot

### !question

Write a function called "computeSquareRoot".
Given a number, "computeSquareRoot" returns its square root.

```
output = computeSquareRoot(9)
print(output) # --> 3
```

### !end-question

### !placeholder

```python
import math

def computeSquareRoot(num):
    # your code here
    pass

```

### !end-placeholder

### !tests

```python
import main
import unittest
import math

class TestScript(unittest.TestCase):
    def test1(self):
        # "it should return the square root of a number"
        self.assertEqual(main.computeSquareRoot(16), 4,
        msg = "it should return the square root of a number" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e5a953a0-42f3-414c-bd77-c4247d272f7a
* title: doubleSquareRootOf

### !question

Write a function called "doubleSquareRootOf".
Given a number, "doubleSquareRootOf" returns double its square root.

```
output = doubleSquareRootOf(121)
print(output) # --> 22
```

### !end-question

### !placeholder

```python
import math
def doubleSquareRootOf(num):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest
import math

class TestScript(unittest.TestCase):
    def test1(self):
        # it
        self.assertEqual(main.doubleSquareRootOf(121), 22,
        msg = "it should return the doubled square root of the passed in number" )


```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
