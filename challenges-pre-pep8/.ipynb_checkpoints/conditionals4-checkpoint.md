# Conditionals 4

### !challenge

* type: code-snippet
* language: python3.6
* id: c13afed5-de19-458a-a3b9-65fc3d34f842
* title: isOdd

### !question

Write a function called "isOdd".
Given a number, "isOdd" returns whether the given number is odd.

```
output = isOdd(9)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isOdd(num):
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
        # "it should return a bool"
        self.assertIs(type(main.isOdd(8)), bool,
        msg="it should return a bool")

    def test2(self):
        #it should return True if number is odd
        for num in range(1,11,2):
                with self.subTest(num=num):
                    self.assertTrue(main.isOdd(num),
                    msg="it should return True if the number is odd")

    def test3(self):
        ##it should return False if number is not odd
        for num in range(0,10,2):
                with self.subTest(num=num):
                    self.assertFalse(main.isOdd(num),
                    msg="it should return False if the number is not odd")
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: d502830a-6d86-479d-9bd3-664e13d2a686
* title: isSameLength

### !question

Write a function called "isSameLength".

Given two words, "isSameLength" returns whether the given words have the same length.

```
output = isSameLength('words', 'super')
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isSameLength(word1, word2):
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
        self.assertIs(type(main.isSameLength("book", "books")), bool, msg="it should return a bool")

    def test2(self):
        #it "should return True if the two words are the same length"
        self.assertTrue(main.isSameLength("yes", "you"), msg="should return True if the two words are the same length")

    def test3(self):
        #it should return False if the two words are not the same length
        self.assertFalse(main.isSameLength("book","books"), msg="it should return False if the two words are not the same length")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 2b052832-2dec-494d-9a24-090c8051db0a
* title: areBothOdd

### !question

Write a function called "areBothOdd".

Given 2 numbers, "areBothOdd" returns whether or not both of the given numbers are odd.

```
output = areBothOdd(1, 3)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def areBothOdd(num1, num2):
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
        # it "should return a boolean"
        self.assertIs(type(main.areBothOdd(6, 7)), bool, msg = "should return a boolean")

    def test2(self):
        #it "should return True if both numbers are odd"
        self.assertTrue(main.areBothOdd(7, 99), msg = "should return True if both numbers are odd")

    def test3(self):
        #it "should return False if the first number is even"
        self.assertFalse(main.areBothOdd(4, 7), msg = "should return False if the first number is even")

    def test4(self):
        #it "should return False if the second number is even"
        self.assertFalse(main.areBothOdd(71, 88), msg = "should return False if the second number is even")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 2aa4cdd8-0158-438d-8a53-b9c0283226c7
* title: isEitherEven

### !question

Write a function called "isEitherEven".

Given two numbers, "isEitherEven" returns whether or not either one of the given numbers is even.

```
output = isEitherEven(1, 4)
print(output) # --> True
```

### !end-question

### !placeholder

```python
def isEitherEven(num1, num2):
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
        # it "should return a boolean"
        self.assertIs(type(main.isEitherEven(6, 7)), bool, msg = "should return a boolean")

    def test2(self):
        #it "should return False if both numbers are odd"
        self.assertFalse(main.isEitherEven(17, 49), msg = "should return False if both numbers are odd")

    def test3(self):
        #it "should return True if the first number is even"
        self.assertTrue(main.isEitherEven(4, 7), msg = "should return True if the first number is even")

    def test4(self):
        #it "should return True if the second number is even"
        self.assertTrue(main.isEitherEven(71, 88), msg = "should return True if the second number is even")

```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
