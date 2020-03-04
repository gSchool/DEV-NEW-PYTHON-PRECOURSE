# Dictionary 13

### !challenge

* type: code-snippet
* language: python3.6
* id: be23ee89-7ea7-4f26-8194-5cc405d6b7a4
* title: get_sum_of_all_elements_at_key

### !question

Write a function called "get_sum_of_all_elements_at_key".

Given a dictionary and a key, "get_sum_of_all_elements_at_key" returns the sum of all the elements in the list located at the given key.

Notes:

* If the list exists at the key, you can assume it contains only numbers.
* If the list is empty, it should return 0.
* If the value at the given key is not a list, it should return 0.
* If the key does not exist or its value is None, it should return 0.

```
dictionary = {'key': [4, 1, 8]}

output = get_sum_of_all_elements_at_key(dictionary, 'key')
print(output) # --> 13
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
    def test_00(self):
        # it should return a number
        dictionary = {'key': [4, 1, 8]}
        self.assertIsInstance(main.get_sum_of_all_elements_at_key(dictionary, 'key'), (int, float),
        msg = 'should return a number')

    def test_0(self):
        # it should return the sum of all the elements of the list located at key
        dictionary = {'key': [40, 10, 80]}
        self.assertEqual(main.get_sum_of_all_elements_at_key(dictionary, 'key'), 130,
        msg = 'should return the sum of all the elements of the list located at key')


    def test_1(self):
        # it should return 0 if the list is empty
        dictionary = {'key': []}
        self.assertEqual(main.get_sum_of_all_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the list is empty')


    def test_2(self):
        # it should return 0 if the property is not a list
        dictionary = {'key': 'nope'}
        self.assertEqual(main.get_sum_of_all_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the value is not a list')


    def test_3(self):
        # it should return 0 if the property does not exist
        dictionary = {'nope': 'nope'}
        self.assertEqual(main.get_sum_of_all_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the key does not exist')


```

### !end-tests

### !explanation
```python
from functools import reduce
def get_sum_of_all_elements_at_property(dictionary, key):
    value = dictionary.get(key)
    if not value: return 0
    try:
        return reduce(lambda x,y: x+y, value, 0)
    except:
        return 0
```
### !end-explanation

### !end-challenge
