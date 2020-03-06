# List Methods 12

### !challenge

* type: code-snippet
* language: python3.6
* id: 3e9cfffd-1ec6-4243-a91b-4546c2d647aa
* title: find_smallest_element

### !question

Write a function called "find_smallest_element".

Given a list of numbers, "find_smallest_element" returns the smallest number within the given list.

Notes:
* If the given list is empty, it should return 0.

```
output = find_smallest_element([4, 1, 9, 10])
print(output) # --> 1
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
        self.assertIsInstance(main.find_smallest_element([3, 5, 3, 1]), (float, int),
        msg = 'should return a number')


    def test_1(self):
        # it should return the smallest element in a list
        self.assertEqual(main.find_smallest_element([3, 5, 3, 1]), 1,
        msg = 'should return the smallest element in a list')


    def test_2(self):
        # it should return the smallest element in a list when there are ties
        self.assertEqual(main.find_smallest_element([3, 1, 3, 1, 5]), 1,
        msg = 'should return the smallest element in a list when there are ties')


    def test_3(self):
        # it should return the smallest element in a list when they are all negative
        self.assertEqual(main.find_smallest_element([-1, -5, -3]), -5,
        msg = 'should return the smallest element in a list when they are all negative')


    def test_4(self):
        # it should return 0 if the list is empty
        self.assertEqual(main.find_smallest_element([]), 0,
        msg = 'should return 0 if the list is empty')

```

### !end-tests

### !explanation
```python
def find_smallest_element(input_list):
    if not input_list: return 0
    return min(input_list)
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 3a3527f5-84ad-4d59-8ba5-5e774661e37e
* title: find_shortest_element

### !question

Write a function called "find_shortest_element".

Given a list of strings, "find_shortest_element" returns the shortest string within the given list.

Notes:
* If there are ties, it should return the first element to appear.
* If the given list is empty, it should return an empty string.

```
output = find_shortest_element(['a', 'two', 'three'])
print(output) # --> 'a'
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
        # it should return a string
        self.assertIsInstance(main.find_shortest_element(["one", "two", "three"]), str,
        msg = 'should return a string')


    def test_1(self):
        # it should return the shortest element in a list
        self.assertEqual(main.find_shortest_element(["a", "two", "three"]), "a",
        msg = 'should return the shortest element in a list')


    def test_2(self):
        # it should return the first shortest element in a list when there are ties
        self.assertEqual(main.find_shortest_element(["one", "to", "no"]), "to",
        msg = 'should return the first shortest element in a list when there are ties')

    def test_3(self):
        # it should return an empty string if the list is empty
        self.assertEqual(main.find_shortest_element([]), "",
        msg = 'should return an empty string if the list is empty')

```

### !end-tests

### !explanation
```python
def find_shortest_element(input_list):
    if not input_list: return ""
    
    min_len, shortest_string = len(input_list[0]), input_list[0]
    for item in input_list:
        if len(item) < min_len:
            min_len, shortest_string = len(item), item
    return shortest_string
```
### !end-explanation

### !end-challenge
