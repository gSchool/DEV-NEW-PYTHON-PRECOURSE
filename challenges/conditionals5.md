# Conditionals 5

### !challenge

* type: code-snippet
* language: python3.6
* id: 9a167567-dfa8-4854-a21c-3d773b0c1ef5
* title: is_odd_length

### !question

Write a function called "is_odd_length".

Given a word, "is_odd_length" returns whether the length of the given word is odd.

```
output = is_odd_length('special')
print(output) # --> True

output = is_odd_length('')
print(output) # --> False

```

### !end-question

### !placeholder

```python
def is_odd_length(word):
    # your code here
    pass



```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it "should return a boolean"
        self.assertIs(type(main.is_odd_length("wow")), bool, msg="it should return a boolean")

    def test2(self):
        #it "should return False if the length of the word is even"
        self.assertFalse(main.is_odd_length("arrays"), msg="should return False if the length of the word is even")

    def test3(self):
        #it "should return True if the length of the word is odd"
        self.assertTrue(main.is_odd_length("wow"), msg="should return True if the length of the word is odd")

    def test4(self):
        #it "should return False if the string is empty"
        self.assertFalse(main.is_odd_length(''), msg="should return False if passed an empty string")
```


### !end-tests

### !explanation
```python
def is_odd_length(word):
    return len(word) % 2 == 1

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 3e56d53e-7025-45e4-a697-fd2851b6495d
* title: is_even_length

### !question

Write a function called "is_even_length".

Given a word, "is_even_length" returns whether the length of the word is even.

```
output = is_even_length('wow')
print(output) # --> False

output = is_even_length('')
print(output) # --> True
```

### !end-question

### !placeholder

```python
def is_even_length(word):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it "should return a boolean"
        self.assertIs(type(main.is_even_length("wow")), bool, msg="it should return a boolean")

        def test2(self):
            #it "should return False if the length of the word is odd"
            self.assertFalse(main.is_even_length("wow"), msg="should return False if the length of the word is even")

        def test3(self):
            #it "should return True if the length of the word is odd"
            self.assertTrue(main.is_even_length("arrays"), msg="should return True if the length of the word is odd")

        def test4(self):
            #it "should return True if the string is empty"
            self.assertFalse(main.is_even_length(''), msg="should return True if passed an empty string")
```


### !end-tests

### !explanation
```python
def is_even_length(word):
    return len(word) % 2 == 0

```
### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python3.6
* id: 547a6787-3d47-4a09-83d6-ca86e7aa26c9
* title: is_even_and_greater_than_10

### !question

Write a function called "is_even_and_greater_than_10".

Given a number, "is_even_and_greater_than_10" returns whether it is both even and greater than 10.

```
output = is_even_and_greater_than_10(13)
print(output) # --> False
```

### !end-question

### !placeholder

```python
def is_even_and_greater_than_10(num):
    # your code here
    pass


```

### !end-placeholder

### !tests

```python
import main
import unittest

class TestScript(unittest.TestCase):
    def test1(self):
        # it should return a boolean
        self.assertIs(type(main.is_even_and_greater_than_10(40)), bool, msg="")

    def test2(self):
        #it "should return True if the number is even and greater than 10"
        self.assertTrue(main.is_even_and_greater_than_10(40), msg="should return True if the number is even and greater than 10")

    def test3(self):
        #it "should return False if the number is odd"
        self.assertFalse(main.is_even_and_greater_than_10(99), msg="it should return False if the number is odd")


    def test4(self):
        #it "should return False if the number is odd"
        self.assertFalse(main.is_even_and_greater_than_10(17), msg="it should return False if the number is odd")

    def test5(self):
        #it "should return False if the number is 10"
        self.assertFalse(main.is_even_and_greater_than_10(10), msg="it should return False if the number is 10")

    def test6(self):
        #it "should return False if the number is less than 10"
        self.assertFalse(main.is_even_and_greater_than_10(4), msg="it should return False if the number is less than 10")    

```

### !end-tests

### !explanation
```python
def is_even_and_greater_than_10(num):
    return num % 2 == 0 and num > 10


```
### !end-explanation

### !end-challenge
