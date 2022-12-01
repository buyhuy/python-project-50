#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff


expected_stylish = open('tests/fixtures/stylish_expected.txt').read()
expected_plain = open('tests/fixtures/plain_expected.txt').read()
expected_json = open('tests/fixtures/json_expected.txt').read()

json1 = 'tests/fixtures/file1.json'
json2 = 'tests/fixtures/file2.json'

yaml1 = 'tests/fixtures/file1.yaml'
yaml2 = 'tests/fixtures/file2.yaml'


def test_json_generate_diff():
    assert generate_diff(json1, json2, 'stylish') == expected_stylish
    assert generate_diff(json1, json2, 'plain') == expected_plain
    assert generate_diff(json1, json2, 'json') == expected_json


def test_yaml_generate_diff():
    assert generate_diff(yaml1, yaml2, 'stylish') == expected_stylish
    assert generate_diff(yaml1, yaml2, 'plain') == expected_plain
    assert generate_diff(yaml1, yaml2, 'json') == expected_json
