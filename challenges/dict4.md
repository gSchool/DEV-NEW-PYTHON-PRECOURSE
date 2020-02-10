# Dictionary 4

### !challenge

* type: code-snippet
* language: python3.6
* id: 09b2c4c3-d899-49fa-a943-60a03de413c2
* title: remove_numbers_larger_than

### !question

Write a function called "remove_numbers_larger_than".

Given a number and an dictionary, "remove_numbers_larger_than" removes any keys whose values are numbers greater than the given number.

```
input = {'a': 8, 'b': 2, 'c': 'montana'}

remove_numbers_larger_than(5, input)
print(input) # --> {'b': 2, 'c': 'montana'}
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
        # it should remove any keys with values that are numbers greater than the given number
        input = {'a': 8, 'b': 6, 'c':'montana', 'd':'-3'}
        number = -1
        result = {'c':'montana', 'd':'-3'}
        self.assertEqual(main.remove_numbers_larger_than(number, input), result,
        msg = 'should remove any keys with values that are numbers greater than num')
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: ee54e130-d037-4ff7-9c59-5461322523e1
* title: remove_numbers_less_than

### !question

Write a function called "remove_numbers_less_than".

Given a number and a dictionary, "remove_numbers_less_than" removes any keys whose values are numbers less than the given number.

```
input = {'a': 8, 'b': 2, 'c':'montana'}

remove_numbers_less_than(5, input)
print(input) # --> {'a': 8, 'c':'montana'}
```

### !end-question

### !placeholder

```python
#your code here

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test_0(self):
        # it should remove any properties with values that are numbers less than num
        input = {'a': 8, 'b': 6, 'c':'montana', 'd': -3}
        number = 5
        result = {'a': 8, 'b': 6, 'c':'montana'}

        self.assertEqual(main.remove_numbers_less_than(number, input), result,
        msg = 'should remove any properties with values that are numbers less than num')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 47b07382-07c8-41b1-98e0-dae82ed992da
* title: remove_string_values_longer_than

### !question

Write a function called "remove_string_values_longer_than".

Given an number and an dictionary, "remove_string_values_longer_than" removes any keys on the given dict whose values are strings longer than the given number.

```
input = {'name': 'Montana', 'age': 20, 'location': 'Texas'}
remove_string_values_longer_than(6, input)

print(input)  # -> {'age': 20, 'location': 'Texas'}
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
        # it should remove any keys with values that are strings longer than num
        input = {'a': 8, 'b': 6, 'c':'montana', 'location':'castle', 'age': 'old'}
        number = 5
        result = {'a': 8, 'b': 6, 'age': 'old'}

        self.assertEqual(main.remove_string_values_longer_than(number, input), result,
        msg = 'should remove any keys with values that are strings longer than num')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
