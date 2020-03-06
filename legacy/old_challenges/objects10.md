# Objects 10

### !challenge

* type: code-snippet
* language: python3.6
* id: 89965766-9afc-4a39-a053-974ea791eed3
* title: getSquaredElementsAtProperty

### !question

Write a function called "getSquaredElementsAtProperty".

Given a dictionary and a key, "getSquaredElementsAtProperty" returns a list containing all the squared elements of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If the property at the given key is not a list, it should return an empty list.
* If there is no property at the key, it should return an empty list.

```
obj = {'key': [2, 1, 5]}

output = getSquaredElementsAtProperty(obj, 'key')
print(output) # --> [4, 1, 25]
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
        obj = {'key': [1, 2, 7]}
        self.assertIsInstance(main.getSquaredElementsAtProperty(obj, 'key'), list, msg = 'should return a list')


    def test_0(self):
        # it should return a list containing all the squared elements of the list located at key
        obj = {'key': [1, 2, 7]}
        self.assertEqual(main.getSquaredElementsAtProperty(obj, 'key'), [1, 4, 49],
        msg = 'should return a list containing all the squared elements of the list located at key')


    def test_1(self):
        # it should return an empty list if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getSquaredElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the list is empty')


    def test_2(self):
        # it should return an empty list if the property is not a list
        obj = {'key': 'nope'}
        self.assertEqual(main.getSquaredElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the value is not a list')


    def test_3(self):
        # it should return an empty list if the property does not exist
        obj = {'nope': [2,2,4]}
        self.assertEqual(main.getSquaredElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the key does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 10993279-1166-4e9d-813b-aff9705fab7b
* title: getOddElementsAtProperty

### !question

Write a function called "getOddElementsAtProperty".

Given a dictionary and a key, "getOddElementsAtProperty" returns a list containing all the odd elements of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If it contains no odd elements, it should return an empty list.
* If the property at the given key is not a list, it should return an empty list.
* If there is no property at the key, it should return an empty list.

```
obj = {'key': [1, 2, 3, 4, 5]}

output = getOddElementsAtProperty(obj, 'key')
print(output) # --> [1, 3, 5]
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
        obj = {'key': [1, 2, 7]}
        self.assertIsInstance(main.getOddElementsAtProperty(obj, 'key'), list, msg = 'should return a list')

    def test_0(self):
        # it should return a list containing all the odd elements of the list located at key
        obj = {'key': [1, 2, 7]}
        self.assertEqual(main.getOddElementsAtProperty(obj, 'key'), [1, 7],
        msg = 'should return a list containing all the odd elements of the list located at key')

    def test_1(self):
        # it should return an empty list if the list has only no odd elements
        obj = {'key': [2, 2, 4]}
        self.assertEqual(main.getOddElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the list has no odd elements')


    def test_2(self):
        # it should return an empty list if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getOddElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the property is not a list
        obj = {'key': 'nope'}
        self.assertEqual(main.getOddElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the property is not a list')


    def test_4(self):
        # it should return an empty list if the property does not exist
        obj = {'nope': [2, 2, 4]}
        self.assertEqual(main.getOddElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the property does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: f55d3c6d-ea58-477c-9682-4573e7f48e75
* title: getEvenElementsAtProperty

### !question

Write a function called "getEvenElementsAtProperty".

Given a dictionary and a key, "getEvenElementsAtProperty" returns a list containing all the even elements of the list located at the given key.

Notes:
* If the list is empty, it should return an empty list.
* If the list contains no even elements, it should return an empty list.
* If the property at the given key is not a list, it should return an empty list.
* If there is no property at the given key, it should return an empty list.

```
obj = :key: [1000, 11, 50, 17]

output = getEvenElementsAtProperty(obj, 'key')
print(output) # --> [1000, 50]
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
        obj = {'key': [1, 2, 7]}
        self.assertIsInstance(main.getEvenElementsAtProperty(obj, 'key'), list, msg = 'should return a list')

    def test_0(self):
        # it should return a list containing all the even elements of the list located at key
        obj = {'key': [1, 2, 4, 7]}
        self.assertEqual(main.getEvenElementsAtProperty(obj, 'key'), [2, 4],
        msg = 'should return a list containing all the even elements of the list located at key')


    def test_1(self):
        # it should return an empty list if the list has only no even elements
        obj = {'key': [1, 3, 7]}
        self.assertEqual(main.getEvenElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the list has no even elements')


    def test_2(self):
        # it should return an empty list if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getEvenElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the list is empty')


    def test_3(self):
        # it should return an empty list if the property is not a list
        obj = {'key': 'nope'}
        self.assertEqual(main.getEvenElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the property is not a list')


    def test_4(self):
        # it should return an empty list if the property does not exist
        obj = {'nope': [1, 2, 7]}
        self.assertEqual(main.getEvenElementsAtProperty(obj, 'key'), [],
        msg = 'should return an empty list if the property does not exist')
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
