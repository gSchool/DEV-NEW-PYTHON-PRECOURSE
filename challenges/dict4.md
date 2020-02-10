# Dictionary 4

### !challenge

* type: code-snippet
* language: python3.6
* id: 09b2c4c3-d899-49fa-a943-60a03de413c2
* title: remove_numbers_larger_than

### !question

Write a function called "remove_numbers_larger_than".

Given a number and a dictionary, "remove_numbers_larger_than" removes any keys whose values are numbers greater than the given number.

```
dictionary = {'a': 8, 'b': 2, 'c': 'montana'}

result = remove_numbers_larger_than(5, dictionary)
print(result) # --> {'b': 2, 'c': 'montana'}
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
        # it should remove any keys with values that are integers greater than the given number
        dictionary = {'a': 8, 'b': 6, 'c':'montana', 'd':-3}
        number = -1
        result = {'c':'montana', 'd':-3}
        self.assertEqual(main.remove_numbers_larger_than(number, dictionary), result,
        msg = 'should remove any keys with values that are integers greater than num')
```

### !end-tests

### !explanation
```python
def remove_numbers_larger_than(target, dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] > target: removal_list.append(key)
    
    for key in removal_list:
        dictionary.pop(key)
    return dictionary
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: ee54e130-d037-4ff7-9c59-5461322523e1
* title: remove_integers_less_than

### !question

Write a function called "remove_integers_less_than".

Given a number and a dictionary, "remove_integers_less_than" removes any keys whose values are numbers less than the given number.

```
dictionary = {'a': 8, 'b': 2, 'c':'montana'}

result = remove_integers_less_than(5, dictionary)
print(result) # --> {'a': 8, 'c':'montana'}
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
        # it should remove any keys with values that are integers less than target
        dictionary = {'a': 8, 'b': 6, 'c':'montana', 'd': -3}
        target = 5
        result = {'a': 8, 'b': 6, 'c':'montana'}

        self.assertEqual(main.remove_integers_less_than(target, dictionary), result,
        msg = 'should remove any keys with values that are integers less than target')

```

### !end-tests

### !explanation
```python
def remove_integers_less_than(target, dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] < target: removal_list.append(key)
    
    for key in removal_list:
        dictionary.pop(key)
    
    return dictionary
```

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 47b07382-07c8-41b1-98e0-dae82ed992da
* title: remove_string_values_longer_than

### !question

Write a function called "remove_string_values_longer_than".

Given an number and a dictionary, "remove_string_values_longer_than" removes any keys on the given dictionary whose values are strings longer than the given number.

```
dictionary = {'name': 'Montana', 'age': 20, 'location': 'Texas'}
result = remove_string_values_longer_than(6, dictionary)

print(result)  # -> {'age': 20, 'location': 'Texas'}
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
        dictionary = {'a': 8, 'b': 6, 'c':'montana', 'location':'castle', 'age': 'old'}
        number = 5
        result = {'a': 8, 'b': 6, 'age': 'old'}

        self.assertEqual(main.remove_string_values_longer_than(number, dictionary), result,
        msg = 'should remove any keys with values that are strings longer than num')

```

### !end-tests

### !explanation
```python
def remove_string_values_longer_than(target, dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], str):
            if len(dictionary[key]) > target: removal_list.append(key)
    
    for key in removal_list:
        dictionary.pop(key)
    
    return dictionary
```
### !end-explanation

### !end-challenge
