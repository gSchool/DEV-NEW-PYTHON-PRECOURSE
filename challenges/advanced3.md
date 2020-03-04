# Advanced 3

### !challenge

* type: code-snippet
* language: python3.6
* id: e7a0d366-b299-4c2a-81ac-45fcbacd2b54
* title: select

### !question

Write a function called "select".

Given list and a dictionary, "select" returns a *new* dictionary whose keys are those in the given dictionary which are present in the given list.

Notes:
* If keys are present in the given list, but are not in the given dictionary, it should ignore them.
* It does not modify the passed in dictionary.

```
input_list = ['a', 'c', 'e']
input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

output = select(input_list, input_dict)
print(output) # --> {'a': 1, 'c': 3}

print(input_dict) # --> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
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
        # it should return a dict
        self.assertEqual(type(main.select(['a', 'c', 'e'], {'a': 1, 'b': 2})), dict,
        msg = 'should return a dict')


    def test_1(self):
        # it should return a dict with key in from the passed in dict whose keys are ALSO present in the given list
        input_list = ['a', 'c', 'e']
        input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(main.select(input_list, input_dict), {'a': 1, 'c': 3},
        msg = 'it should return a dict with keys in BOTH the passed in dict and the given list')


    def test_2(self):
        # it should not modify the passed in dict
        input_list = ['a', 'c', 'e']
        input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        main.select(input_list, input_dict)    
        self.assertEqual(input_dict, {'a': 1, 'b': 2, 'c': 3, 'd': 4},
        msg = 'should not modify the passed in dict')

```

### !end-tests

### !explanation
```python
def select(input_list, input_dict):
    result = {}
    for key in input_list:
        if key in input_dict:
            result[key] = input_dict[key]
    return result

```
### !end-explanation

### !end-challenge
