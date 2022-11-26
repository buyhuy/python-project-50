#!/usr/bin/env python3

import json as js
import yaml

from yaml.loader import SafeLoader
from project_50.formatters.stylish import stylish
from project_50.formatters.plain import plain
from project_50.formatters.json import json
from project_50.generate_diff import generate_diff, fix_values


expected_stylish = open('tests/fixtures/stylish_expected.txt').read()
expected_plain = open('tests/fixtures/plain_expected.txt').read()
expected_json = open('tests/fixtures/json_expected.txt').read()

json1 = fix_values(js.load(open('tests/fixtures/file1.json')))
json2 = fix_values(js.load(open('tests/fixtures/file2.json')))

yaml1 = fix_values(yaml.load(open('tests/fixtures/file1.yaml'), Loader=SafeLoader))
yaml2 = fix_values(yaml.load(open('tests/fixtures/file2.yaml'), Loader=SafeLoader))


def test_json_generate_diff():
    assert generate_diff(json1, json2, stylish) == expected_stylish
    assert generate_diff(json1, json2, plain) == expected_plain
    assert generate_diff(json1, json2, json) == expected_json


def test_yaml_generate_diff():
    assert generate_diff(yaml1, yaml2, stylish) == expected_stylish
    assert generate_diff(yaml1, yaml2, plain) == expected_plain
    assert generate_diff(yaml1, yaml2, json) == expected_json
