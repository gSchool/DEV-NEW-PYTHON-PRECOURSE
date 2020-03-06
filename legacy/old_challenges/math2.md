# Math 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 9ac26815-96c8-44bd-baac-960b874e4b32
* title: computeAreaOfARectangle

### !question

Write a function called "computeAreaOfARectangle".

Given the length and width of a rectangle, "computeAreaOfARectangle" returns its area.

```
output = computeAreaOfARectangle(4, 8)
print(output) # --> 32
```

### !end-question

### !placeholder

```python
def computeAreaOfARectangle(length, width):
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
        # it should return the area of a rectangle
        self.assertEqual(main.computeAreaOfARectangle(6, 7), 42,
        msg = "it should return the area of a rectangle" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 2fd97e96-08e0-4a67-a662-949acbf0e43c
* title: computePerimeterOfARectangle

### !question

Write a function called "computePerimeterOfARectangle".

Given a length and a width describing a rectangle, "computePerimeterOfARectangle" returns its perimter.

```
output = computePerimeterOfARectangle(5, 2)
print(output) # --> 14
```

### !end-question

### !placeholder

```python
def computePerimeterOfARectangle(length, width):
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
        # it should return the perimeter of a rectangle
        self.assertEqual(main.computePerimeterOfARectangle(5, 6), 22,
        msg = "it should return the perimeter of a rectangle" )

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 349703e4-eba7-4566-9a0f-c81569733b84
* title: computePerimeterOfATriangle

### !question

Write a function called "computePerimeterOfATriangle".

Given 3 sides describing a triangle, "computePerimeterOfATriangle" returns its perimter.

```
output = computePerimeterOfATriangle(6, 7, 10)
print(output) # --> 23
```

### !end-question

### !placeholder

```python
def computePerimeterOfATriangle(side1, side2, side3):
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
        # it should return the perimeter of a triangle
        self.assertEqual(main.computePerimeterOfATriangle(6, 8, 10), 24,
        msg = "it should return the perimeter of a triangle" )
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
