# Dictionary 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 5c68f405-579c-4427-8f13-9df8539009c7
* title: remove_even_values

### !question

Write a function called "remove_even_values".

Given an dictionary, "remove_even_values" removes any keys whose values are even integers.

Do this in place, and return the original dictionary.

Example:

```
dictionary = {'a': 2, 'b': 3, 'c': 4, 'd':'Texas'}

output = remove_even_values(dictionary)
print(output) # --> {'b': 3, 'd':'Texas'}
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
        # it should remove any keys with values that are even integers
        dictionary = {'a':1, 'b':2, 'c': 'montana', 'd':8}
        result = {'a':1, 'c': 'montana'}
        self.assertEqual(main.remove_even_values(dictionary), result,
        msg = 'should remove any keys with values that are even integers')

```

### !end-tests

### !explanation
```python
def remove_even_values(dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] % 2 == 0: 
                removal_list.append(key)
    
    for key in removal_list:
        dictionary.pop(key)
    
    return dictionary
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 74b7a416-a4bc-4854-b870-0f92c6d57335
* title: count_number_of_keys

### !question

Write a function called "count_number_of_keys".

Given an dictionary, "count_number_of_keys" returns how many keys the given dictionary has.

```
dictionary = {'a': 1, 'b': 2, 'c': 3}

output = count_number_of_keys(dictionary)
print(output) # --> 3
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

    def test_1(self):
        # it should return the number of keys for an dictionary
        self.assertEqual(main.count_number_of_keys({'a': 1, 'b': 2, 'c': 3}), 3,
        msg = 'should return the number of keys for a dict')


    def test_2(self):
        # it should return 0 for an dictionary with no keys
        self.assertEqual(main.count_number_of_keys({}), 0,
        msg = 'should return 0 for a dict with no keys')


```

### !end-tests

### !explanation
```python
def count_number_of_keys(dictionary):
    return len(dictionary.keys())
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e01182d1-9906-49b8-830d-bae725ad5b4b
* title: remove_odd_values

### !question

Write a function called "remove_odd_values".

Given an dictionary, "remove_odd_values" removes any keys whose values are odd integers.

```
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd':'montana'}

output = remove_odd_values(dictionary)
print(output) # --> {'b': 2, 'd':'montana'}
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
        # it should remove any keys with values that are odd integers
        self.assertEqual(main.remove_odd_values({'a': 1, 'b': 2, 'c': 3, 'd':'Montana'}), {'b': 2, 'd':'Montana'},
        msg = 'should remove any key with values that are odd integers')

```

### !end-tests

### !explanation
```python
def remove_odd_values(dictionary):
    removal_list = []
    for key in dictionary:
        if isinstance(dictionary[key], int):
            if dictionary[key] % 2 == 1: 
                removal_list.append(key)
    
    for key in removal_list:
        dictionary.pop(key)
    
    return dictionary
```
### !end-explanation

### !end-challenge
