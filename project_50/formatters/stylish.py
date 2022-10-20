#!/usr/bin/env python3

import itertools


def make_proper_values(dict):
    for key in dict:
        if dict[key] == True:
            dict[key] = 'true'
        elif dict[key] == False:
            dict[key] = 'false'
        elif dict[key] == None:
            dict[key] = 'null'
    return dict


def stylish(data, replacer=' ', spaces_count=4):

    def walk(value, depth):
        if type(value) != dict:
            return value
        make_proper_values(value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - 2)
        current_indent = replacer * depth
        lines = []
        for key, val in value.items():
            lines.append(f'{deep_indent}{key}: {walk(val, deep_indent_size)}')
        lines.sort(key=lambda x: x.strip('+- '))
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)

    return walk(data, 0)


def main():
    pass


if __name__ == '__main__':
    main()
