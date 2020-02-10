# Dictionary 11

### !challenge

* type: code-snippet
* language: python3.6
* id: c0da71bc-093b-4eae-a574-d31aa2cb1109
* title: get_smallest_element_at_property

### !question

Write a function called "get_smallest_element_at_property".

Given a dictionary and a key, "get_smallest_element_at_property" returns the smallest element in the list located at the given key.

Notes:
* If the list is empty, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
obj = {'key': [2, 1, 5]}

output = get_smallest_element_at_property(obj, 'key')
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
        obj = {'list1': [2, 1, 5]}
        self.assertEqual(main.get_smallest_element_at_property(obj, "list1"), 1,
        msg = 'should return the smallest element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        obj = {'list1': []}
        self.assertIsNone(main.get_smallest_element_at_property(obj, "list1"),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        obj = {'list1': 'Nope'}
        self.assertIsNone(main.get_smallest_element_at_property(obj, "list1"),
        msg = 'should return None if the property is not a list')


    def test_3(self):
        # it should return None if the property does not exist
        obj = {'nope': [2, 1, 5]}
        self.assertIsNone(main.get_smallest_element_at_property(obj, "list1"),
        msg = 'should return None if the property does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: c63f092a-7fbe-496b-92f2-b3622b0da240
* title: get_largest_element_at_property

### !question

Write a function called "get_largest_element_at_property".

Given a dictionary and a key, "get_largest_element_at_property" returns the largest element in the list located at the given key.

Notes:
* If the list is empty, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
obj = {'key': [2, 1, 50]}

output = get_largest_element_at_property(obj, 'key')
print(output) # --> 50
```

### !end-question

### !placeholder

```python
def get_largest_element_at_property(obj, key):
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
        # it should return the largest element of the list located at key
        obj = {'key': [2, 1, 5]}
        self.assertEqual(main.get_largest_element_at_property(obj, 'key'), 5,
        msg = 'should return the largest element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        obj = {'key': []}
        self.assertIsNone(main.get_largest_element_at_property(obj, 'key'),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        obj = {'key': 'nope'}
        self.assertIsNone(main.get_largest_element_at_property(obj, 'key'),
        msg = 'should return None if the property is not a list')


    def test_3(self):
        # it should return None if the property does not exist
        obj = {'nope': [1,2,3]}        
        self.assertIsNone(main.get_largest_element_at_property(obj, 'key'),
        msg = 'should return None if the property does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: eb2ace99-f027-4845-9d09-529ef85273ca
* title: get_all_but_last_element_of_property

### !question

Write a function called "get_all_but_last_element_of_property".

Given a dictionary and a key, "get_all_but_last_element_of_property" returns a list containing all but the last element of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If the property at the given key is not a list, it return an empty list.
* If there is no property at the key, it should return an empty list.

```
obj = {'key': [2, 10, 50]}

output = get_all_but_last_element_of_property(obj, 'key')
print(output) # --> [2,10]
```

### !end-question

### !placeholder

```python
def get_all_but_last_element_of_property(obj, key):
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
        # it should return a list containing all but the last element of the list located at key
        obj = {'key': [2, 11, 50]}
        self.assertEqual(main.get_all_but_last_element_of_property(obj, "key"), [2, 11],
        msg = 'should return a list containing all but the last element of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only 1 element
        obj = {'key': [50]}
        self.assertEqual(main.get_all_but_last_element_of_property(obj, "key"), [],
        msg = 'should return an empty list if the list has only 1 element')


    def test_2(self):
        # it should return an empty list if the list is empty
        obj = {'key': []}
        self.assertEqual(main.get_all_but_last_element_of_property(obj, "key"), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the property is not a list
        obj = {'key': {8,9,0}}
        self.assertEqual(main.get_all_but_last_element_of_property(obj, "key"), [],
        msg = 'should return an empty list if the property is not a list')


    def test_4(self):
        # it should return an empty list if the property does not exist
        obj = {'Nope': [2, 1, 50]}
        self.assertEqual(main.get_all_but_last_element_of_property(obj, "key"), [],
        msg = 'should return an empty list if the property does not exist')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e43a1adc-c398-4090-9f18-be31fd425d6b
* title: get_element_of_array_property

### !question

Write a function called "get_element_of_array_property".

Given a dictionary, a key, and a numerical index, "get_element_of_array_property" returns the value of the element at the given index of the list located within the given dictionary at the given key.

Notes:
* If the list is empty, it should return None.
* If the given index is out of range of the list located at the given key, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
obj = {'key': ['Jamil', 'Albrey']}

output = get_element_of_array_property(obj, 'key', 0)
print(output) # --> 'Jamil'
```


### !end-question

### !placeholder

```python
def get_element_of_array_property(obj, key, index):
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
        # it should return the element at the index of the list at the key of the passed in dictionary
        obj = {'numbers': [1,0,2]}
        self.assertEqual(main.get_element_of_array_property(obj, "numbers", 1), 0,
        msg = 'should return the element at the index of the list at the key of the passed in dictionary')


    def test_1(self):
        # it should return None if the index is out of range
        obj = {'key': ['Jamil', 'Albrey']}
        self.assertIsNone(main.get_element_of_array_property(obj, 'key', 5),
        msg = 'should return None if the index is out of range')


    def test_2(self):
        # it should return None if the property at the key is not a list
        obj = {'name': 'Jamil'}
        self.assertIsNone(main.get_element_of_array_property(obj, "name", 0),
        msg = 'should return None if the property at the key is not a list')


    def test_3(self):
        # it should return None if there is no property at the key
        obj = {'key': ['Jamil', 'Albrey']}
        self.assertIsNone(main.get_element_of_array_property(obj, "what", 0),
        msg = 'should return None if there is no property at the key')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
