#!/usr/bin/env python3

import argparse
import json
import yaml

from yaml.loader import SafeLoader
from project_50.formatters.stylish import stylish
from project_50.formatters.plain import plain


parser = argparse.ArgumentParser(description='Compares two configuration '
                                             'files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', default='stylish', choices=['stylish', 'plain'],
                    help='set format of output')

arguments = parser.parse_args()

if arguments.first_file[-4:] == 'yaml' or '.yml':
    file1 = yaml.load(open(arguments.first_file), Loader=SafeLoader)
    file2 = yaml.load(open(arguments.second_file), Loader=SafeLoader)
elif arguments.first_file[-5:] == '.json':
    file1 = json.load(open(arguments.first_file))
    file2 = json.load(open(arguments.second_file))

if arguments.format == 'stylish':
    formatter = stylish
elif arguments.format == 'plain':
    formatter = plain


def main():
    print('dont call me')


if __name__ == '__main__':
    main()
