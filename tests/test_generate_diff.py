#!/usr/bin/env python3

import json

from project_50.generate_diff import generate_diff

expected = 'jopa'

path1 = 'tests/fixtures/file1.json'
path2 = 'tests/fixtures/file2.json'
f1 = json.load(open(path1))
f2 = json.load(open(path2))


def test_generate_diff():
    assert generate_diff(f1, f2) == '{\n' + ''.join([' - follow: False\n',
                                    '   host: hexlet.io\n', ' - proxy: 123.234.53.22\n',
                                    ' - timeout: 50\n + timeout: 20\n', ' + verbose: True\n']) + '}'
