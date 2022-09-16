#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=int)
parser.add_argument('second_file', type=int)
parser.add_argument('-f', '--format', help='set format of output')
arguments = parser.parse_args()
# print(parser)

print(arguments.first_file + arguments.second_file)
