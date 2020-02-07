# Objects 9

### !challenge

* type: code-snippet
* language: python3.6
* id: badca645-bd7e-42db-9a63-1b14d1bf99ec
* title: getOddLengthWordsAtProperty

### !question

Write a function called "getOddLengthWordsAtProperty".

Given a dictionary and a key, "getOddLengthWordsAtProperty" returns a list containing all the odd length word elements of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If it contains no odd length elements, it should return an empty list.
* If the property at the given key is not a list, it should return an empty list.
* If there is no property at the given key, it should return an empty list.

```
obj = {'key': ['It', 'has', 'some', 'words']}

output = getOddLengthWordsAtProperty(obj, 'key')
print(output) # --> ['has', 'words']
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
        obj = {'key': ['It', 'has', 'some', 'words']}
        self.assertIsInstance(main.getOddLengthWordsAtProperty(obj, 'key'), list,
        msg = 'should return a list')

    def test_0(self):
        # it should return a list containing all the odd length elements of the list located at key
        obj = {'key': ['a', 'night', 'to', 'remember']}
        self.assertEqual(main.getOddLengthWordsAtProperty(obj, 'key'), ["a", "night"],
        msg = 'should return a list containing all the odd length elements of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only even length elements
        obj = {'key': ['some', 'even', 'list']}
        self.assertEqual(main.getOddLengthWordsAtProperty(obj, 'key'), [],
        msg = 'it should return an empty list if the list has only even length elements')


    def test_2(self):
        # it should return an empty list if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getOddLengthWordsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the property is not a list
        obj = {'key':'nope'}
        self.assertEqual(main.getOddLengthWordsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the value at key is not a list')


    def test_4(self):
        # it should return an empty list if the property does not exist
        obj = {'nope':'nope'}
        self.assertEqual(main.getOddLengthWordsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the key does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: eae34f47-83d0-42c2-8ebc-9b72ae0482c3
* title: getAverageOfElementsAtProperty

### !question

Write a function called "getAverageOfElementsAtProperty".

Given a dictionary and a key, "getAverageOfElementsAtProperty" returns the average of all the elements in the list located at the given key.

Notes:
* If the list at the given key is empty, it should return 0.
* If the property at the given key is not a list, it should return 0.
* If there is no property at the given key, it should return 0.

```
obj = {'key': [1, 2, 3]}

output = getAverageOfElementsAtProperty(obj, 'key')
print(output) # --> 2
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
        # it should return an int or a float
        obj = {'key': [1, 2, 3]}
        self.assertIsInstance(main.getAverageOfElementsAtProperty(obj, 'key'),
        (int,float),
        msg = 'should return an int or a float')    

    def test_0(self):
        # it should return the average of all the elements of the list located at key
        obj = {'key': [0, 0, 30]}
        self.assertEqual(main.getAverageOfElementsAtProperty(obj, 'key'), 10,
        msg = 'should return the average of all the elements of the list located at key')


    def test_1(self):
        # it should return 0 if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getAverageOfElementsAtProperty(obj, 'key'), 0,
        msg = 'should return 0 if the list is empty')


    def test_2(self):
        # it should return 0 if the property is not a list
        obj = {'key': 'nope'}
        self.assertEqual(main.getAverageOfElementsAtProperty(obj, 'key'), 0,
        msg = 'should return 0 if the property is not a list')


    def test_3(self):
        # it should return 0 if the property does not exist
        obj = {'key1_not_key': [10,20,30]}
        self.assertEqual(main.getAverageOfElementsAtProperty(obj, 'key'), 0,
        msg = 'should return 0 if the property does not exist')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 6a474db4-3933-40f0-8af5-d52e55e0dff0
* title: getEvenLengthWordsAtProperty

### !question

Write a function called "getEvenLengthWordsAtProperty".

Given a dictionary and a key, "getEvenLengthWordsAtProperty" returns a list containing all the even length word elements of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If it contains no even length elements, it should return an empty list.
* If the property at the given key is not a list, it should return an empty list.
* If there is no property at the key, it should return an empty list.

```
obj = {key: ['a', 'long', 'game']}

output = getEvenLengthWordsAtProperty(obj, 'key')
print(output) # --> ['long', 'game']
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
        obj = {'key': ['It', 'has', 'some', 'words']}
        self.assertIsInstance(main.getEvenLengthWordsAtProperty(obj, 'key'), list,
        msg = 'should return a list')

    def test_0(self):
        # it should return a list containing all the even length elements of the list located at key
        obj = {'key': ['It', 'has', 'some', 'long','words']}
        self.assertEqual(main.getEvenLengthWordsAtProperty(obj, 'key'), ['some', 'long'],
        msg = 'should return a list containing all the even length elements of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only odd length elements
        obj = {'key': ['has','odd','words']}
        self.assertEqual(main.getEvenLengthWordsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the list has only odd length elements')


    def test_2(self):
        # it should return an empty list if the list is empty
        obj = {'key1': []}
        self.assertEqual(main.getEvenLengthWordsAtProperty(obj, 'key1'), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the property is not a list
        obj = {'nope':'nope'}
        self.assertEqual(main.getEvenLengthWordsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the property is not a list')


    def test_4(self):
        # it should return an empty list if the property does not exist
        obj = {'nope':['nope', 'still nope']}
        self.assertEqual(main.getEvenLengthWordsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the property does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
