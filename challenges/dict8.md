# Dictionary 8

### !challenge

* type: code-snippet
* language: python3.6
* id: 4c450aa6-15da-4604-9aa9-b1f65d98850b
* title: get_elements_greater_than_10_at_key

### !question

Write a function called "get_elements_greater_than_10_at_key".

Given a dictionary and a key, "get_elements_greater_than_10_at_key" returns a list containing the elements within the list, located at the given key, that are greater than 10.

Notes:
* If the list is empty it should return an empty list.
* If the list contains no elements greater than 10 it should return an empty list.
* If the value at the given key is not a list it should return an empty list.
* If there is no value at the key it should return an empty list.
* If there is a list at the given key you can assume it is a list of numbers.

```
dictionary = {'key': [1, 20, 30]}

output = get_elements_greater_than_10_at_key(dictionary, 'key')
print(output) # --> [20, 30]
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
        # it should return a list
        self.assertIsInstance(main.get_elements_greater_than_10_at_key(
        {'key': [1, 20, 30]}, 'key'), list,
        msg = 'should return a list')

    def test_0(self):
        # "should return a list containing all the elements greater than 10 in the list located at key"
        dictionary = {'key': [10, 20, 30], 'key2':[30,30,30,30,30]}
        self.assertEqual(main.get_elements_greater_than_10_at_key(dictionary, 'key'),
         [20,30],
        msg = "should return a list containing all the elements greater than 10 in the list located at key")


    def test_1(self):
        # "should return an empty list if the list has no elements greater than 10"
        dictionary = {'key': [10, 10, 10]}
        self.assertEqual(main.get_elements_greater_than_10_at_key(dictionary, 'key'), [],
        msg = "should return an empty list if the list has no elements greater than 10")


    def test_2(self):
        # "should return an empty list if the list is empty"
        self.assertEqual(main.get_elements_greater_than_10_at_key({'key': []}, 'key'), [],
        msg = "should return an empty list if the list is empty")


    def test_3(self):
        # "should return an empty list if the key is not a list"
        dictionary = {'key': "nope"}
        self.assertEqual(main.get_elements_greater_than_10_at_key(dictionary, 'key'), [],
        msg = "should return an empty list if the value at key is not a list")

    def test_3(self):
        # "should return an empty list if the key does not exist"
        dictionary = {'nope': 'nopety nope'}
        self.assertEqual(main.get_elements_greater_than_10_at_key(dictionary, 'key'), [],
        msg = "should return an empty list if the key does not exist")

```

### !end-tests

### !explanation
```python
def get_elements_greater_than_10_at_key(dictionary, key):
    value = dictionary.get(key)
    if value is None or type(value) is not list: return []
    return [x for x in value if x > 10]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: aa75a574-cc22-47c9-9464-6d9cf0a3b7de
* title: get_first_element_of_key

### !question

Write a function called "get_first_element_of_key".

Given a dictionary and a key, "get_first_element_of_key" returns the first element of the list located at the given key.

Notes:
* If the value of the given key is an empty list the function should return None.
* If the value at the given key is not a list the function should return None.
* If there is no value at the key, the function should return None.

```
dictionary = {'key': [1, 2, 4]}

output = get_first_element_of_key(dictionary, 'key')
print(output) # --> 1
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
        # it should return the first element of the list located at key
        self.assertEqual(main.get_first_element_of_key({'key': [1, 2, 4]}, 'key'), 1,
        msg = 'should return the first element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        self.assertIsNone(main.get_first_element_of_key({'key': []}, 'key'),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return undefined if the value at key is not a list
        self.assertIsNone(main.get_first_element_of_key({'key': 'nope'}, 'key'),
        msg = 'should return None if the value at key is not a list')


    def test_3(self):
        # it should return None if the key does not exist
        self.assertIsNone(main.get_first_element_of_key({'nope': 'nope'}, 'key'),
        msg = 'should return None if the key does not exist')

```

### !end-tests

### !explanation
```python
def get_first_element_of_key(dictionary, key):
    value = dictionary.get(key)
    if value is None or not value or type(value) is not list: return None
    return value[0]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 30a364d6-98d8-4819-a1b6-67cbc47e85de
* title: get_element_at_index_n_of_key

### !question

Write a function called "get_element_at_index_n_of_key".

Given a dictionary and a key, "get_element_at_index_n_of_key" returns the nth element of a list located at the given key.

Notes:
* If the value of the given key is an empty list, function should return None.
* If the value of the given key is a list but n is out of range, the function should return None.
* If the value at the given key is not a list, the function should return None.
* If the key does not exist in the dictionary, the function should return None.

```
dictionary = {'key': [1, 2, 6]}

output = get_element_at_index_n_of_key(dictionary, 'key', 1)
print(output) # --> 2
```

### !end-question

### !placeholder

```python
def get_element_at_index_n_of_key(dictionary, key, n):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return the nth element of the list located at key
        dictionary = {'items': [1, 2, 4]}
        self.assertEqual(main.get_element_at_index_n_of_key(dictionary, 'items', 2), 4,
        msg = 'should return the nth element of the list located at key')


    def test_1(self):
        # it should return None if the n is out of range
        dictionary = {'items': [1, 2, 4]}
        self.assertIsNone(main.get_element_at_index_n_of_key(dictionary, 'items', 8),
        msg = 'should return None if the n is out of range')


    def test_2(self):
        # it should return None if the list is empty
        dictionary = {'items': []}
        self.assertIsNone(main.get_element_at_index_n_of_key(dictionary, 'items', 0),
        msg = 'should return None if the list is empty')


    def test_3(self):
        # it should return None if the key does not point to a list
        dictionary = {'items': -999}
        self.assertIsNone(main.get_element_at_index_n_of_key(dictionary, 'items', 7),
        msg = 'should return None if the key does not point to a list')


    def test_4(self):
        # it should return None if the key does not exist
        dictionary = {'nope': 'nope'}
        self.assertIsNone(main.get_element_at_index_n_of_key(dictionary, 'items', 8),
        msg = 'should return None if the key does not exist')

```

### !end-tests

### !explanation
```python
def get_element_at_index_n_of_key(dictionary, key, n):
    value = dictionary.get(key)
    if value is None or not value or (type(value) is not list) or (len(value) <= n):
        return None
    return value[n]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 0128dc86-b7a6-4022-8aa6-178ac9dd020b
* title: get_last_element_of_key

### !question

Write a function called "get_last_element_of_key".

Given a dictionary and a key, "get_last_element_of_key" returns the last element of a list located at the given key.

Notes:
* If the value of the given key is an empty list, function should return None.
* If the value of the given key is a list but n is out of range, the function should return None.
* If the value at the given key is not a list, the function should return None.
* If the key does not exist in the dictionary, the function should return None.

```
dictionary = {'my_key': [1, 2, 5]}

output = get_last_element_of_key(dictionary, 'my_key')
print(output) # --> 5
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
        # it should return the last element of the list located at key
        dictionary = {'key': [1, 2, 4]}
        self.assertEqual(main.get_last_element_of_key(dictionary, 'key'), 4,
        msg = 'should return the last element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        dictionary = {'key': []}
        self.assertIsNone(main.get_last_element_of_key(dictionary, 'key'),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the key is not a list
        dictionary = {'key': 'Nope, nobody here but us chickens'}
        self.assertIsNone(main.get_last_element_of_key(dictionary, 'key'),
        msg = 'should return None if the key does not point to a list')


    def test_3(self):
        # it should return None if the key does not exist
        dictionary = {'key2_not_key': [1, 2, 4]}
        self.assertIsNone(main.get_last_element_of_key(dictionary, 'key'),
        msg = 'should return None if the key does not exist')

```

### !end-tests

### !explanation
```python
def get_last_element_of_key(dictionary, key):
    value = dictionary.get(key)
    if value is None or not value or (type(value) is not list):
        return None
    return value[-1]



```
### !end-explanation

### !end-challenge
