#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(description='Compares two configuration '
                                             'files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', choices=['stylish', 'plain', 'json'],
                    default='stylish', help='set format of output')

arguments = parser.parse_args()

first_path = arguments.first_file
second_path = arguments.second_file

formatter = arguments.format


def main():
    pass


if __name__ == '__main__':
    main()
