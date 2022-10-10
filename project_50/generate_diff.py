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


def make_indent(value):
    if not isinstance(value, dict):
        return value
    new = {}
    for key, val in value.items():
        new[f'  {key}'] = make_indent(val)
    return new


def generate_diff(file1, file2):
    lines = {}
    make_proper_values(file1)
    make_proper_values(file2)
    minus = set(file1) - set(file2)
    plus = set(file2) - set(file1)
    neutral = set(file1) & set(file2)
    for key in minus:
        lines[f'- {key}'] = make_indent(file1[key])
    for key in plus:
        lines[f'+ {key}'] = make_indent(file2[key])
    for key in neutral:
        if type(file1[key]) and type(file2[key]) == dict:
            lines[f'  {key}'] = generate_diff(file1[key], file2[key])
        else:
            if file1[key] == file2[key]:
                lines[f'  {key}'] = make_indent(file1[key])
            elif file1[key] != file2[key]:
                lines[f'- {key}'] = make_indent(file1[key])
                lines[f'+ {key}'] = make_indent(file2[key])
    return lines


def stylish(data, replacer=' ', spaces_count=4):

    def walk(value, depth):
        if type(value) != dict:
            return value
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
    print('dont call me')


if __name__ == '__main__':
    main()
