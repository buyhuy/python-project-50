#!/usr/bin/env python3

import json
import yaml

from yaml.loader import SafeLoader
from project_50.generate_diff import generate_diff


expected = open('tests/fixtures/expected_value.txt').read()


def test_json_generate_diff():
    json1 = json.load(open('tests/fixtures/file1.json'))
    json2 = json.load(open('tests/fixtures/file2.json'))
    assert generate_diff(json1, json2) == expected


def test_yaml_generate_diff():
    yaml1 = yaml.load(open('tests/fixtures/file1.yaml'), Loader=SafeLoader)
    yaml2 = yaml.load(open('tests/fixtures/file2.yaml'), Loader=SafeLoader)
    assert generate_diff(yaml1, yaml2) == expected
