# List Methods 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 95a46849-2478-44f2-8783-0729dd17eaae
* title: get_nth_element

### !question

Write a function called "get_nth_element".

Given a list and an integer, "get_nth_element" returns the element at the given integer index, within the given list.

Notes:
* Remember, arrays in Python begin counting at element with index 0.
* If the array has a length of 0, it should return 'None'.


```
output = get_nth_element([1, 3, 5], 1)
print(output) # --> 3
```

### !end-question

### !placeholder

```python
def get_nth_element(lst, n):
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
        self.assertIs(main.get_nth_element([], 3), None,
        msg = "it should return None if the array is Empty" )

    def test2(self):
        #it should return the nth element of a list
        self.assertEqual(main.get_nth_element([10,12,14,16], 3), 16,
        msg = "it should return the nth element of a list" )

```

### !end-tests

### !explanation
```python
def get_nth_element(lst, n):
    if len(lst):
        return lst[n]
    else:
        return None
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 7c720b84-05ae-44b5-ab40-5ef78db09bec
* title: get_first_element

### !question

Write a function called "get_first_element".

Given a list, "get_first_element" returns the first element of the given array.

Notes:
* If the given array has a length of 0, it should return None.

```
output = get_first_element([1, 2, 3, 4, 5])
print(output) # --> 1
```

### !end-question

### !placeholder

```python
def get_first_element(array):
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
        self.assertIs(main.get_first_element([]), None,
        msg = "it should return None if the array is Empty" )

    def test2(self):
        #it should return the first element of a list
        self.assertEqual(main.get_first_element([-99, 99, 0]), -99,
        msg = "it should return the first element of a list" )

```

### !end-tests

### !explanation
```python
def get_first_element(lst):
    if len(lst):
        return lst[0]
    else:
        return None
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: d89ba6ec-9149-4147-b78e-d449659e0661
* title: get_last_element

### !question

Write a function called "get_last_element".

Given a list, "get_last_element" returns the last element of the given array.

Notes:
* If the given array has a length of 0, it should return None.

```
output = get_last_element([1, 2, 3, 4])
print(output) # --> 4
```

### !end-question

### !placeholder

```python
def get_last_element(array):
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
        self.assertIs(main.get_last_element([]), None,
        msg = "it should return None if the array is Empty" )

    def test2(self):
        #it should return the last element of a list
        self.assertEqual(main.get_last_element([-99, 99, 10]), 10,
        msg = "it should return the last element of a list" )

```


### !end-tests

### !explanation
```python
def get_last_element(lst):
    if len(lst):
        return lst[-1]
    else:
        return None
```
### !end-explanation

### !end-challenge
