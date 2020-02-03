import os
import re

source_path = os.path.join('..','testdir')
target_path = os.path.join('..','snake_case_challenges')

for file in os.listdir(source_path):
  filepath = os.path.join(source_path, file)
  with open(filepath, "rt") as f:
    data = f.read()
    titles = re.compile(r'title:\s+([a-zA-Z]*)')
    function_names = titles.findall(data)
    print(file,function_names)