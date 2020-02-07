# Array Methods 8

### !challenge

* type: code-snippet
* language: python3.6
* id: 5fc75a18-76e2-4e35-afac-e8433908ea84
* title: removeElement

### !question

Write a function called "removeElement".

Given a list of elements, and a "discarder" parameter, "removeElement" returns a list containing the items in the given list that do not match the "discarder" parameter.

Notes:
* If all the elements match, it should return an empty list.
* If an empty list is passed in, it should return an empty list.

```
output = removeElement([1, 2, 3, 2, 1], 2)
print(output) # --> [1, 3, 1]
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
        self.assertIsInstance(main.removeElement(["there", "it", "is", "there"], 3), list,
        msg = 'should return a list')


    def test_1(self):
        # it return a list with all strings not matching 'discarder'
        self.assertEqual(main.removeElement(["there", "it", "is", "there"], "there"), ["it", "is"],
        msg = "return a list with all strings not matching 'discarder'")


    def test_2(self):
        # it return a list with all numbers not matching 'discarder'
        self.assertEqual(main.removeElement([1, 2, 4, 3, 1, 4], 4), [1, 2, 3, 1],
        msg = "return a list with all strings not matching 'discarder'")


    def test_3(self):
        # it return a list with all booleans not matching 'discarder'
        self.assertEqual(main.removeElement([True, True, True, False, True], True), [False],
        msg = "return a list with all strings not matching 'discarder'")


    def test_4(self):
        # it return an empty list when all elements match 'discarder'
        self.assertEqual(main.removeElement([True, True, True, True], True), [],
        msg = "return a list with all strings not matching 'discarder'")


    def test_5(self):
        # it return an empty list when given an empty list
        self.assertEqual(main.removeElement([], 4), [],
        msg = 'return an empty list when given an empty list')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 93c14e61-6f43-4158-848c-268271807a39
* title: keep

### !question

Write a function called "keep".

Given a list and a keeper element, "keep" returns a list containing the items that match the given keeper element.

Notes:
* If no elements match, "keep" should return an empty list.

```
output = keep([1, 2, 3, 2, 1], 2)
print(output) --> [2, 2]
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
        self.assertIsInstance(main.keep(["there", "it", "is", "there"], 2), list,
        msg = 'should return a list')


    def test_1(self):
        # it returns a list with all strings matching 'kept'
        self.assertEqual(main.keep(["there", "it", "is", "there"], "there"), ["there", "there"],
        msg = "returns a list with all strings matching 'kept'")


    def test_2(self):
        # it returns a list with all numbers matching 'kept'
        self.assertEqual(main.keep([1, 2, 4, 3, 1, 4], 4), [4, 4],
        msg = "returns a list with all strings matching 'kept'")


    def test_3(self):
        # it returns a list with all booleans matching 'kept'
        self.assertEqual(main.keep([True, True, True, False, True], True), [True, True, True, True],
        msg = "returns a list with all strings matching 'kept'")


    def test_4(self):
        # it returns an empty list when no elements match 'kept'
        self.assertEqual(main.keep([True, True, True, False, True], 4), [],
        msg = "returns an empty list when no elements match 'kept'")


    def test_5(self):
        # it returns an empty list when given an empty list
        self.assertEqual(main.keep([], 4), [],
        msg = 'returns an empty list when given an empty list')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bc301ebb-2394-447c-a893-a41007246e59
* title: computeAverageOfNumbers

### !question

Write a function called "computeAverageOfNumbers".

Given a list of numbers, "computeAverageOfNumbers" returns their average.

Notes:
* If given an empty list, it should return 0.

```
input = [1,2,3,4,5]
output = computeAverageOfNumbers(input)
print(output) # --> 3
```

### !end-question

### !placeholder

```python
def computeAverageOfNumbers(nums):
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
        self.assertIsInstance(main.computeAverageOfNumbers([6, 8, 10]), (float,int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the average of the numbers in the given list
        self.assertEqual(main.computeAverageOfNumbers([6, 8, 10]), 8,
        msg = 'should return the average of the numbers in the given list')


    def test_2(self):
        # it should return the average of negative numbers in the given list
        self.assertEqual(main.computeAverageOfNumbers([-6, -8, -10]), -8,
        msg = 'should return the average of negative numbers in the given list')


    def test_3(self):
        # it should return 0 if given an empty list
        self.assertEqual(main.computeAverageOfNumbers([]), 0,
        msg = 'should return 0 if given an empty list')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
