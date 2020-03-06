# Array Methods 13

### !challenge

* type: code-snippet
* language: python3.6
* id: 54143016-2767-47af-9931-408799951ba0
* title: getLargestElement

### !question

Write a function called "getLargestElement".

Given a list, "getLargestElement" returns the largest number in the given list.

Notes:
* It should return 0 if the list is empty.

```
output = getLargestElement([5, 2, 8, 3])
print(output) # --> 8
```

### !end-question

### !placeholder

```python
def getLargestElement(arr):
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
        self.assertIsInstance(main.getLargestElement([3, 5, 3, 1]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the largest element in a list
        self.assertEqual(main.getLargestElement([3, 5, 3, 1]), 5,
        msg = 'should return the largest element in a list')


    def test_2(self):
        # it should return the largest element in a list when there are ties
        self.assertEqual(main.getLargestElement([3, 5, 3, 1, 5]), 5,
        msg = 'should return the largest element in a list when there are ties')


    def test_3(self):
        # it should return the largest element in a list when they are all negative
        self.assertEqual(main.getLargestElement([-1, -5, -3]), -1,
        msg = 'should return the largest element in a list when they are all negative')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: baa3bc1e-1a67-4a6b-a66a-72cc6e55c8b4
* title: computeSumOfAllElements

### !question

Write a function called "computeSumOfAllElements".

Given a list of numbers, "computeSumOfAllElements" returns the sum of all the elements in the given list.

```
output = computeSumOfAllElements([1, 2, 3])
print(output) # --> 6
```

### !end-question

### !placeholder

```python
def computeSumOfAllElements(arr):
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
        self.assertIsInstance(main.computeSumOfAllElements([1, 2, 4]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it return the sum of all elements
        self.assertEqual(main.computeSumOfAllElements([1, 2, 4]), 7,
        msg = 'return the sum of all elements')


    def test_2(self):
        # it return 0 if the passed in list is empty
        self.assertEqual(main.computeSumOfAllElements([]), 0,
        msg = 'return 0 if the passed in list is empty')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
