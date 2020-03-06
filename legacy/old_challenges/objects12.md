# Objects 12

### !challenge

* type: code-snippet
* language: python3.6
* id: 99bad9ce-b926-41aa-b33b-1ed86c6efc9d
* title: getProductOfAllElementsAtProperty

### !question

Write a function called "getProductOfAllElementsAtProperty".

Given a dictionary and a key, "getProductOfAllElementsAtProperty" returns the product of all the elements in the list located at the given key.

Notes:
* If the list is empty, it should return 0.
* If the property at the given key is not a list, it should return 0.
* If there is no property at the given key, it should return 0.

```
obj = {'key': [1, 2, 3, 4]}

output = getProductOfAllElementsAtProperty(obj, 'key')
print(output) # --> 24
```

### !end-question

### !placeholder

```python
def getProductOfAllElementsAtProperty(obj, key):
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
        #it should return the product of all the elements of the list located at key
        obj = {'key': [1, 2, 3, 4]}
        self.assertEqual(main.getProductOfAllElementsAtProperty(obj, 'key'), 24,
        msg = 'should return the product of all the elements of the list located at key')

    def test_00(self):
        # it should return an int
        obj = {'key': [1, 2, 3, 4]}
        self.assertIsInstance(main.getProductOfAllElementsAtProperty(obj, 'key'), (float, int),
        msg = 'it should return an int')


    def test_1(self):
        # it should return 0 if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getProductOfAllElementsAtProperty(obj, 'key'), 0,
        msg = 'should return 0 if the list is empty')


    def test_2(self):
        # it should return 0 if the value is not a list
        obj = {'key': 'nope'}
        self.assertEqual(main.getProductOfAllElementsAtProperty(obj, 'key'), 0,
        msg = 'should return 0 if the property is not a list')


    def test_3(self):
        # it should return 0 if the property does not exist
        obj = {'nope': [7,8,9]}
        self.assertEqual(main.getProductOfAllElementsAtProperty(obj, 'key'), 0,
        msg = 'should return 0 if the property does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
