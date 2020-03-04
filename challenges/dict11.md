# Dictionary 11

### !challenge

* type: code-snippet
* language: python3.6
* id: c0da71bc-093b-4eae-a574-d31aa2cb1109
* title: get_smallest_element_at_key

### !question

Write a function called "get_smallest_element_at_key".

Given a dictionary and a key, "get_smallest_element_at_key" returns the smallest element in the list located at the given key.

Notes:
* If the list is empty, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
dictionary = {'key': [2, 1, 5]}

output = get_smallest_element_at_key(dictionary, 'key')
print(output) # --> 1
```

### !end-question

### !placeholder

```python


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):

    def test_0(self):
        # it should return the smallest element of the list located at key
        dictionary = {'list1': [2, 1, 5]}
        self.assertEqual(main.get_smallest_element_at_key(dictionary, "list1"), 1,
        msg = 'should return the smallest element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        dictionary = {'list1': []}
        self.assertIsNone(main.get_smallest_element_at_key(dictionary, "list1"),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        dictionary = {'list1': 'Nope'}
        self.assertIsNone(main.get_smallest_element_at_key(dictionary, "list1"),
        msg = 'should return None if the property is not a list')


    def test_3(self):
        # it should return None if the property does not exist
        dictionary = {'nope': [2, 1, 5]}
        self.assertIsNone(main.get_smallest_element_at_key(dictionary, "list1"),
        msg = 'should return None if the property does not exist')

```

### !end-tests

### !explanation
```python
def get_smallest_element_at_key(dictionary):
    value = dictionary.get(key)
    if not value or type(value) is not list: return None
    return min(value)
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c63f092a-7fbe-496b-92f2-b3622b0da240
* title: get_largest_element_at_key

### !question

Write a function called "get_largest_element_at_key".

Given a dictionary and a key, "get_largest_element_at_key" returns the largest element in the list located at the given key.

Notes:
* If the list is empty, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
dictionary = {'key': [2, 1, 50]}

output = get_largest_element_at_key(dictionary, 'key')
print(output) # --> 50
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
        # it should return the largest element of the list located at key
        dictionary = {'key': [2, 1, 5]}
        self.assertEqual(main.get_largest_element_at_key(dictionary, 'key'), 5,
        msg = 'should return the largest element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        dictionary = {'key': []}
        self.assertIsNone(main.get_largest_element_at_key(dictionary, 'key'),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        dictionary = {'key': 'nope'}
        self.assertIsNone(main.get_largest_element_at_key(dictionary, 'key'),
        msg = 'should return None if the property is not a list')


    def test_3(self):
        # it should return None if the property does not exist
        dictionary = {'nope': [1,2,3]}        
        self.assertIsNone(main.get_largest_element_at_key(dictionary, 'key'),
        msg = 'should return None if the property does not exist')

```

### !end-tests

### !explanation
```python
def get_largest_element_at_key(dictionary, key):
    value = dictionary.get(key)
    if not value or type(value) is not list: return None
    return max(value)
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: eb2ace99-f027-4845-9d09-529ef85273ca
* title: get_all_but_last_element_of_key

### !question

Write a function called "get_all_but_last_element_of_key".

Given a dictionary and a key, "get_all_but_last_element_of_key" returns a list containing all but the last element of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If the property at the given key is not a list, it return an empty list.
* If there is no property at the key, it should return an empty list.

```
dictionary = {'key': [2, 10, 50]}

output = get_all_but_last_element_of_key(dictionary, 'key')
print(output) # --> [2,10]
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
        # it should return a list containing all but the last element of the list located at key
        dictionary = {'key': [2, 11, 50]}
        self.assertEqual(main.get_all_but_last_element_of_key(dictionary, "key"), [2, 11],
        msg = 'should return a list containing all but the last element of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only 1 element
        dictionary = {'key': [50]}
        self.assertEqual(main.get_all_but_last_element_of_key(dictionary, "key"), [],
        msg = 'should return an empty list if the list has only 1 element')


    def test_2(self):
        # it should return an empty list if the list is empty
        dictionary = {'key': []}
        self.assertEqual(main.get_all_but_last_element_of_key(dictionary, "key"), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the property is not a list
        dictionary = {'key': {8,9,0}}
        self.assertEqual(main.get_all_but_last_element_of_key(dictionary, "key"), [],
        msg = 'should return an empty list if the property is not a list')


    def test_4(self):
        # it should return an empty list if the property does not exist
        dictionary = {'Nope': [2, 1, 50]}
        self.assertEqual(main.get_all_but_last_element_of_key(dictionary, "key"), [],
        msg = 'should return an empty list if the property does not exist')


```

### !end-tests

### !explanation
```python
def get_all_but_last_element_of_key(dictionary, key):
    value = dictionary.get(key)
    if not value or type(value) is not list: return []
    return value[:-1]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e43a1adc-c398-4090-9f18-be31fd425d6b
* title: get_element_of_list_at_key

### !question

Write a function called "get_element_of_list_at_key".

Given a dictionary, a key, and a numerical index, "get_element_of_list_at_key" returns the value of the element at the given index of the list located within the given dictionary at the given key.

Notes:
* If the list is empty, it should return None.
* If the given index is out of range of the list located at the given key, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
dictionary = {'key': ['Jamil', 'Albrey']}

output = get_element_of_list_at_key(dictionary, 'key', 0)
print(output) # --> 'Jamil'
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
        # it should return the element at the index of the list at the key of the passed in dictionary
        dictionary = {'numbers': [1,0,2]}
        self.assertEqual(main.get_element_of_list_at_key(dictionary, "numbers", 1), 0,
        msg = 'should return the element at the index of the list at the key of the passed in dictionary')


    def test_1(self):
        # it should return None if the index is out of range
        dictionary = {'key': ['Jamil', 'Albrey']}
        self.assertIsNone(main.get_element_of_list_at_key(dictionary, 'key', 5),
        msg = 'should return None if the index is out of range')


    def test_2(self):
        # it should return None if the property at the key is not a list
        dictionary = {'name': 'Jamil'}
        self.assertIsNone(main.get_element_of_list_at_key(dictionary, "name", 0),
        msg = 'should return None if the property at the key is not a list')


    def test_3(self):
        # it should return None if there is no property at the key
        dictionary = {'key': ['Jamil', 'Albrey']}
        self.assertIsNone(main.get_element_of_list_at_key(dictionary, "what", 0),
        msg = 'should return None if there is no property at the key')

```

### !end-tests

### !explanation
```python
def get_element_of_list_at_key(dictionary, key, index):
    value = dictionary.get(key)
    if not value or type(value) is not list: return None
    if len(value) > index:
        return value[index]
    else:
        return None
```
### !end-explanation

### !end-challenge
