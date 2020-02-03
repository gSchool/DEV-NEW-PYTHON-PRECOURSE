# Objects 13

### !challenge

* type: code-snippet
* language: python3.6
* id: be23ee89-7ea7-4f26-8194-5cc405d6b7a4
* title: get_sum_of_all_elements_at_property

### !question

Write a function called "get_sum_of_all_elements_at_property".

Given a dictionary and a key, "get_sum_of_all_elements_at_property" returns the sum of all the elements in the list located at the given key.

Notes:
* If the list is empty, it should return 0.
* If the property at the given key is not a list, it should return 0.
* If there is no property at the key, it should return 0.

```
obj = {'key': [4, 1, 8]}

output = get_sum_of_all_elements_at_property(obj, 'key')
print(output) # --> 13
```

### !end-question

### !placeholder

```python

def get_sum_of_all_elements_at_property(obj, key):
    # your code here
    pass

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test_00(self):
        # it should return a number
        obj = {'key': [4, 1, 8]}
        self.assertIsInstance(main.get_sum_of_all_elements_at_property(obj, 'key'), (int, float),
        msg = 'should return a number')

    def test_0(self):
        # it should return the sum of all the elements of the list located at key
        obj = {'key': [40, 10, 80]}
        self.assertEqual(main.get_sum_of_all_elements_at_property(obj, 'key'), 130,
        msg = 'should return the sum of all the elements of the list located at key')


    def test_1(self):
        # it should return 0 if the list is empty
        obj = {'key': []}
        self.assertEqual(main.get_sum_of_all_elements_at_property(obj, 'key'), 0,
        msg = 'should return 0 if the list is empty')


    def test_2(self):
        # it should return 0 if the property is not a list
        obj = {'key': 'nope'}
        self.assertEqual(main.get_sum_of_all_elements_at_property(obj, 'key'), 0,
        msg = 'should return 0 if the property is not a list')


    def test_3(self):
        # it should return 0 if the property does not exist
        obj = {'nope': 'nope'}
        self.assertEqual(main.get_sum_of_all_elements_at_property(obj, 'key'), 0,
        msg = 'should return 0 if the property does not exist')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
