#!/usr/bin/env python3

import argparse

from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


parser = argparse.ArgumentParser(description='Compares two configuration '
                                             'files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', choices=['stylish', 'plain', 'json'],
                    default='stylish', help='set format of output')

arguments = parser.parse_args()

first_path = arguments.first_file
second_path = arguments.second_file

if arguments.format == 'stylish':
    formatter = stylish
elif arguments.format == 'plain':
    formatter = plain
elif arguments.format == 'json':
    formatter = json


def main():
    pass


if __name__ == '__main__':
    main()
