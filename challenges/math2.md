# Math 2

### !challenge

* type: code-snippet
* language: python3.6
* id: 9ac26815-96c8-44bd-baac-960b874e4b32
* title: compute_area_of_aRectangle

### !question

Write a function called "compute_area_of_aRectangle".

Given the length and width of a rectangle, "compute_area_of_aRectangle" returns its area.

```
output = compute_area_of_aRectangle(4, 8)
print(output) # --> 32
```

### !end-question

### !placeholder

```python
def compute_area_of_aRectangle(length, width):
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
        self.assertEqual(main.compute_area_of_aRectangle(6, 7), 42,
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
* title: compute_perimeter_of_aRectangle

### !question

Write a function called "compute_perimeter_of_aRectangle".

Given a length and a width describing a rectangle, "compute_perimeter_of_aRectangle" returns its perimter.

```
output = compute_perimeter_of_aRectangle(5, 2)
print(output) # --> 14
```

### !end-question

### !placeholder

```python
def compute_perimeter_of_aRectangle(length, width):
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
        self.assertEqual(main.compute_perimeter_of_aRectangle(5, 6), 22,
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
* title: compute_perimeter_of_aTriangle

### !question

Write a function called "compute_perimeter_of_aTriangle".

Given 3 sides describing a triangle, "compute_perimeter_of_aTriangle" returns its perimter.

```
output = compute_perimeter_of_aTriangle(6, 7, 10)
print(output) # --> 23
```

### !end-question

### !placeholder

```python
def compute_perimeter_of_aTriangle(side1, side2, side3):
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
        self.assertEqual(main.compute_perimeter_of_aTriangle(6, 8, 10), 24,
        msg = "it should return the perimeter of a triangle" )
```


### !end-tests

### !explanation

### !end-explanation

### !end-challenge
