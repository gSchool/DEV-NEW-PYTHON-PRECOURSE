# Objects 11

### !challenge

* type: code-snippet
* language: python3.6
* id: c0da71bc-093b-4eae-a574-d31aa2cb1109
* title: getSmallestElementAtProperty

### !question

Write a function called "getSmallestElementAtProperty".

Given a dictionary and a key, "getSmallestElementAtProperty" returns the smallest element in the list located at the given key.

Notes:
* If the list is empty, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
obj = {'key': [2, 1, 5]}

output = getSmallestElementAtProperty(obj, 'key')
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
        self.assertEqual(main.getSmallestElementAtProperty(obj, "list1"), 1,
        msg = 'should return the smallest element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        obj = {'list1': []}
        self.assertIsNone(main.getSmallestElementAtProperty(obj, "list1"),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        obj = {'list1': 'Nope'}
        self.assertIsNone(main.getSmallestElementAtProperty(obj, "list1"),
        msg = 'should return None if the property is not a list')


    def test_3(self):
        # it should return None if the property does not exist
        obj = {'nope': [2, 1, 5]}
        self.assertIsNone(main.getSmallestElementAtProperty(obj, "list1"),
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
* title: getLargestElementAtProperty

### !question

Write a function called "getLargestElementAtProperty".

Given a dictionary and a key, "getLargestElementAtProperty" returns the largest element in the list located at the given key.

Notes:
* If the list is empty, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
obj = {'key': [2, 1, 50]}

output = getLargestElementAtProperty(obj, 'key')
print(output) # --> 50
```

### !end-question

### !placeholder

```python
def getLargestElementAtProperty(obj, key):
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
        self.assertEqual(main.getLargestElementAtProperty(obj, 'key'), 5,
        msg = 'should return the largest element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        obj = {'key': []}
        self.assertIsNone(main.getLargestElementAtProperty(obj, 'key'),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        obj = {'key': 'nope'}
        self.assertIsNone(main.getLargestElementAtProperty(obj, 'key'),
        msg = 'should return None if the property is not a list')


    def test_3(self):
        # it should return None if the property does not exist
        obj = {'nope': [1,2,3]}        
        self.assertIsNone(main.getLargestElementAtProperty(obj, 'key'),
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
* title: getAllButLastElementOfProperty

### !question

Write a function called "getAllButLastElementOfProperty".

Given a dictionary and a key, "getAllButLastElementOfProperty" returns a list containing all but the last element of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If the property at the given key is not a list, it return an empty list.
* If there is no property at the key, it should return an empty list.

```
obj = {'key': [2, 10, 50]}

output = getAllButLastElementOfProperty(obj, 'key')
print(output) # --> [2,10]
```

### !end-question

### !placeholder

```python
def getAllButLastElementOfProperty(obj, key):
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
        self.assertEqual(main.getAllButLastElementOfProperty(obj, "key"), [2, 11],
        msg = 'should return a list containing all but the last element of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only 1 element
        obj = {'key': [50]}
        self.assertEqual(main.getAllButLastElementOfProperty(obj, "key"), [],
        msg = 'should return an empty list if the list has only 1 element')


    def test_2(self):
        # it should return an empty list if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getAllButLastElementOfProperty(obj, "key"), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the property is not a list
        obj = {'key': {8,9,0}}
        self.assertEqual(main.getAllButLastElementOfProperty(obj, "key"), [],
        msg = 'should return an empty list if the property is not a list')


    def test_4(self):
        # it should return an empty list if the property does not exist
        obj = {'Nope': [2, 1, 50]}
        self.assertEqual(main.getAllButLastElementOfProperty(obj, "key"), [],
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
* title: getElementOfArrayProperty

### !question

Write a function called "getElementOfArrayProperty".

Given a dictionary, a key, and a numerical index, "getElementOfArrayProperty" returns the value of the element at the given index of the list located within the given dictionary at the given key.

Notes:
* If the list is empty, it should return None.
* If the given index is out of range of the list located at the given key, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.

```
obj = {'key': ['Jamil', 'Albrey']}

output = getElementOfArrayProperty(obj, 'key', 0)
print(output) # --> 'Jamil'
```


### !end-question

### !placeholder

```python
def getElementOfArrayProperty(obj, key, index):
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
        self.assertEqual(main.getElementOfArrayProperty(obj, "numbers", 1), 0,
        msg = 'should return the element at the index of the list at the key of the passed in dictionary')


    def test_1(self):
        # it should return None if the index is out of range
        obj = {'key': ['Jamil', 'Albrey']}
        self.assertIsNone(main.getElementOfArrayProperty(obj, 'key', 5),
        msg = 'should return None if the index is out of range')


    def test_2(self):
        # it should return None if the property at the key is not a list
        obj = {'name': 'Jamil'}
        self.assertIsNone(main.getElementOfArrayProperty(obj, "name", 0),
        msg = 'should return None if the property at the key is not a list')


    def test_3(self):
        # it should return None if there is no property at the key
        obj = {'key': ['Jamil', 'Albrey']}
        self.assertIsNone(main.getElementOfArrayProperty(obj, "what", 0),
        msg = 'should return None if there is no property at the key')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
