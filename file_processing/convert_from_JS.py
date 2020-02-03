import os
import re
import unicodedata

source_file_name = "152-greetCustomer.md"
source_path = os.path.join("diagnostic-JS", source_file_name)
target_path = os.path.join("diagnostic", source_file_name)

test_class_string = '''
```python
import main
import unittest

class TestScript(unittest.TestCase):
```
'''

assert_is = '''
    def test_{n}(self):
        # it {msg}
        self.assertIs(type(main.{function}), {result},
        msg = '{msg}' )

'''

assert_equal = '''
    def test_{n}(self):
        # it {msg}
        self.assertEqual(main.{function}, {result},
        msg = '{msg}')

'''

assert_true = '''
    def test_{n}(self):
        # it {msg}
        self.assertTrue(main.{function},
        msg = '{msg}')

'''

assert_false = '''
    def test_{n}(self):
        # it {msg}
        self.assertFalse(main.{function},
        msg = '{msg}')

'''

with open(source_path, "rt") as f:
    data = f.read()
data = unicodedata.normalize("NFKD", data)


describe = re.compile(r'describe[^`]*')
describe_blocks = describe.findall(data)
function_name = re.compile(r'describe\(\"([A-z]*)')
test_description = re.compile(r'it\("([^"]*)')
expected_result = re.compile(r'eq\(([^\)]*)\)')

test_object = {}  #container for parsed describe block

for block in describe_blocks:
    if function_name.findall(block):
        name = function_name.findall(block)[0]
        function_with_args = re.compile(r'{}\([^)]+\)'.format(name))
        test_object[name] = list(zip(function_with_args.findall(block),
                                     expected_result.findall(block),
                                     test_description.findall(block)))

output_strings = []  # creates final test strings for insertion at each function after test_class_string

for key in test_object:
    acc = ""
    for n, test in enumerate(test_object[key]):
        result = assert_equal.format(n=n,
                                  function=test[0],
                                  result=test[1],
                                  msg=test[2])
        acc += result
    output_strings.append(acc)

#print(output_strings)

data = re.sub(r'var\s+', '', data)
data = re.sub(r'local-snippet', 'code-snippet', data)
data = re.sub(r'javascript', r'python3.6', data)
data = re.sub(r';', '', data)  # everyone hates semicolons, amirite?
data = re.sub(r'{\s*', ':', data)
data = re.sub(r'}', '', data)
data = re.sub(r'\s{0,2}//\s+your code here', '\n    # your code here\n    pass',
              data)
data = re.sub(r'//', r'#', data)  # pythonic comments
data = re.sub(r'console.log', r'print', data)  # python print statement
data = re.sub(r'function\s(?!called)', r'def ', data)  # function -> def
data = re.sub(r'`js', r'`python', data)
data = re.sub(r'!tests', "!tests\n"+test_class_string+"\n".join(output_strings),
              data)
data = re.sub(r'\)\s+:', r'):', data)
data = re.sub(r'true', 'True', data)
data = re.sub(r'false', 'False', data)
data = re.sub(r'array', r'list', data)
data = re.sub(r'properties', r'keys', data)
data = re.sub(r'objects', r'dictionaries', data)
data = re.sub(r'\bobject\b', r'dictionary', data)
data = re.sub(r'an dictionary', r'a dictionary', data)
data = re.sub(r'an list', r'a list', data)
data = re.sub(r'undefined', r'None', data)

with open(target_path, "wt") as f:
    f.write(data)
