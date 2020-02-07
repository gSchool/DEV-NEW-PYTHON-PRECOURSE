# Array Methods 3

### !challenge

* type: code-snippet
* language: python3.6
* id: 14e62a93-6633-4448-bea5-14ab6d68995c
* title: join_arrays

### !question

Write a function called "joinLists".

Given two lists, "joinLists" returns an list with the elements of "list1" in order, followed by the elements in "list2".

```
output = joinLists([1, 2], [3, 4])
print(output) # --> [1, 2, 3, 4]
```


### !end-question

### !placeholder

```python
#fill in the function definition below
# be sure to name the function according to the instructions


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it it should return a list
        self.assertIs(type(main.joinLists([1, 2], [3, 4])), list,
        msg = "it should return a list" )

    def test2(self):
        # it "should return an array with the elements from the first and then the second array"
        self.assertEqual(main.joinLists(['a', 'b'], [1, 3]), ['a', 'b', 1, 3],
        msg = "should return an array with the elements from the first and then the second array" )

    def test3(self):
        # "it should handle empty arrays in the first position"
        self.assertEqual(main.joinLists([], [1, 3]), [ 1, 3],
        msg = "it should handle empty arrays in the first position" )

    def test4(self):
        # "it should handle empty arrays in the second position"
        self.assertEqual(main.joinLists(['a', 'b'], []), ['a', 'b'],
        msg = "it should handle empty arrays in the second position" )

```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 39177ecc-9a13-4ca6-83c2-495489bfa312
* title: get_elements_after

### !question

Write a function called "get_elements_after".

Given an list and an index, "get_elements_after" returns a new list with all the elements after (but not including) the given index.

Note:
* In order to do this you should be familiar with slicing lists in Python.

```
Specifications:

output = get_elements_after(['a', 'b', 'c', 'd', 'e'], 2)
print(output) # --> ['d', 'e']

output = get_elements_after(['a', 'b', 'c'], 5)
print(output) # --> []

output = get_elements_after([], 2)
print(output) # --> []

output = get_elements_after([4], 1)
print(output) # --> []


```

### !end-question

### !placeholder

```python
#fill in the function definition below
# be sure to name the function according to the instructions


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return a list
        self.assertIs(type(main.get_elements_after([4, 5, 6], 2)), list,
        msg = "it should return a list" )

    def test2(self):
        # it "should return an array with all the elements of the passed in array get_elements_after the nth"
        self.assertEqual(main.get_elements_after([4, 5, 6, 7, 8, 9], 3), [8, 9],
        msg = "it should return an list with all the elements of the passed in array get_elements_after the nth" )

    def test3(self):
        # it "should return an empty array when passed an n out of range"
        self.assertEqual(main.get_elements_after([4,5,6,7,8,9], 11), [],
        msg = "it should return an empty list when passed an n out of range" )

    def test4(self):
        # it should return an empty array when passed in a single element array
        for n in range(5):
            with self.subTest(n=n):
                self.assertEqual(main.get_elements_after([4], n), [],
                msg = " it should return an empty list when passed in a single element list" )

    def test5(self):
        # it "should return an empty array when passed in an empty array"
        for n in range(5):
            with self.subTest(n=n):
                self.assertEqual(main.get_elements_after([], n), [],
                    msg = "should return an empty list when passed in an empty list" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 41fe3188-d6e9-4f43-9c4a-a1313a61b407
* title: get_elements_up_to

### !question

Write a function called "get_elements_up_to".

Given an list and a index, "get_elements_up_to", returns a list with all the elements up until, but not including, the element at the given index.

Notes:
* In order to do this you should be familiar with slicing lists in Python.

```
Specifications:

output = get_elements_up_to(['a', 'b', 'c', 'd', 'e'], 3)
print(output) # --> ['a', 'b', 'c']

output = get_elements_up_to(['a'], 0)
print(output) # --> []

output = get_elements_up_to(['a'], 3)
print(output) # --> ['a']

output = get_elements_up_to(['a','b'], 3)
print(output) # --> ['a','b']

output = get_elements_up_to([], 3)
print(output) # --> []


```

### !end-question

### !placeholder

```python
#fill in the function definition below
# be sure to name the function according to the instructions

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return a list
        self.assertIs(type(main.get_elements_up_to(['a', 'b', 'c', 'd', 'e'], 3)), list, msg = "it should return a list" )

    def test2(self):
        # it "should return an array with all the elements of the passed in array up to but not including the nth"
        self.assertEqual(main.get_elements_up_to([4, 5, 6], 2), [4, 5],
        msg = "it should return a list with all the elements of the passed in array up to but not including the nth" )

    def test3(self):
        # "it should return an empty array when passed in a single element array"
        self.assertEqual(main.get_elements_up_to([4], 0), [],
        msg = "it should return an empty list when passed in a single element array" )

    def test4(self):
        # it "should return a mirror of the original array when passed an n out of range"
        self.assertEqual(main.get_elements_up_to([4], 10), [4],
        msg = "it should return a mirror of the original list when passed an n out of range" )


    def test5(self):
        # "should return an empty array when passed in an empty array"
        for n in range(5):
            with self.subTest(n=n):
                self.assertEqual(main.get_elements_up_to([], n), [],
                msg = "it should return an empty list when passed in an empty list" )
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
