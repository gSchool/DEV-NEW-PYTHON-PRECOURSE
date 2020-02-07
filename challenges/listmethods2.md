# Array Methods 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 81d6b24b-5a97-408c-9681-c698da6881f6
* title: add_to_front

### !question

Write a function called "add_to_front".

Given an list and an element, "add_to_front" adds the given element to the front of the given list, and returns the given list.

Notes:
* It should be the SAME list, not a new list.

```
output = add_to_front([1, 2], 3)
print(output) # -> [3, 1, 2]
```

### !end-question

### !placeholder

```python
def add_to_front(input_list, element):
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
        # "it should return a list"
        self.assertIs(type(main.add_to_front([1, 2], 13)), list,
        msg = "it should return a list" )

    def test2(self):
        # "it should add an element to the beginning of an list"
        self.assertEqual(main.add_to_front([1, 2], 13), [13,1,2],
        msg = "it should add an element to the beginning of an list" )

    def test3(self):
        # "it should add an element to the beginning of an empty list"
        self.assertEqual(main.add_to_front([], 13), [13],
        msg = "it should add an element to the beginning of an empty list" )

    def test4(self):
        # "it should add an element to the beginning of an empty list"
        list1 = [1,2,3]
        self.assertIs(main.add_to_front(list1, -13), list1,
        msg = "it should be the same list object that was passed in" )
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e2ea174d-35c8-441d-9d82-7f2690a30278
* title: add_to_back

### !question

Write a function called "add_to_back".

Given an list and an element, "add_to_back" returns the given list with the given element added to the end.

Note: It should be the SAME array, not a new array.

```
output = add_to_back([1, 2], 3)
print(output) # -> [1, 2, 3]
```

### !end-question

### !placeholder

```python
def add_to_back(input_list, element):
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
        # "it should return a list"
        self.assertIs(type(main.add_to_back([1, 2], 13)), list,
        msg = "it should return a list" )

    def test2(self):
        # "it should add an element to the beginning of an list"
        self.assertEqual(main.add_to_back([1, 2], 13), [1, 2, 13],
        msg = "it should add an element to the back of a list" )

    def test3(self):
        # "it should add an element to the beginning of an empty list"
        self.assertEqual(main.add_to_back([], 13), [13],
        msg = "it should add an element to the back of an empty list" )

    def test4(self):
        # "it should add an element to the beginning of an empty list"
        list1 = [1,2,3]
        self.assertIs(main.add_to_back(list1, 13), list1,
        msg = "it should be the same list object that was passed in" )
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
