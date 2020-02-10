# List Methods 4

### !challenge

* type: code-snippet
* language: python3.6
* id: 879c0dc1-12a5-4dad-876a-5f698f0dbe05
* title: get_all_elements_but_first

### !question

Write a function called "get_all_elements_but_first".

Given a list, "get_all_elements_but_first" returns a list with all the elements but the first.

```
x = [1, 2, 3, 4]
output = get_all_elements_but_first(x)
print(output) # --> [2, 3, 4]

output = get_all_elements_but_first([])
print(output) # --> []

output = get_all_elements_but_first([14])
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
        # it "should return an list"
        self.assertIs(type(main.get_all_elements_but_first([1,2,3,4])), list,
        msg =  "it should return an list")

    def test2(self):
        # "should return an array with all the elements of the passed in array, except for the first"
        self.assertEqual(main.get_all_elements_but_first([4, 5, 6]), [5,6],
        msg = "it should return an array with all the elements of the passed in array, except for the first")

    def test3(self):
        # it "should return an empty array when passed in a single element array"
        self.assertEqual(main.get_all_elements_but_first([4]), [],
        msg = "it should return an empty array when passed in a single element array")

    def test4(self):
        # it "should return an empty array when passed in an empty array"
        self.assertEqual(main.get_all_elements_but_first([]), [],
        msg = "it should return an empty array when passed in an empty array")

```

### !end-tests

### !explanation
```python
def get_all_elements_but_first(lst):
    return lst[1:]
```

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 1662f5c1-43d4-4cbe-8a0e-2c6866408de5
* title: get_all_elements_but_last

### !question

Write a function called "get_all_elements_but_last".

Given an list, "get_all_elements_but_last" returns an list with all the elements but the last.

```
x = [1, 2, 3, 4]
output = get_all_elements_but_last(x)
print(output) # --> [1, 2, 3]

output = get_all_elements_but_last([])
print(output) # --> []

output = get_all_elements_but_last([14])
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
        # it "should return an list"
        self.assertIs(type(main.get_all_elements_but_last([1,2,3,4])), list,
        msg =  "it should return an list")

    def test2(self):
        # it "should return an array with all the elements of the passed in array, except for the last"
        self.assertEqual(main.get_all_elements_but_last([1,2,3,4]), [1,2,3],
        msg = "should return an array with all the elements of the passed in array, except for the last")

    def test3(self):
        # it "should return an empty array when passed in a single element array"
        self.assertEqual(main.get_all_elements_but_last([1]), [],
        msg = "should return an empty array when passed in a single element array")

    def test4(self):
        # it
        self.assertEqual(main.get_all_elements_but_last([]), [],
        msg = "it should return an empty array when passed in an empty array")

```

### !end-tests

### !explanation
```python
def get_all_elements_but_last(lst):
    return lst[:-1]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 94f66a0e-795b-439b-bb69-c12c78b475b0
* title: remove_from_front

### !question

Write a function called "remove_from_front".

Given an list, "remove_from_front" returns the given list with its first element removed.


```
output = remove_from_front([1, 2, 3])
print(output) # --> [2, 3]

output = remove_from_front([])
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
        # it "should return an array"
        self.assertIs(type(main.remove_from_front([1, 2, 3])), list,
        msg = "it should return a list" )

    def test2(self):
        # it "should return the array with the first element removed"
        self.assertEqual(main.remove_from_front([1, 2]),[2],
        msg = "should return the list with the first element removed")

    def test3(self):
        # it "should handle an empty array"
        self.assertEqual(main.remove_from_front([]), [],
        msg = "it should handle an empty list" )

```


### !end-tests

### !explanation
```python
def remove_from_front(lst):
    return lst[1:]
```
### !end-explanation

### !end-challenge
