# Objects 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 5c68f405-579c-4427-8f13-9df8539009c7
* title: removeEvenValues

### !question

Write a function called "removeEvenValues".

Given an object, "removeEvenValues" removes any properties whose values are even numbers.

Do this in place and return the original object, do not construct a cloned object that omits the properties.

Example:

```
input = {'a': 2, 'b': 3, 'c': 4, 'd':'Texas'}

output = removeEvenValues(input)
print(output) # --> {'b': 3, 'd':'Texas'}
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
        # it should remove any keys with values that are even numbers
        input = {'a':1, 'b':2, 'c': 'montana', 'd':8}
        result = {'a':1, 'c': 'montana'}
        self.assertEqual(main.removeEvenValues(input), result,
        msg = 'should remove any keys with values that are even numbers')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 74b7a416-a4bc-4854-b870-0f92c6d57335
* title: countNumberOfKeys

### !question

Write a function called "countNumberOfKeys".

Given an object, "countNumberOfKeys" returns how many properties the given object has.

```
input = {'a': 1, 'b': 2, 'c': 3}

output = countNumberOfKeys(input)
print(output) # --> 3
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

    def test_1(self):
        # it should return the number of keys for an object
        self.assertEqual(main.countNumberOfKeys({'a': 1, 'b': 2, 'c': 3}), 3,
        msg = 'should return the number of keys for a dict')


    def test_2(self):
        # it should return 0 for an object with no keys
        self.assertEqual(main.countNumberOfKeys({}), 0,
        msg = 'should return 0 for a dict with no keys')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: e01182d1-9906-49b8-830d-bae725ad5b4b
* title: removeOddValues

### !question

Write a function called "removeOddValues".

Given an object, "removeOddValues" removes any keys whose values are odd numbers.

```
input = {'a': 1, 'b': 2, 'c': 3, 'd':'montana'}

output = removeOddValues(input)
print(output) # --> {'b': 2, 'd':'montana'}
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
        # it should remove any properties with values that are odd numbers
        self.assertEqual(main.removeOddValues({'a': 1, 'b': 2, 'c': 3, 'd':'Montana'}), {'b': 2, 'd':'Montana'},
        msg = 'should remove any key with values that are odd numbers')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
