# Math 1

### !challenge

* type: code-snippet
* language: python3.6
* id: 6a2a074c-7652-488e-b51c-0a441fa0fae9
* title: average

### !question

Write a function called "average".

Given two numbers, "average" returns their average.

```
output = average(4, 6)
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def average(num1, num2):
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
        # "it should return the average of two numbers"
        self.assertEqual(main.average(100,200), 150,
        msg = "it should return the average of two numbers" )

```

### !end-tests

### !explanation
```python
def average(num1, num2):
    return (num1 + num2)/2


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: bb88d243-fda0-4b49-ba45-f4a19ead5d03
* title: compute_area_of_triangle

### !question

Write a function called "compute_area_of_triangle".

Given the base and height of a triangle, "compute_area_of_triangle" returns its area.

```
output = compute_area_of_triangle(4, 6)
print(output) # --> 12
```

### !end-question

### !placeholder

```python
def compute_area_of_triangle(base, height):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test2(self):
        # "it should return the area of a triangle"
        self.assertEqual(main.compute_area_of_triangle(4, 6), 12,
        msg = "it should return the area of a triangle" )


```

### !end-tests

### !explanation
```python

def compute_area_of_triangle(base, height):
    return base * height / 2


```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 327a2860-4858-4627-9632-f451e415e7d4
* title: cube

### !question

Write a function called "cube".

Given a number, "cube" returns the cube of that number.

```
output = cube(3)
print(output) # --> 27
```

### !end-question

### !placeholder

```python
def cube(num):
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
        # it should_cube_a_positive_number
        self.assertEqual(main.cube(2), 8,
        msg = "it should cube a positive number")

    def test2(self):
        # it should_cube_a_positive_number
        self.assertEqual(main.cube(0), 0,
        msg = "it should cube zero")

    def test3(self):
        # it should_cube_a_positive_number
        self.assertEqual(main.cube(-2), -8,
        msg = "it should cube a negative number")

```


### !end-tests

### !explanation
```python
def cube(num):
    return num * num * num

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 1d51ed19-4978-4574-bb07-9b65921ed07e
* title: square

### !question

Write a function called "square".

Given a number, "square" should return the square of the given number.

```
output = square(5)
print(output) # --> 25
```

### !end-question

### !placeholder

```python
def square(num):
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
        # it should square a positive number
        self.assertEqual(main.square(12), 144,
        msg = "it should square a positive number")

    def test2(self):
        # it should square zero
        self.assertEqual(main.square(0), 0,
        msg = "it should square a zero")

    def test3(self):
        # it should square a negative number
        self.assertEqual(main.square(-12), 144,
        msg = "it should square a negative number")

```


### !end-tests

### !explanation
```python

def square(num):
    return num * num
    
```
### !end-explanation

### !end-challenge
