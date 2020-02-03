# Iteration 4

### !challenge

* type: code-snippet
* language: python3.6
* id: cbcdeb30-874c-43d4-bf34-efee529c29d9
* title: compute_factorial_of_n

### !question

Write a function called "compute_factorial_of_n".

Given a natural number (a whole number greater than 0), "compute_factorial_of_n" returns its factorial.

```
output = compute_factorial_of_n(3)
print(output) # --> 6

output = compute_factorial_of_n(4)
print(output) # --> 24
```

### !end-question

### !placeholder

```python

def compute_factorial_of_n(n):
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
        self.assertIsInstance(main.compute_factorial_of_n(7), int,
        msg = 'should return an int')


    def test_1(self):
        # it should return the factorial of 'n'
        self.assertEqual(main.compute_factorial_of_n(4), 24,
        msg = "should return the factorial of 'n'")


    def test_2(self):
        # it should return the factorial of 1
        self.assertEqual(main.compute_factorial_of_n(1), 1,
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
* title: repeat_string

### !question

Write a function called "repeat_string".

Given a string and a number, "repeat_string" returns the given string repeated the given number of times.

```
output = repeat_string('code', 3)
print(output) # --> 'codecodecode'
```

### !end-question

### !placeholder

```python
def repeat_string(string, num):
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
        self.assertIsInstance(main.repeat_string("what", 3), str,
        msg = 'should return a string')


    def test_1(self):
        # it should repeat a string a given number of times
        self.assertEqual(main.repeat_string("what", 3), "whatwhatwhat",
        msg = 'should repeat a string a given number of times')


    def test_2(self):
        # it should repeat a string 0 number of times
        self.assertEqual(main.repeat_string("what", 0), "",
        msg = 'should repeat a string 0 number of times')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
