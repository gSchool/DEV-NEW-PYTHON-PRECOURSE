# Objects 7

### !challenge

* type: code-snippet
* language: python3.6
* id: c0e2ea23-c0e1-47bf-b0c0-4cd29b1b4dcd
* title: getElementsThatEqual10AtProperty

### !question

Write a function called "getElementsThatEqual10AtProperty".

Given a dictionary and a key, "getElementsThatEqual10AtProperty" returns a list containing all the elements of the list located at the given key that are equal to ten.

Notes:
* If the list is empty, it should return an empty list.
* If the list contains no elements that are equal to 10, it should return an empty list.
* If the value at the given key is not a list, it should return an empty list.
* If the key doesn't exist or its value is None, it should return an empty list.

```
obj1 = {'key': [1000, 10, 50, 10]}
output1 = getElementsThatEqual10AtProperty(obj1, 'key')
print(output1) # --> [10, 10]

obj2 = {'key': 10}
output2 = getElementsThatEqual10AtProperty(obj2, 'key')
print(output2) # --> []
```

### !end-question

### !placeholder

```python

def getElementsThatEqual10AtProperty(obj, key):
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
            # it should return a list
            obj = {'key': [10,20,30,10,100]}
            self.assertIsInstance(main.getElementsThatEqual10AtProperty(obj,
            'key'), list, msg = "should return a list")

    def test_1(self):
            # it should return a list containing all the elements that equal 10 in the list located at key
            obj = {'key': [10,20,30,10,100]}
            self.assertEqual(main.getElementsThatEqual10AtProperty(obj, 'key'),
             [10,10], msg = "should return a list containing all the elements that equal 10 in the list located at key")        

    def test_2(self):
            # it "should return an empty list if the list has no elements that equal 10"
            obj = {'key': [20,100]}
            self.assertEqual(main.getElementsThatEqual10AtProperty(obj, 'key'),
             [], msg = "should return an empty list if the list has no elements that equal 10")

    def test_3(self):
            # it "should return an empty list if the list is empty"
            obj = {'key': []}
            self.assertEqual(main.getElementsThatEqual10AtProperty(obj, 'key'),
             [], msg = "should return an empty listy")

    def test_4(self):
            # it "should return an empty list if the value of the key is not a list"
            obj = {'key': 10}
            self.assertEqual(main.getElementsThatEqual10AtProperty(obj, 'key'),
             [], msg = "should return an empty list if the value of the key is not a list")

    def test_4(self):
            # it "should return an empty list if the key does not exist"
            obj = {'nope': 10}
            self.assertEqual(main.getElementsThatEqual10AtProperty(obj, 'key'),
             [], msg = "should return an empty list if the key does not exist")

```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: fc295f5b-ed11-4bcc-8a6b-17f34618a97e
* title: getElementsLessThan100AtProperty

### !question

Write a function called "getElementsLessThan100AtProperty".

Given a dictionary and a key, "getElementsLessThan100AtProperty" returns a list containing all the elements of the list located at the given key that are less than 100.

Notes:
* If the list is empty, it should return an empty list.
* If the list contains no elements less than 100, it should return an empty list.
* If the property at the given key is not a list, it should return an empty list.
* If there is no property at the key, it should return an empty list.

```
obj = {'key': [1000, 20, 50, 500, 100]}

output = getElementsLessThan100AtProperty(obj, 'key')
print(output) # --> [20, 50]
```

### !end-question

### !placeholder

```python
def getElementsLessThan100AtProperty(obj, key):
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
        # it "should return a list containing all the elements less than 100 in the list located at key"
        obj = {'key': [1, 2, 100, 400]}
        self.assertEqual(main.getElementsLessThan100AtProperty(obj, 'key'), [1, 2],
        msg = "should return a list containing all the elements less than 100 in the list located at key")


    def test_1(self):
        # it should return None if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getElementsLessThan100AtProperty(obj, 'key'),[],
        msg = 'should return an empty list if the list is empty')


    def test_2(self):
        # it should return None if the property is not a list
        obj = {'key': 'Nope, nobody here but us chickens'}
        self.assertEqual(main.getElementsLessThan100AtProperty(obj, 'key'),[],
        msg = 'should return an empty list if the key does not point to a list')

    def test_2_5(self):
        # it should return an empty list if the list is empty
        obj = {'key': []}
        self.assertEqual(main.getElementsLessThan100AtProperty(obj, 'key'),[],
        msg = 'it should return an empty list if the list is emptyy')

    def test_3(self):
        # it should return an empty list if the key does not exist
        obj = {'key2_not_key': [1, 2, 4]}
        self.assertEqual(main.getElementsLessThan100AtProperty(obj, 'key'),[],
        msg = 'should return an empty list if the key does not exist')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
