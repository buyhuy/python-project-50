#!/usr/bin/env python3

import argparse
import json


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

arguments = parser.parse_args()

json1 = json.loads(open(arguments.first_file).read())
json2 = json.loads(open(arguments.second_file).read())


def generate_diff(file1, file2):
    result = []
    all_keys = list(set(list(file1) + list(file2)))
    for key, value in file1.items():
        if key in file2 and file2[key] == value:
            result.append(f'   {key}: {value}\n')
            all_keys.remove(key)
        elif key in file2 and file2[key] != value:
            result.append(f' - {key}: {value}\n '
                          f' + {key}: {file2[key]}\n')
            all_keys.remove(key)
        elif key not in file2:
            result.append(f' - {key}: {value}\n')
            all_keys.remove(key)
    if len(all_keys) != 0:
        for key in all_keys:
            result.append(f' + {key}: {file2[key]}\n')
    result.sort(key=lambda x: x[3])
    print('{\n', *result, '}')


generate_diff(json1, json2)
