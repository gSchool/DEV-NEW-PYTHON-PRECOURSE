# Dictionary 7

### !challenge

* type: code-snippet
* language: python3.6
* id: c0e2ea23-c0e1-47bf-b0c0-4cd29b1b4dcd
* title: get_elements_that_equal10_at_key

### !question

Write a function called "get_elements_that_equal10_at_key".

Given a dictionary and a key, "get_elements_that_equal10_at_key" returns a list containing all the elements of the list located at the given key that are equal to ten.

Notes:
* If the list is empty, it should return an empty list.
* If the list contains no elements that are equal to 10, it should return an empty list.
* If the value at the given key is not a list, it should return an empty list.
* If the key doesn't exist or its value is None, it should return an empty list.
* If there is a list at the given key you can assume it is a list of numbers.

```
dictionary = {'list_of_numbers': [1000, 10, 50, 10]}
output1 = get_elements_that_equal10_at_key(dictionary, 'list_of_numbers')
print(output1) # --> [10, 10]

dictionary = {'number': 10}
output2 = get_elements_that_equal10_at_key(dictionary, 'number')
print(output2) # --> []
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
            # it should return a list
            dictionary = {'key': [10,20,30,10,100]}
            self.assertIsInstance(main.get_elements_that_equal10_at_key(dictionary,
            'key'), list, msg = "should return a list")

    def test_1(self):
            # it should return a list containing all the elements that equal 10 in the list located at key
            dictionary = {'key': [10,20,30,10,100]}
            self.assertEqual(main.get_elements_that_equal10_at_key(dictionary, 'key'),
             [10,10], msg = "should return a list containing all the elements that equal 10 in the list located at key")        

    def test_2(self):
            # it "should return an empty list if the list has no elements that equal 10"
            dictionary = {'key': [20,100]}
            self.assertEqual(main.get_elements_that_equal10_at_key(dictionary, 'key'),
             [], msg = "should return an empty list if the list has no elements that equal 10")

    def test_3(self):
            # it "should return an empty list if the list is empty"
            dictionary = {'key': []}
            self.assertEqual(main.get_elements_that_equal10_at_key(dictionary, 'key'),
             [], msg = "should return an empty listy")

    def test_4(self):
            # it "should return an empty list if the value of the key is not a list"
            dictionary = {'key': 10}
            self.assertEqual(main.get_elements_that_equal10_at_key(dictionary, 'key'),
             [], msg = "should return an empty list if the value of the key is not a list")

    def test_4(self):
            # it "should return an empty list if the key does not exist"
            dictionary = {'nope': 10}
            self.assertEqual(main.get_elements_that_equal10_at_key(dictionary, 'key'),
             [], msg = "should return an empty list if the key does not exist")

```
### !end-tests

### !explanation
```python
def get_elements_that_equal10_at_value(dictionary, key):
    value = dictionary.get(key)
    if value is None or type(value) is not list: return []
    
    return [x for x in value if x == 10]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: fc295f5b-ed11-4bcc-8a6b-17f34618a97e
* title: get_elements_less_than_100_at_key

### !question

Write a function called "get_elements_less_than_100_at_key".

Given a dictionary and a key, "get_elements_less_than_100_at_key" returns a list containing all the elements of the list located at the given key that are less than 100.

Notes:
* If the list is empty, it should return an empty list.
* If the list contains no elements less than 100, it should return an empty list.
* If the value at the given key is not a list, it should return an empty list.
* If there is no value at the key, it should return an empty list.
* If there is a list at the given key you can assume it is a list of numbers.

```
dictionary = {'key': [1000, 20, 50, 500, 100]}

output = get_elements_less_than_100_at_key(dictionary, 'key')
print(output) # --> [20, 50]
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
        # it "should return a list containing all the elements less than 100 in the list located at key"
        dictionary = {'key': [1, 2, 100, 400]}
        self.assertEqual(main.get_elements_less_than_100_at_key(dictionary, 'key'), [1, 2],
        msg = "should return a list containing all the elements less than 100 in the list located at key")


    def test_1(self):
        # it should return None if the list is empty
        dictionary = {'key': []}
        self.assertEqual(main.get_elements_less_than_100_at_key(dictionary, 'key'),[],
        msg = 'should return an empty list if the list is empty')


    def test_2(self):
        # it should return None if the value is not a list
        dictionary = {'key': 'Nope, nobody here but us chickens'}
        self.assertEqual(main.get_elements_less_than_100_at_key(dictionary, 'key'),[],
        msg = 'should return an empty list if the key does not point to a list')

    def test_2_5(self):
        # it should return an empty list if the list is empty
        dictionary = {'key': []}
        self.assertEqual(main.get_elements_less_than_100_at_key(dictionary, 'key'),[],
        msg = 'it should return an empty list if the list is emptyy')

    def test_3(self):
        # it should return an empty list if the key does not exist
        dictionary = {'key2_not_key': [1, 2, 4]}
        self.assertEqual(main.get_elements_less_than_100_at_key(dictionary, 'key'),[],
        msg = 'should return an empty list if the key does not exist')

```

### !end-tests

### !explanation
```python
def get_elements_less_than_100_at_key(dictionary, key):
    value = dictionary.get(key)
    if value is None or type(value) is not list: return []
    
    return [x for x in value if x < 100]
```
### !end-explanation

### !end-challenge
