#!/usr/bin/env python3

from itertools import chain


def dict_indent(value, depth, replacer=" ", spaces_count=4):

    if not isinstance(value, dict):
        return value

    deep_indent_size = depth + spaces_count
    deep_indent = replacer * (deep_indent_size - 2)
    current_indent = replacer * depth
    lines = []
    for key, val in value.items():
        lines.append(f'{deep_indent}  {key}: {dict_indent(val, deep_indent_size)}')
    result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def stylish(data, replacer=" ", spaces_count=4):

    def walk(value, depth):

        if not isinstance(value, dict):
            return value

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * (deep_indent_size - 2)  # "- 2" need for pretty indent
        current_indent = replacer * depth
        lines = []
        for key, val in value.items():
            if val["status"] == "same":
                lines.append(f'{deep_indent}  {key}: {walk(val["value"], deep_indent_size)}')
            elif val["status"] == "changed":
                lines.append(f'{deep_indent}- {key}: {dict_indent(val["old_value"], deep_indent_size)}')
                lines.append(f'{deep_indent}+ {key}: {dict_indent(val["new_value"], deep_indent_size)}')
            elif val["status"] == "removed":
                lines.append(f'{deep_indent}- {key}: {dict_indent(val["value"], deep_indent_size)}')
            elif val["status"] == "added":
                lines.append(f'{deep_indent}+ {key}: {dict_indent(val["value"], deep_indent_size)}')
        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(data, 0)


def main():
    pass


if __name__ == '__main__':
    main()
