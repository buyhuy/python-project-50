#!/usr/bin/env python3

import argparse
import json

from project_50.generate_diff import generate_diff


parser = argparse.ArgumentParser(description='Compares two configuration '
                                             'files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

arguments = parser.parse_args()

json1 = json.load(open(arguments.first_file))
json2 = json.load(open(arguments.second_file))


def main():
    generate_diff(json1, json2)


if __name__ == '__main__':
    main()