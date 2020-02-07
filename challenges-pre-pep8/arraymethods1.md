# Array Methods 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 95a46849-2478-44f2-8783-0729dd17eaae
* title: getNthElement

### !question

Write a function called "getNthElement".

Given an array and an integer, "getNthElement" returns the element at the given integer index, within the given array.

Notes:
* Remember, arrays in Python begin counting at element with index 0.
* If the array has a length of 0, it should return 'None'.


```
output = getNthElement([1, 3, 5], 1)
print(output) # --> 3
```

### !end-question

### !placeholder

```python
def getNthElement(array, n):
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
        # it should return None if the array is Empty
        self.assertIs(main.getNthElement([], 3), None,
        msg = "it should return None if the array is Empty" )

    def test2(self):
        #it should return the nth element of an array
        self.assertEqual(main.getNthElement([10,12,14,16], 3), 16,
        msg = "it should return the nth element of an array" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 7c720b84-05ae-44b5-ab40-5ef78db09bec
* title: getFirstElement

### !question

Write a function called "getFirstElement".

Given an array, "getFirstElement" returns the first element of the given array.

Notes:
* If the given array has a length of 0, it should return None.

```
output = getFirstElement([1, 2, 3, 4, 5])
print(output) # --> 1
```

### !end-question

### !placeholder

```python
def getFirstElement(array):
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
        # it should return None if the array is Empty
        self.assertIs(main.getFirstElement([]), None,
        msg = "it should return None if the array is Empty" )

    def test2(self):
        #it should return the first element of an array
        self.assertEqual(main.getFirstElement([-99, 99, 0]), -99,
        msg = "it should return the first element of an array" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: d89ba6ec-9149-4147-b78e-d449659e0661
* title: getLastElement

### !question

Write a function called "getLastElement".

Given an array, "getLastElement" returns the last element of the given array.

Notes:
* If the given array has a length of 0, it should return 'undefined'.

```
output = getLastElement([1, 2, 3, 4])
print(output) # --> 4
```

### !end-question

### !placeholder

```python
def getLastElement(array):
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
        # it should return None if the array is Empty
        self.assertIs(main.getLastElement([]), None,
        msg = "it should return None if the array is Empty" )

    def test2(self):
        #it should return the last element of an array
        self.assertEqual(main.getLastElement([-99, 99, 10]), 10,
        msg = "it should return the last element of an array" )

```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
