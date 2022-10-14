#!/usr/bin/env python3

import json
import yaml

from yaml.loader import SafeLoader
from project_50.generate_diff import generate_diff
from project_50.formatters.stylish import stylish
from project_50.formatters.plain import plain


expected_stylish = open('tests/fixtures/stylish_expected.txt').read()
expected_plain = open('tests/fixtures/plain_expected.txt').read()


def test_json_generate_diff():
    json1 = json.load(open('tests/fixtures/file1.json'))
    json2 = json.load(open('tests/fixtures/file2.json'))
    assert generate_diff(json1, json2, plain) == expected_plain
    #assert stylish(generate_diff(json1, json2)) == expected_stylish


def test_yaml_generate_diff():
    yaml1 = yaml.load(open('tests/fixtures/file1.yaml'), Loader=SafeLoader)
    yaml2 = yaml.load(open('tests/fixtures/file2.yaml'), Loader=SafeLoader)
    assert generate_diff(yaml1, yaml2, plain) == expected_plain
    #assert stylish(generate_diff(yaml1, yaml2)) == expected_stylish
