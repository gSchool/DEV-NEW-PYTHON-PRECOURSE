# Iteration 4

### !challenge

* type: code-snippet
* language: python3.6
* id: cbcdeb30-874c-43d4-bf34-efee529c29d9
* title: computeFactorialOfN

### !question

Write a function called "computeFactorialOfN".

Given a natural number (a whole number greater than 0), "computeFactorialOfN" returns its factorial.

```
output = computeFactorialOfN(3)
print(output) # --> 6

output = computeFactorialOfN(4)
print(output) # --> 24
```

### !end-question

### !placeholder

```python

def computeFactorialOfN(n):
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
        self.assertIsInstance(main.computeFactorialOfN(7), int,
        msg = 'should return an int')


    def test_1(self):
        # it should return the factorial of 'n'
        self.assertEqual(main.computeFactorialOfN(4), 24,
        msg = "should return the factorial of 'n'")


    def test_2(self):
        # it should return the factorial of 1
        self.assertEqual(main.computeFactorialOfN(1), 1,
        msg = 'should return the factorial of 1')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 184175a0-0e1a-4639-9502-825d7e6cc8f3
* title: repeatString

### !question

Write a function called "repeatString".

Given a string and a number, "repeatString" returns the given string repeated the given number of times.

```
output = repeatString('code', 3)
print(output) # --> 'codecodecode'
```

### !end-question

### !placeholder

```python
def repeatString(string, num):
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
        # it should return a string
        self.assertIsInstance(main.repeatString("what", 3), str,
        msg = 'should return a string')


    def test_1(self):
        # it should repeat a string a given number of times
        self.assertEqual(main.repeatString("what", 3), "whatwhatwhat",
        msg = 'should repeat a string a given number of times')


    def test_2(self):
        # it should repeat a string 0 number of times
        self.assertEqual(main.repeatString("what", 0), "",
        msg = 'should repeat a string 0 number of times')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
