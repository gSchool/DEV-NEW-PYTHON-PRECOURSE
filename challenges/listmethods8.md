# List Methods 8

### !challenge

* type: code-snippet
* language: python3.6
* id: 5fc75a18-76e2-4e35-afac-e8433908ea84
* title: remove_element

### !question

Write a function called "remove_element".

Given a list of elements, and a "discarder" parameter, "remove_element" returns a list containing the items in the given list that do not match the "discarder" parameter.

Notes:
* If all the elements match, it should return an empty list.
* If an empty list is passed in, it should return an empty list.

```
output = remove_element([1, 2, 3, 2, 1], 2)
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
        self.assertIsInstance(main.remove_element(["there", "it", "is", "there"], 3), list,
        msg = 'should return a list')


    def test_1(self):
        # it return a list with all strings not matching 'discarder'
        self.assertEqual(main.remove_element(["there", "it", "is", "there"], "there"), ["it", "is"],
        msg = "return a list with all strings not matching 'discarder'")


    def test_2(self):
        # it return a list with all numbers not matching 'discarder'
        self.assertEqual(main.remove_element([1, 2, 4, 3, 1, 4], 4), [1, 2, 3, 1],
        msg = "return a list with all strings not matching 'discarder'")


    def test_3(self):
        # it return a list with all booleans not matching 'discarder'
        self.assertEqual(main.remove_element([True, True, True, False, True], True), [False],
        msg = "return a list with all strings not matching 'discarder'")


    def test_4(self):
        # it return an empty list when all elements match 'discarder'
        self.assertEqual(main.remove_element([True, True, True, True], True), [],
        msg = "return a list with all strings not matching 'discarder'")


    def test_5(self):
        # it return an empty list when given an empty list
        self.assertEqual(main.remove_element([], 4), [],
        msg = 'return an empty list when given an empty list')


```

### !end-tests

### !explanation
```python
def remove_element(lst, discarder):
    return [x for x in lst if x != discarder]
```
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
```python
def keep(lst, keeper):
    return [x for x in lst if x == keeper]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bc301ebb-2394-447c-a893-a41007246e59
* title: compute_average_of_numbers

### !question

Write a function called "compute_average_of_numbers".

Given a list of numbers, "compute_average_of_numbers" returns their average.

Notes:
* If given an empty list, it should return 0.

```
input_list = [1,2,3,4,5]
output = compute_average_of_numbers(input_list)
print(output) # --> 3
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
        self.assertIsInstance(main.compute_average_of_numbers([6, 8, 10]), (float,int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the average of the numbers in the given list
        self.assertEqual(main.compute_average_of_numbers([6, 8, 10]), 8,
        msg = 'should return the average of the numbers in the given list')


    def test_2(self):
        # it should return the average of negative numbers in the given list
        self.assertEqual(main.compute_average_of_numbers([-6, -8, -10]), -8,
        msg = 'should return the average of negative numbers in the given list')


    def test_3(self):
        # it should return 0 if given an empty list
        self.assertEqual(main.compute_average_of_numbers([]), 0,
        msg = 'should return 0 if given an empty list')

```

### !end-tests

### !explanation
```python
def compute_average_of_numbers(num_list):
    if not num_list: return 0
    return sum(num_list) / len(num_list)


```
### !end-explanation

### !end-challenge
