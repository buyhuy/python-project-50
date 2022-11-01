
from project_50.generate_diff import generate_diff
from project_50.formatters.plain import plain
from project_50.formatters.stylish import stylish
import json
from project_50.generate_diff import make_lines

json1 = json.load(open('tests/fixtures/file1.json'))
json2 = json.load(open('tests/fixtures/file2.json'))

foo = make_lines(json1, json2)

json.dump(foo, open('tests/fixtures/json_expected.txt', 'w'), indent=4, sort_keys=lambda x: x[2:])
