#!/usr/bin/env python3

from gendiff.generate_diff import generate_diff
from gendiff.parser import first_path, second_path, formatter


def main():
    print(generate_diff(first_path, second_path, formatter))


if __name__ == '__main__':
    main()
