import os
import re

source_path = os.path.join('..','diagnostic')
target_path = os.path.join('..','snake_case_challenges')
titles = re.compile(r'title:\s+([a-zA-Z0-9]*)')
camel_case = re.compile(r"(.+?)([A-Z])")
def snake_case(match):
    return match.group(1).lower() + "_" + match.group(2).lower()

for file in os.listdir(source_path):
  print(file, os.path.isdir(file))
  if os.path.isdir(file):
    continue
  source_filepath = os.path.join(source_path, file)
  target_filepath  = os.path.join(target_path, file)
  with open(source_filepath, "rt") as f:
    markdown = f.read()
    old_function_names = titles.findall(markdown)
    new_function_names = [re.sub(camel_case, snake_case, name, 0) for name in old_function_names]

    try:
      assert(len(old_function_names) == len(new_function_names))
    except:
      print(f'failed for file {file}')



    name_changes = zip(old_function_names,new_function_names)
#    [print(file,i,j) for i,j in name_changes]
    for old, new in name_changes:
      markdown = re.sub(old, new, markdown)

  with open(target_filepath, "wt") as f:
    f.write(markdown)