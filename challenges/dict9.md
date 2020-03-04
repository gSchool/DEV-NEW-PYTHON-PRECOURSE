# Dictionary 9

### !challenge

* type: code-snippet
* language: python3.6
* id: badca645-bd7e-42db-9a63-1b14d1bf99ec
* title: get_odd_length_words_at_key

### !question

Write a function called "get_odd_length_words_at_key".

Given a dictionary and a key, "get_odd_length_words_at_key" returns a list containing all the odd length word elements of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If it contains no odd length elements, it should return an empty list.
* If the value at the given key is not a list, it should return an empty list.
* If there is no value at the given key, it should return an empty list.

```
dictionary = {'key': ['It', 'has', 'some', 'words']}

output = get_odd_length_words_at_key(dictionary, 'key')
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
        dictionary = {'key': ['It', 'has', 'some', 'words']}
        self.assertIsInstance(main.get_odd_length_words_at_key(dictionary, 'key'), list,
        msg = 'should return a list')

    def test_0(self):
        # it should return a list containing all the odd length elements of the list located at key
        dictionary = {'key': ['a', 'night', 'to', 'remember']}
        self.assertEqual(main.get_odd_length_words_at_key(dictionary, 'key'), ["a", "night"],
        msg = 'should return a list containing all the odd length elements of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only even length elements
        dictionary = {'key': ['some', 'even', 'list']}
        self.assertEqual(main.get_odd_length_words_at_key(dictionary, 'key'), [],
        msg = 'it should return an empty list if the list has only even length elements')


    def test_2(self):
        # it should return an empty list if the list is empty
        dictionary = {'key': []}
        self.assertEqual(main.get_odd_length_words_at_key(dictionary, 'key'), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the value is not a list
        dictionary = {'key':'nope'}
        self.assertEqual(main.get_odd_length_words_at_key(dictionary, 'key'), [],
        msg = 'should return an empty list if the value at key is not a list')


    def test_4(self):
        # it should return an empty list if the value does not exist
        dictionary = {'nope':'nope'}
        self.assertEqual(main.get_odd_length_words_at_key(dictionary, 'key'), [],
        msg = 'should return an empty list if the key does not exist')

```

### !end-tests

### !explanation
```python
def get_odd_length_words_at_key(dictionary, key):
    value = dictionary.get(key)
    if (value is None) or (not value) or (type(value) is not list):
        return []

    return [item for item in value if len(item) % 2 == 1]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: eae34f47-83d0-42c2-8ebc-9b72ae0482c3
* title: get_average_of_elements_at_key

### !question

Write a function called "get_average_of_elements_at_key".

Given a dictionary and a key, "get_average_of_elements_at_key" returns the average of all the elements in the list located at the given key.

Notes:
* If the list at the given key is empty, it should return 0.
* If the value at the given key is not a list, it should return 0.
* If there is no value at the given key, it should return 0.

```
dictionary = {'key': [1, 2, 3]}

output = get_average_of_elements_at_key(dictionary, 'key')
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
        dictionary = {'key': [1, 2, 3]}
        self.assertIsInstance(main.get_average_of_elements_at_key(dictionary, 'key'),
        (int,float),
        msg = 'should return an int or a float')    

    def test_0(self):
        # it should return the average of all the elements of the list located at key
        dictionary = {'key': [0, 0, 30]}
        self.assertEqual(main.get_average_of_elements_at_key(dictionary, 'key'), 10,
        msg = 'should return the average of all the elements of the list located at key')


    def test_1(self):
        # it should return 0 if the list is empty
        dictionary = {'key': []}
        self.assertEqual(main.get_average_of_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the list is empty')


    def test_2(self):
        # it should return 0 if the value is not a list
        dictionary = {'key': 'nope'}
        self.assertEqual(main.get_average_of_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the value is not a list')


    def test_3(self):
        # it should return 0 if the value does not exist
        dictionary = {'key1_not_key': [10,20,30]}
        self.assertEqual(main.get_average_of_elements_at_key(dictionary, 'key'), 0,
        msg = 'should return 0 if the value does not exist')


```

### !end-tests

### !explanation
```python
def get_average_of_elements_at_key(dictionary, key):
    value = dictionary.get(key)
    if (value is None) or (not value) or (type(value) is not list):
        return 0

    return sum(value) / len(value)
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 6a474db4-3933-40f0-8af5-d52e55e0dff0
* title: get_even_length_words_at_key

### !question

Write a function called "get_even_length_words_at_key".

Given a dictionary and a key, "get_even_length_words_at_key" returns a list containing all the even length word elements of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If it contains no even length elements, it should return an empty list.
* If the value at the given key is not a list, it should return an empty list.
* If there is no value at the key, it should return an empty list.

```
dictionary = {key: ['a', 'long', 'game']}

output = get_even_length_words_at_key(dictionary, 'key')
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
        dictionary = {'key': ['It', 'has', 'some', 'words']}
        self.assertIsInstance(main.get_even_length_words_at_key(dictionary, 'key'), list,
        msg = 'should return a list')

    def test_0(self):
        # it should return a list containing all the even length elements of the list located at key
        dictionary = {'key': ['It', 'has', 'some', 'long','words']}
        self.assertEqual(main.get_even_length_words_at_key(dictionary, 'key'), ['It','some', 'long'],
        msg = 'should return a list containing all the even length elements of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only odd length elements
        dictionary = {'key': ['has','odd','words']}
        self.assertEqual(main.get_even_length_words_at_key(dictionary, 'key'), [],
        msg = 'should return an empty list if the list has only odd length elements')


    def test_2(self):
        # it should return an empty list if the list is empty
        dictionary = {'key1': []}
        self.assertEqual(main.get_even_length_words_at_key(dictionary, 'key1'), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the value is not a list
        dictionary = {'nope':'nope'}
        self.assertEqual(main.get_even_length_words_at_key(dictionary, 'key'), [],
        msg = 'should return an empty list if the value is not a list')


    def test_4(self):
        # it should return an empty list if the value does not exist
        dictionary = {'nope':['nope', 'still nope']}
        self.assertEqual(main.get_even_length_words_at_key(dictionary, 'key'), [],
        msg = 'should return an empty list if the value does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
