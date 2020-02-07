# Objects 6

### !challenge

* type: code-snippet
* language: python3.6
* id: 0fa027aa-cf1a-4b02-a19e-5d43a6c83a32
* title: remove_array_values

### !question

Write a function called "removeListValues".

Given an dict, "removeListValues" removes any keys whose values are lists.

```
input = {'a': [1, 3, 4], 'b': 2, 'c': ['hi', 'there']}

output = removeListValues(input)
print(output) # --> {'b': 2}
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
        # it should remove any keys with values that are lists
        input = {'a': [1, 3, 4], 'b': 2, 'c': ['hi', 'there'], 'd':'hi'}
        output = {'b': 2, 'd':'hi'}
        self.assertEqual(main.removeListValues(input), output,
        msg = 'should remove any keys with values that are lists')


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 717ab908-571e-4a56-a675-ec540640c6ea
* title: remove_number_values

### !question

Write a function called "remove_number_values".

Given a dictionary, "remove_number_values" removes any keys whose values are numbers.

```
input = {'b': 2, 'c': ['hi', 'there'], 'd':'hi'}

output = remove_number_values(input)
print(output) # --> {'c': ['hi', 'there'], 'd':'hi'}
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
        # it should remove any properties with values that are numbers
        self.assertEqual(main.remove_number_values({'b': 2.9, 'c': ['hi', 'there'], 'd':4}), {'c': ['hi', 'there']},
        msg = 'should remove any keys with values that are numbers')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 8fa998a8-1847-4de4-aada-7c319bf55354
* title: remove_string_values

### !question

Write a function called "remove_string_values".

Given an dictionary, "remove_string_values" removes any keys on the given dictionary whose values are strings.

```
input = {'name': 'Sam', 'age': 20}

output = remove_string_values(input)
print(output) # -> {'age': 20}
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
        # it should remove any keys with values that are strings
        self.assertEqual(main.remove_string_values({'b': 2, 'c': ['hi', 'there'], 'd':'4'}), {'b': 2, 'c': ['hi', 'there']},
        msg = 'should remove any keys with values that are strings')

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
