# Conditionals 3

### !challenge

* type: code-snippet
* language: python3.6
* id: a5f1e64f-3419-4259-9304-ea54969381ca
* title: isLessThan

### !question

Write a function called "isLessThan".
Given 2 numbers, "isLessThan" returns whether num2 is less than num1.

```python
output = isLessThan(9, 4)
print(output) # --> True
```


### !end-question

### !placeholder

```python
def isLessThan(num1, num2):
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
        self.assertIs(type(main.isLessThan(0,10)), bool, msg="it should return a boolean")

    def test2(self):
        #it should return True when num2 is less than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertTrue(main.isLessThan(num, num - 1), msg="it should return True if num2 is less than num1")

    def test3(self):
        #it should return False when num2 is greater than than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.isLessThan(num, num + 1), msg="it should return False if num2 is greater than num1")

    def test4(self):
        #it should return False if the numbers are equal
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.isLessThan(num, num), msg="it should return False if the numbers are equal")

```

### !end-tests

### !explanation
```python

def isLessThan(num1, num2):
    return num2 < num1

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 4fa4323d-3abd-4206-ba59-91c3df97203f
* title: isGreaterThan

### !question

Write a function called "isGreaterThan".
Given 2 numbers, "isGreaterThan" returns whether num2 is greater than num1.

```python
output = isGreaterThan(11, 10)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def isGreaterThan(num1, num2):
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
        self.assertIs(type(main.isGreaterThan(0,10)), bool, msg="it should return a boolean")

    def test2(self):
        #it should return True when num2 is greater than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertTrue(main.isGreaterThan(num - 1, num), msg="it should return True if num2 is greater than num1")

    def test3(self):
        #it should return False when num2 is less than than num1
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.isGreaterThan(num + 1, num), msg="it should return False if num2 is less than num1")

    def test4(self):
        #it should return False if the numbers are equal
        for num in range(10):
                with self.subTest(num=num):
                    self.assertFalse(main.isGreaterThan(num, num), msg="it should return False if the numbers are equal")
```

### !end-tests

### !explanation
```python

def isGreaterThan(num1, num2):
    return num2 > num1


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 9d6af24e-85e1-441c-a10c-d629d6381469
* title: isEqualTo

### !question

Write a function called "isEqualTo".
Given 2 numbers, "isEqualTo" returns whether num2 is equal to num1.

```
output = isEqualTo(11, 10)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def isEqualTo(num1, num2):
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
        self.assertIs(type(main.isEqualTo(3,4)), bool, msg="it should return a bool")

    def test2(self):
        #it should return True if the numbers are equal
        for num in range(10):
                with self.subTest(num=num):
                    self.assertTrue(main.isEqualTo(num, num),
                    msg="it should return True if the numbers are equal")

    def test3(self):
        #it should return False if the numbers are not equal
        for num1 in range(1,20,2): #odd
            for num2 in range(0,20,2): #even
                with self.subTest(num1=num1, num2=num2):
                    self.assertFalse(main.isEqualTo(num1, num2),
                    msg="it should return False if the numbers are not equal")
```

### !end-tests

### !explanation
```python

def isEqualTo(num1, num2):
    return num1 == num2


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 32135330-a5c2-49cd-b9a4-cffe41db64b3
* title: isEven

### !question

Write a function called "isEven".
Given a number, "isEven" returns whether it is even.

```
output = isEven(11)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def isEven(num):
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
        self.assertIs(type(main.isEven(8)), bool,
        msg="it should return a bool")

    def test2(self):
        #it should return True if number is even
        for num in range(0,10,2):
                with self.subTest(num=num):
                    self.assertTrue(main.isEven(num),
                    msg="it should return True if the number is even")

    def test3(self):
        ##it should return False if number is not even
        for num in range(1,11,2):
                with self.subTest(num=num):
                    self.assertFalse(main.isEven(num),
                    msg="it should return False if the number is not even")

```

### !end-tests

### !explanation
```python

def isEven(num):
    return num % 2 == 0


```
### !end-explanation

### !end-challenge
