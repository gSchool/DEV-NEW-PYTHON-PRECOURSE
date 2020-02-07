# Array Methods 11

### !challenge

* type: code-snippet
* language: python3.6
* id: 3fb77f32-bfa4-46a3-b207-3b7cf58ba011
* title: filterEvenElements

### !question

Write a function called "filterEvenElements".

Given a list of numbers, "filterEvenElements" returns a list containing only the even numbers of the given list.
```
output = filterEvenElements([2, 3, 4, 5, 6])
print(output) # --> [2, 4, 6]
```

### !end-question

### !placeholder

```python
def filterEvenElements(arr):
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
        self.assertIsInstance(main.filterEvenElements([1, 2, 3, 4]), list,
        msg = 'should return a list')


    def test_1(self):
        # it should return a list with the even elements from the passed in list
        self.assertEqual(main.filterEvenElements([1, 2, 3, 4, 5]), [2, 4],
        msg = 'should return a list with the even elements from the passed in list')


    def test_2(self):
        # it should return a list if there are no even numbers
        self.assertEqual(main.filterEvenElements([1, 3, 5]), [],
        msg = 'should return a list if there are no even numbers')


    def test_3(self):
        # it should return a list if given an empty list
        self.assertEqual(main.filterEvenElements([]), [],
        msg = 'should return a list if given an empty list')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 0c0a6c72-d8a0-488e-a0c7-c3a8df27630f
* title: getLengthOfShortestElement

### !question

Write a function called "getLengthOfShortestElement".

Given a list, "getLengthOfShortestElement" returns the length of the shortest string in the given list.

Notes:
* It should return 0 if the list is empty.

```
output = getLengthOfShortestElement(['one', 'two', 'three'])
print(output) # --> 3
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
        # it should return a number
        self.assertIsInstance(main.getLengthOfShortestElement(["one", "two", "three"]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the length of the shortest element in a list
        self.assertEqual(main.getLengthOfShortestElement(["one", "four", "three"]), 3,
        msg = 'should return the length of the shortest element in a list')


    def test_2(self):
        # it it should handle ties
        self.assertEqual(main.getLengthOfShortestElement(["one", "to", "no"]), 2,
        msg = 'it should handle ties')


    def test_3(self):
        # it it should return 0 when given an empty list
        self.assertEqual(main.getLengthOfShortestElement([]), 0,
        msg = 'it should return 0 when given an empty list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c910016d-56a3-4e65-88d8-01111d85a609
* title: getLongestElement

### !question

Write a function called "getLongestElement".

Given a list, "getLongestElement" returns the longest string in the given list.

Notes:
* If there are ties, it returns the first element to appear.
* If the list is empty, it should return an empty string.

```
output = getLongestElement(['one', 'two', 'three'])
print(output) # --> 'three'
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
            # it should return a string
            self.assertIsInstance(main.getLongestElement(["one", "two", "three"]), str,
            msg = 'should return a string')


        def test_1(self):
            # it should return the longest element in a list
            self.assertEqual(main.getLongestElement(["one", "two", "three"]), "three",
            msg = 'should return the longest element in a list')


        def test_2(self):
            # it should return the first longest element in a list when there are ties
            self.assertEqual(main.getLongestElement(["one", "two", "one"]), "one",
            msg = 'should return the first longest element in a list when there are ties')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
