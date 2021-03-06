# List Methods 10

### !challenge

* type: code-snippet
* language: python3.6
* id: 89972114-2f9f-47da-aae3-8df266ff32b7
* title: square_elements

### !question

Write a function called "square_elements".
Given a list of numbers, "square_elements" should return a new list where each element is the square of the element of the given list.
```
output = square_elements([1, 2, 3])
print(output) # --> [1, 4, 9]
```

### !end-question

### !placeholder

```python
# your code here



```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a list
        self.assertIsInstance(main.square_elements([1, 2, 3]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with the elements of the passed in list, squared
        self.assertEqual(main.square_elements([10, 20, 30]), [100, 400, 900],
        msg = 'should return a list with the elements of the passed in list, squared')

```

### !end-tests

### !explanation
```python
def square_elements(lst):
    return [x*x for x in lst]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bc26b616-3099-4e47-ad75-5670968a8ed1
* title: filter_odd_elements

### !question

Write a function called "filter_odd_elements".

Given a list of numbers, "filter_odd_elements" returns a list containing only the odd numbers of the given list.
```
output = filter_odd_elements([1, 2, 3, 4, 5])
print(output) # --> [1, 3, 5]
```

### !end-question

### !placeholder

```python

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a list
        self.assertIsInstance(main.filter_odd_elements([1, 2, 3, 4]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with the odd elements from the passed in list
        self.assertEqual(main.filter_odd_elements([1, 2, 3, 4, 5]), [1, 3, 5],
        msg = 'should return a list with the odd elements from the passed in list')


    def test_2(self):
        # it should return a list if there are no odd numbers
        self.assertEqual(main.filter_odd_elements([2, 4, 6]), [],
        msg = 'should return a list if there are no odd numbers')


    def test_3(self):
        # it should return a list if given an empty list
        self.assertEqual(main.filter_odd_elements([]), [],
        msg = 'should return a list if given an empty list')

```

### !end-tests

### !explanation
```python
def filter_odd_elements(lst):
    return [x for x in lst if x % 2 == 1]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e2f51369-1a84-42dc-8613-2ccd23f46bc2
* title: compute_product_of_all_elements

### !question

Write a function called "compute_product_of_all_elements".

Given a list of numbers, "compute_product_of_all_elements" returns the products of all the elements in the given list.

Notes:
* If given list is empty, it should return 0.
* If the list contains strings, it should return -1.

```
output = compute_product_of_all_elements([2, 5, 6])
print(output) # --> 60
```

### !end-question

### !placeholder

```python
# your code here


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return a number
        self.assertIsInstance(main.compute_product_of_all_elements([1, 2, 4]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it return the product of all elements
        self.assertEqual(main.compute_product_of_all_elements([1, 2, 4]), 8,
        msg = 'return the product of all elements')


    def test_2(self):
        # it return 0 if the passed in list is empty
        self.assertEqual(main.compute_product_of_all_elements([]), 0,
        msg = 'return 0 if the passed in list is empty')

    def test_3(self):
        # it return 0 if the passed in list that doesn't have all numbers
        self.assertEqual(main.compute_product_of_all_elements([3, "not",'numbers']), -1,
        msg = 'return -1 if the list contains one or more strings')

```

### !end-tests

### !explanation
```python
from functools import reduce
def compute_product_of_all_elements(lst):
    if not lst: return 0
    try:
        return reduce(lambda x, y: x * y, lst, 1)
    except TypeError: #if there are strings in lst, will get TypeError on x*y
        return -1    

#alternative solution
# def compute_product_of_all_elements(lst):
#     if not lst: return 0

#     acc = 1
#     for item in lst:
#         if isinstance(item, str):
#             return -1
#         else:
#             acc *= item

#     return acc
```
### !end-explanation

### !end-challenge
