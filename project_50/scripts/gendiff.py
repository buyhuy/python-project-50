#!/usr/bin/env python3

from project_50.generate_diff import generate_diff
from project_50.parser import file1, file2


def main():
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
