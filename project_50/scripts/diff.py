#!/usr/bin/env python3

from project_50.gendiff import generate_diff
from project_50.parser import file1, file2, formatter


def main():
    print(generate_diff(file1, file2, formatter))


if __name__ == '__main__':
    main()
