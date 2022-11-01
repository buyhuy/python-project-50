#!/usr/bin/env python3

import argparse
import json as js
import yaml

from yaml.loader import SafeLoader
from project_50.formatters.stylish import stylish
from project_50.formatters.plain import plain
from project_50.formatters.json import json


parser = argparse.ArgumentParser(description='Compares two configuration '
                                             'files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', choices=['stylish', 'plain', 'json'],
                    default='stylish', help='set format of output')

arguments = parser.parse_args()

if arguments.first_file[-4:] == 'yaml' or '.yml':
    file1 = yaml.load(open(arguments.first_file), Loader=SafeLoader)
    file2 = yaml.load(open(arguments.second_file), Loader=SafeLoader)
elif arguments.first_file[-5:] == '.json':
    file1 = js.load(open(arguments.first_file))
    file2 = js.load(open(arguments.second_file))

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
