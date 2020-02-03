# Conditionals 3

### !challenge

* type: code-snippet
* language: python3.6
* id: a5f1e64f-3419-4259-9304-ea54969381ca
* title: is_less_than

### !question

Write a function called "is_less_than".
Given 2 numbers, "is_less_than" returns whether num2 is less than num1.

```python
output = is_less_than(9, 4)
print(output) # --> True
```


### !end-question

### !placeholder

```python
def is_less_than(num1, num2):
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
        # it should return a boolean
        self.assertIs(type(main.is_less_than(0,10)), bool, msg="it should return a boolean")

    def test2(self):
        #it should return True when num2 is less than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertTrue(main.is_less_than(num, num - 1), msg="it should return True if num2 is less than num1")

    def test3(self):
        #it should return False when num2 is greater than than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.is_less_than(num, num + 1), msg="it should return False if num2 is greater than num1")

    def test4(self):
        #it should return False if the numbers are equal
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.is_less_than(num, num), msg="it should return False if the numbers are equal")

```

### !end-tests

### !explanation
```python

def is_less_than(num1, num2):
    return num2 < num1

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 4fa4323d-3abd-4206-ba59-91c3df97203f
* title: is_greater_than

### !question

Write a function called "is_greater_than".
Given 2 numbers, "is_greater_than" returns whether num2 is greater than num1.

```python
output = is_greater_than(11, 10)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def is_greater_than(num1, num2):
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
        # it should return a boolean
        self.assertIs(type(main.is_greater_than(0,10)), bool, msg="it should return a boolean")

    def test2(self):
        #it should return True when num2 is greater than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertTrue(main.is_greater_than(num - 1, num), msg="it should return True if num2 is greater than num1")

    def test3(self):
        #it should return False when num2 is less than than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.is_greater_than(num + 1, num), msg="it should return False if num2 is less than num1")

    def test4(self):
        #it should return False if the numbers are equal
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.is_greater_than(num, num), msg="it should return False if the numbers are equal")
```

### !end-tests

### !explanation
```python

def is_greater_than(num1, num2):
    return num2 > num1


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 9d6af24e-85e1-441c-a10c-d629d6381469
* title: is_equal_to

### !question

Write a function called "is_equal_to".
Given 2 numbers, "is_equal_to" returns whether num2 is equal to num1.

```
output = is_equal_to(11, 10)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def is_equal_to(num1, num2):
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
        # it should return a book
        self.assertIs(type(main.is_equal_to(3,4)), bool, msg="it should return a bool")

    def test2(self):
        #it should return True if the numbers are equal
        for num in range(10):
                with self.subTest(num=num):
                    self.assertTrue(main.is_equal_to(num, num),
                    msg="it should return True if the numbers are equal")

    def test3(self):
        #it should return False if the numbers are not equal
        for num1 in range(1,20,2): #odd
            for num2 in range(0,20,2): #even
                with self.subTest(num1=num1, num2=num2):
                    self.assertFalse(main.is_equal_to(num1, num2),
                    msg="it should return False if the numbers are not equal")
```

### !end-tests

### !explanation
```python

def is_equal_to(num1, num2):
    return num1 == num2


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 32135330-a5c2-49cd-b9a4-cffe41db64b3
* title: is_even

### !question

Write a function called "is_even".
Given a number, "is_even" returns whether it is even.

```
output = is_even(11)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def is_even(num):
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
        # it should
        self.assertIs(type(main.is_even(8)), bool,
        msg="it should return a bool")

    def test2(self):
        #it should return True if number is even
        for num in range(0,10,2):
                with self.subTest(num=num):
                    self.assertTrue(main.is_even(num),
                    msg="it should return True if the number is even")

    def test3(self):
        ##it should return False if number is not even
        for num in range(1,11,2):
                with self.subTest(num=num):
                    self.assertFalse(main.is_even(num),
                    msg="it should return False if the number is not even")

```

### !end-tests

### !explanation
```python

def is_even(num):
    return num % 2 == 0


```
### !end-explanation

### !end-challenge
