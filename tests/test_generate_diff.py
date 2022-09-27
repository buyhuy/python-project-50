#!/usr/bin/env python3

import json
import yaml

from yaml.loader import SafeLoader
from project_50.generate_diff import generate_diff


expected = '{\n' + ''.join([' - follow: False\n',
           '   host: hexlet.io\n', ' - proxy: 123.234.53.22\n',
           ' - timeout: 50\n + timeout: 20\n', ' + verbose: True\n']) + '}'


def test_generate_diff_json():
    json1 = json.load(open('tests/fixtures/file1.json'))
    json2 = json.load(open('tests/fixtures/file2.json'))
    assert generate_diff(json1, json2) == expected


def test_yaml_generate_diff():
    yaml1 = yaml.load('tests/fixtures/file2.yaml', Loader=SafeLoader)
    yaml2 = yaml.load('tests/fixtures/file2.yaml', Loader=SafeLoader)
    assert generate_diff(yaml1, yaml2) == expected
