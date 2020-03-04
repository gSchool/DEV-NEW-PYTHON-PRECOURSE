# Dictionary 12

### !challenge

* type: code-snippet
* language: python3.6
* id: 99bad9ce-b926-41aa-b33b-1ed86c6efc9d
* title: get_product_of_all_elements_at_key

### !question

Write a function called "get_product_of_all_elements_at_key".

Given a dictionary and a key, "get_product_of_all_elements_at_key" returns the product of all the elements in the list located at the given key.

Notes:

* If the list exists at the key, you can assume it contains only numbers.
* If the list is empty, it should return 0.
* If the value at the given key is not a list, it should return 0.
* If the key does not exist or its value is None, it should return 0.

```
dictionary = {'key': [1, 2, 3, 4]}

output = get_product_of_all_elements_at_key(dictionary, 'key')
print(output) # --> 24
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
        #it should return the product of all the elements of the list located at key
        dictionary = {'key': [1, 2, 3, 4]}
        self.assertEqual(main.get_product_of_all_elements_at_key(dictionary, 'key'), 24,
        msg = 'should return the product of all the elements of the list located at key')

    def test_00(self):
        # it should return an int
        dictionary = {'key': [1, 2, 3, 4]}
        self.assertIsInstance(main.get_product_of_all_elements_at_key(dictionary, 'key'), (float, int),
        msg = 'it should return an int')


    def test_1(self):
        # it should return 0 if the list is empty
        dictionary = {'key': []}
        self.assertEqual(main.get_product_of_all_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the list is empty')


    def test_2(self):
        # it should return 0 if the value is not a list
        dictionary = {'key': 'nope'}
        self.assertEqual(main.get_product_of_all_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the value at the key is not a list')


    def test_3(self):
        # it should return 0 if the property does not exist
        dictionary = {'nope': [7,8,9]}
        self.assertEqual(main.get_product_of_all_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the key does not exist')

```

### !end-tests

### !explanation
```python
from functools import reduce
def get_product_of_all_elements_at_key(dictionary, key):
    value = dictionary.get(key)
    if not value: return 0
    try:
        return reduce(lambda x,y: x * y, value, 1)
    except:
        return 0
```
### !end-explanation

### !end-challenge
