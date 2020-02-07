# Objects 8

### !challenge

* type: code-snippet
* language: python3.6
* id: 4c450aa6-15da-4604-9aa9-b1f65d98850b
* title: getElementsGreaterThan10AtProperty

### !question

Write a function called "getElementsGreaterThan10AtProperty".

Given a dictionary and a key, "getElementsGreaterThan10AtProperty" returns a list containing the elements within the list, located at the given key, that are greater than 10.

Notes:
* If the list is empty, it should return an empty list.
* If the list contains no elements greater than 10, it should return an empty list.
* If the value at the given key is not a list, it should return an empty list.
* If there is no value at the key, it should return an empty list.

```
obj = {'key': [1, 20, 30]}

output = getElementsGreaterThan10AtProperty(obj, 'key')
print(output) # --> [20, 30]
```

### !end-question

### !placeholder

```python
def getElementsGreaterThan10AtProperty(obj, key):
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
        # it should return a list
        self.assertIsInstance(main.getElementsGreaterThan10AtProperty(
        {'key': [1, 20, 30]}, 'key'), list,
        msg = 'should return a list')

    def test_0(self):
        # "should return a list containing all the elements greater than 10 in the list located at key"
        obj = {'key': [10, 20, 30], 'key2':[30,30,30,30,30]}
        self.assertEqual(main.getElementsGreaterThan10AtProperty(obj, 'key'),
         [20,30],
        msg = "should return a list containing all the elements greater than 10 in the list located at key")


    def test_1(self):
        # "should return an empty list if the list has no elements greater than 10"
        obj = {'key': [10, 10, 10]}
        self.assertEqual(main.getElementsGreaterThan10AtProperty(obj, 'key'), [],
        msg = "should return an empty list if the list has no elements greater than 10")


    def test_2(self):
        # "should return an empty list if the list is empty"
        self.assertEqual(main.getElementsGreaterThan10AtProperty({'key': []}, 'key'), [],
        msg = "should return an empty list if the list is empty")


    def test_3(self):
        # "should return an empty list if the property is not a list"
        obj = {'key': "nope"}
        self.assertEqual(main.getElementsGreaterThan10AtProperty(obj, 'key'), [],
        msg = "should return an empty list if the value at key is not a list")

    def test_3(self):
        # "should return an empty list if the key does not exist"
        obj = {'nope': 'nopety nope'}
        self.assertEqual(main.getElementsGreaterThan10AtProperty(obj, 'key'), [],
        msg = "should return an empty list if the key does not exist")

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: aa75a574-cc22-47c9-9464-6d9cf0a3b7de
* title: getFirstElementOfProperty

### !question

Write a function called "getFirstElementOfProperty".

Given a dictionary and a key, "getFirstElementOfProperty" returns the first element of the list located at the given key.

Notes:
* If the list is empty, it should return None.
* If the value at the given key is not a list, it should return None.
* If there is no value at the key, it should return None.

```
dict1 = {'key': [1, 2, 4]}

output = getFirstElementOfProperty(dict1, 'key')
print(output) # --> 1
```

### !end-question

### !placeholder

```python
def getFirstElementOfProperty(dict1, key):
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
        # it should return the first element of the list located at key
        self.assertEqual(main.getFirstElementOfProperty({'key': [1, 2, 4]}, 'key'), 1,
        msg = 'should return the first element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        self.assertIsNone(main.getFirstElementOfProperty({'key': []}, 'key'),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return undefined if the value at key is not a list
        self.assertIsNone(main.getFirstElementOfProperty({'key': 'nope'}, 'key'),
        msg = 'should return None if the value at key is not a list')


    def test_3(self):
        # it should return None if the key does not exist
        self.assertIsNone(main.getFirstElementOfProperty({'nope': 'nope'}, 'key'),
        msg = 'should return None if the key does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 30a364d6-98d8-4819-a1b6-67cbc47e85de
* title: getNthElementOfProperty

### !question

Write a function called "getNthElementOfProperty".

Given a dictionary and a key, "getNthElementOfProperty" returns the nth element of a list located at the given key.

Notes:
* If the list is empty, it should return None.
* If n is out of range, it should return None.
* If the property at the given key is not a list, it should return None.
* If there is no property at the key, it should return None.
* Counting of elements starts at element zero.

```
obj = {'key': [1, 2, 6]}

output = getNthElementOfProperty(obj, 'key', 1)
print(output) # --> 2
```

### !end-question

### !placeholder

```python
def getNthElementOfProperty(obj, key, n):
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
        obj = {'items': [1, 2, 4]}
        self.assertEqual(main.getNthElementOfProperty(obj, 'items', 2), 4,
        msg = 'should return the nth element of the list located at key')


    def test_1(self):
        # it should return None if the n is out of range
        obj = {'items': [1, 2, 4]}
        self.assertIsNone(main.getNthElementOfProperty(obj, 'items', 8),
        msg = 'should return None if the n is out of range')


    def test_2(self):
        # it should return None if the list is empty
        obj = {'items': []}
        self.assertIsNone(main.getNthElementOfProperty(obj, 'items', 0),
        msg = 'should return None if the list is empty')


    def test_3(self):
        # it should return None if the key does not point to a list
        obj = {'items': -999}
        self.assertIsNone(main.getNthElementOfProperty(obj, 'items', 7),
        msg = 'should return None if the key does not point to a list')


    def test_4(self):
        # it should return None if the key does not exist
        obj = {'nope': 'nope'}
        self.assertIsNone(main.getNthElementOfProperty(obj, 'items', 8),
        msg = 'should return None if the key does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 0128dc86-b7a6-4022-8aa6-178ac9dd020b
* title: getLastElementOfProperty

### !question

Write a function called "getLastElementOfProperty".

Given a dictionary and a key, "getLastElementOfProperty" returns the last element of a list located at the given key.

Notes:
* If the list is empty, it should return undefined.
* if the property at the given key is not a list, it should return undefined.
* If there is no property at the key, it should return undefined.

```
obj = {'my_key': [1, 2, 5]}

output = getLastElementOfProperty(obj, 'my_key')
print(output) # --> 5
```

### !end-question

### !placeholder

```python
def getLastElementOfProperty(obj, key):
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
        # it should return the last element of the list located at key
        obj = {'key': [1, 2, 4]}
        self.assertEqual(main.getLastElementOfProperty(obj, 'key'), 4,
        msg = 'should return the last element of the list located at key')


    def test_1(self):
        # it should return None if the list is empty
        obj = {'key': []}
        self.assertIsNone(main.getLastElementOfProperty(obj, 'key'),
        msg = 'should return None if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        obj = {'key': 'Nope, nobody here but us chickens'}
        self.assertIsNone(main.getLastElementOfProperty(obj, 'key'),
        msg = 'should return None if the key does not point to a list')


    def test_3(self):
        # it should return None if the key does not exist
        obj = {'key2_not_key': [1, 2, 4]}
        self.assertIsNone(main.getLastElementOfProperty(obj, 'key'),
        msg = 'should return None if the key does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
