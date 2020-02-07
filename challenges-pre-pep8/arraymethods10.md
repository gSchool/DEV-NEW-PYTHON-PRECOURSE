# Array Methods 10

### !challenge

* type: code-snippet
* language: python3.6
* id: 89972114-2f9f-47da-aae3-8df266ff32b7
* title: squareElements

### !question

Write a function called "squareElements".
Given a list of numbers, "squareElements" should return a new list where each element is the square of the element of the given list.
```
output = squareElements([1, 2, 3])
print(output) # --> [1, 4, 9]
```

### !end-question

### !placeholder

```python
def squareElements(arr):
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
        # it should return a list
        self.assertIsInstance(main.squareElements([1, 2, 3]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with the elements of the passed in list, squared
        self.assertEqual(main.squareElements([10, 20, 30]), [100, 400, 900],
        msg = 'should return a list with the elements of the passed in list, squared')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bc26b616-3099-4e47-ad75-5670968a8ed1
* title: filterOddElements

### !question

Write a function called "filterOddElements".

Given a list of numbers, "filterOddElements" returns a list containing only the odd numbers of the given list.
```
output = filterOddElements([1, 2, 3, 4, 5])
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
        self.assertIsInstance(main.filterOddElements([1, 2, 3, 4]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with the odd elements from the passed in list
        self.assertEqual(main.filterOddElements([1, 2, 3, 4, 5]), [1, 3, 5],
        msg = 'should return a list with the odd elements from the passed in list')


    def test_2(self):
        # it should return a list if there are no odd numbers
        self.assertEqual(main.filterOddElements([2, 4, 6]), [],
        msg = 'should return a list if there are no odd numbers')


    def test_3(self):
        # it should return a list if given an empty list
        self.assertEqual(main.filterOddElements([]), [],
        msg = 'should return a list if given an empty list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e2f51369-1a84-42dc-8613-2ccd23f46bc2
* title: computeProductOfAllElements

### !question

Write a function called "computeProductOfAllElements".

Given a list of numbers, "computeProductOfAllElements" returns the products of all the elements in the given list.

Notes:
* If given list is empty, it should return 0.

```
output = computeProductOfAllElements([2, 5, 6])
print(output) # --> 60
```

### !end-question

### !placeholder

```python
def computeProductOfAllElements(arr):
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
        self.assertEqual(main.computeProductOfAllElements([1, 2, 4]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it return the product of all elements
        self.assertEqual(main.computeProductOfAllElements([1, 2, 4]), 8,
        msg = 'return the product of all elements')


    def test_2(self):
        # it return 0 if the passed in list is empty
        self.assertEqual(main.computeProductOfAllElements([]), 0,
        msg = 'return 0 if the passed in list is empty')

    def test_3(self):
        # it return 0 if the passed in list that doesn't have all numbers
        self.assertEqual(main.computeProductOfAllElements([3, "not",'numbers']), 0,
        msg = 'return 0 if the passed in list that does not have all numbers')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
