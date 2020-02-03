import os
import re

source_path = os.path.join('..','testdir')
target_path = os.path.join('..','snake_case_challenges')
titles = re.compile(r'title:\s+([a-zA-Z0-9]*)')
camel_case = re.compile(r"(.+?)([A-Z])")
def snake_case(match):
    return match.group(1).lower() + "_" + match.group(2).lower()

for file in os.listdir(source_path):
  filepath = os.path.join(source_path, file)
  with open(filepath, "rt") as f:
    markdown = f.read()
    old_function_names = titles.findall(markdown)
    new_function_names = [re.sub(camel_case, snake_case, name, 0) for name in old_function_names]
    print(file, new_function_names)

# split function names according to upper case letters in function name ONLY!
# if not in camel case, ignore function name
# lowercase all words
# replace original function name with lowercase snake function names