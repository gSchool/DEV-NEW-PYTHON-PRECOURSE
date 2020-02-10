# List Methods 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 241a37de-4069-418a-8f8d-64a40cc74f49
* title: remove_from_back_of_new

### !question

Write a function called "remove_from_back_of_new".

Given a list, "remove_from_back_of_new" returns a new list containing all but the last element of the given list. The original list should be unchanged.


```
lst = [1, 2, 3]
output = remove_from_back_of_new(lst)
print(output) # --> [1, 2]
print(lst) # --> [1, 2, 3]
```

### !end-question

### !placeholder

```python
#fill in the function definition below
# be sure to name the function according to the instructions

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it "should return an array"
        self.assertIs(type(main.remove_from_back_of_new([1,2,3])), list,
        msg = "it should return a list"  )

    def test2(self):
        # it "should return an array with the last element of the passed in array removed"
        self.assertEqual(main.remove_from_back_of_new([1, 2]), [1],
        msg = "should return a list with the last element of the passed in array removed")

    def test3(self):
        # it "should handle an empty array"
        self.assertEqual(main.remove_from_back_of_new([]), [],
        msg = "it should handle an empty list")

    def test4(self):
        # "it should leave the original list unmodified"
        input = [5,6,7]
        main.remove_from_back_of_new(input)
        self.assertEqual(input, [5,6,7],
        msg = "it should leave the original list unmodified")

```


### !end-tests

### !explanation
```python
def remove_from_back_of_new(lst):
    return lst[:-1]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 8a97c37b-54f3-4db0-845f-d2e7901e4244
* title: remove_from_front_of_new

### !question

Write a function called "remove_from_front_of_new".

Given a list, "remove_from_front_of_new" returns a new list containing all but the first element of the given list.



```
list1 = [1, 2, 3]
output = remove_from_front_of_new(list1)

print(output) # --> [2, 3]
print(list1) # --> [1, 2, 3]
```

### !end-question

### !placeholder

```python
#fill in the function definition below
# be sure to name the function according to the instructions

```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it "should return an list"
        self.assertIs(type(main.remove_from_front_of_new([1,2,3])), list,
        msg = "it should return a list" )

    def test2(self):
        # it
        self.assertEqual(main.remove_from_front_of_new([1,2,3,4,5]), [2,3,4,5],
        msg = "it should remove an element from the front of a list")

    def test3(self):
        # it "should handle an empty array"
        self.assertEqual(main.remove_from_front_of_new([]), [],
        msg = "it should handle an empty list")

    def test4(self):
        # it "should leave input unmodified"
        input = [12,13,14,15]
        main.remove_from_front_of_new(input)
        self.assertEqual(input, [12,13,14,15],
        msg = "should leave its input unmodified")
```

### !end-tests

### !explanation
```python
def remove_from_front_of_new(lst):
    return lst[1:]
```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: a3d52d99-9784-457b-8201-1210a097d449
* title: count_character

### !question

Write a function called "count_character".

Given a string input and a second string of a single character, "count_character" returns the number of occurrences of the given character in the given string.

```
string1 = 'I am a hacker'
output = count_character(string1, 'a')
print(output) # --> 3

string1 = 'I am a hacker !! '
output = count_character(string1, ' ')
print(output) # --> 5
```

### !end-question

### !placeholder

```python
#fill in the function definition below
# be sure to name the function according to the instructions


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it "should return the number of occurrences of a character in a string when the character exists"
        self.assertEqual(main.count_character("say what!?", "a"), 2,
        msg = "should return the number of occurrences of a character in a string when the character exists")

    def test3(self):
        # it "should return the number of occurrences of a character in a string when the character does not exist"
        self.assertEqual(main.count_character("say what!?", "e"), 0,
        msg = "it should return the number of occurrences of a character in a string when the character does not exist")

    def test4(self):
        # it "should return the number of occurrences of a non-alphanumeric character in a string when the character exists"
        self.assertEqual(main.count_character('I am a hacker!!!?! yes!', ' '), 4,
        msg = "it should return the number of occurrences of a non-alphanumeric character in a string when the character exists")
```

### !end-tests

### !explanation
```python
def count_character(string, target):
    count = 0
    for char in string:
        if char == target: count += 1
    return count
```
### !end-explanation

### !end-challenge
