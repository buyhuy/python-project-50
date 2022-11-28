#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
from gendiff.parser import file1, file2, formatter


def main():
    print(generate_diff(file1, file2, formatter))


if __name__ == '__main__':
    main()
