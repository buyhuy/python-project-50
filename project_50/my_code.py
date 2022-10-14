
from project_50.generate_diff import generate_diff
from project_50.formatters.plain import plain
from project_50.formatters.stylish import stylish
import json
json1 = json.load(open('tests/fixtures/file1.json'))
json2 = json.load(open('tests/fixtures/file2.json'))
print(generate_diff(json1, json2))

print('lalala'.startswith('l'))