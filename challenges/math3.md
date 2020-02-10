# Math 3

### !challenge

* type: code-snippet
* language: python3.6
* id: 4912dcc3-714b-405d-a1c6-9d4668195528
* title: compute_tripled_area_of_rectangle

### !question

Write a function called "compute_tripled_area_of_rectangle".

Given a length and width of a rectangle, "compute_tripled_area_of_rectangle" returns the rectangle's area, multiplied by 3.

```
output = compute_tripled_area_of_rectangle(2, 4)
print(output) # --> 24
```

### !end-question

### !placeholder

```python
def compute_tripled_area_of_rectangle(length, width):
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
        # "it should return the 3 * area of a rectangle"
        self.assertEqual(main.compute_tripled_area_of_rectangle(2, 4),
        24,
        msg = "it should return the 3 * area of a rectangle" )

```


### !end-tests

### !explanation
```python
def compute_tripled_area_of_rectangle(length, width):
    return 3 * length * width
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: a4c9be25-3121-4933-a4b5-e6099ca26ec6
* title: compute_perimeter_of_circle

### !question

Write a function called "compute_perimeter_of_circle".

Given the radius of a circle, "compute_perimeter_of_circle" returns its perimeter.

Notes:
* `math.pi` can be used for pi.

```
output = compute_perimeter_of_circle(4)
print(output) # --> 25.132741228718345
```

Reference:
[docs.python.org/3/library/math.html#math.pi](https://docs.python.org/3/library/math.html#math.pi)

### !end-question

### !placeholder

```python
import math

def compute_perimeter_of_circle(radius):
    # your code here
    pass



```

### !end-placeholder

### !tests

```python
import main
import unittest
import math

class TestScript(unittest.TestCase):
    def test1(self):
        # "it should return the perimeter of a circle"
        self.assertAlmostEqual(main.compute_perimeter_of_circle(4), 25.132741,
        delta = 0.000001,
        msg = "it should return the perimeter of a circle" )


```


### !end-tests

### !explanation
```python
def compute_perimeter_of_circle(radius):
    return 2 * math.pi * radius
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: a2e9ed27-c4b2-4aa9-bd99-afe1d3a8a68a
* title: compute_area_of_circle

### !question

Write a function called "compute_area_of_circle".

Given the radius of a circle, "compute_area_of_circle" returns its area.

Notes:
* `math.pi` can be used for pi.

```
output = compute_area_of_circle(4)
print(output) # --> 50.26548245743669
```


Reference:
[docs.python.org/3/library/math.html#math.pi](https://docs.python.org/3/library/math.html#math.pi)

### !end-question

### !placeholder

```python
import math

def compute_area_of_circle(radius):
    # your code here
    pass



```

### !end-placeholder

### !tests

```python
import main
import unittest
import math
class TestScript(unittest.TestCase):
    def test1(self):
        # "it should return the area of a circle"
        self.assertAlmostEqual(main.compute_area_of_circle(4), 50.265482,
        delta = 0.001,
        msg = "it should return the area of a circle" )

```


### !end-tests

### !explanation
```python
def compute_area_of_circle(radius):
    return math.pi * radius * radius
```
### !end-explanation

### !end-challenge
