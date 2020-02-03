# Array Methods 4

### !challenge

* type: code-snippet
* language: python3.6
* id: 879c0dc1-12a5-4dad-876a-5f698f0dbe05
* title: getAllElementsButFirst

### !question

Write a function called "getAllElementsButFirst".

Given a list, "getAllElementsButFirst" returns a list with all the elements but the first.

```
input = [1, 2, 3, 4]
output = getAllElementsButFirst(input)
print(output) # --> [2, 3, 4]

output = getAllElementsButFirst([])
print(output) # --> []

output = getAllElementsButFirst([14])
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
        self.assertIs(type(main.getAllElementsButFirst([1,2,3,4])), list,
        msg =  "it should return an list")

    def test2(self):
        # "should return an array with all the elements of the passed in array, except for the first"
        self.assertEqual(main.getAllElementsButFirst([4, 5, 6]), [5,6],
        msg = "it should return an array with all the elements of the passed in array, except for the first")

    def test3(self):
        # it "should return an empty array when passed in a single element array"
        self.assertEqual(main.getAllElementsButFirst([4]), [],
        msg = "it should return an empty array when passed in a single element array")

    def test4(self):
        # it "should return an empty array when passed in an empty array"
        self.assertEqual(main.getAllElementsButFirst([]), [],
        msg = "it should return an empty array when passed in an empty array")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 1662f5c1-43d4-4cbe-8a0e-2c6866408de5
* title: getAllElementsButLast

### !question

Write a function called "getAllElementsButLast".

Given an list, "getAllElementsButLast" returns an list with all the elements but the last.

```
input = [1, 2, 3, 4]
output = getAllElementsButLast(input)
print(output) # --> [1, 2, 3]

output = getAllElementsButLast([])
print(output) # --> []

output = getAllElementsButLast([14])
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
        self.assertIs(type(main.getAllElementsButLast([1,2,3,4])), list,
        msg =  "it should return an list")

    def test2(self):
        # it "should return an array with all the elements of the passed in array, except for the last"
        self.assertEqual(main.getAllElementsButLast([1,2,3,4]), [1,2,3],
        msg = "should return an array with all the elements of the passed in array, except for the last")

    def test3(self):
        # it "should return an empty array when passed in a single element array"
        self.assertEqual(main.getAllElementsButLast([1]), [],
        msg = "should return an empty array when passed in a single element array")

    def test4(self):
        # it
        self.assertEqual(main.getAllElementsButLast([]), [],
        msg = "it should return an empty array when passed in an empty array")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 94f66a0e-795b-439b-bb69-c12c78b475b0
* title: removeFromFront

### !question

Write a function called "removeFromFront".

Given an list, "removeFromFront" returns the given list with its first element removed.


```
output = removeFromFront([1, 2, 3])
print(output) # --> [2, 3]

output = removeFromFront([])
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
        self.assertIs(type(main.removeFromFront([1, 2, 3])), list,
        msg = "it should return a list" )

    def test2(self):
        # it "should return the array with the first element removed"
        self.assertEqual(main.removeFromFront([1, 2]),[2],
        msg = "should return the list with the first element removed")

    def test3(self):
        # it "should handle an empty array"
        self.assertEqual(main.removeFromFront([]), [],
        msg = "it should handle an empty list" )

```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
