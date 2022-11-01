#!/usr/bin/env python3

from project_50.formatters.stylish import make_proper_values


def is_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    return value


def add_quotes(value):
    lst = ['null', 'true', 'false', '[complex value]']
    if value not in lst:
        return f"'{value}'"
    return value


def plain(data):

    def walk(value, path='', lines=[]):
        make_proper_values(value)
        for key, val in value.items():
            value_path = path + ' ' + key.strip('+ -')
            value_path = '.'.join(value_path.split())
            if key.startswith('-'):
                if key.replace('-', '+') not in value:
                    lines.append(f"Property '{value_path}' was removed")
                else:
                    updated_key = key.replace('-', '+')
                    lines.append(f"Property '{value_path}' was updated. "
                                 f"From {add_quotes(is_complex(value[key]))} "
                                 f"to {add_quotes(is_complex(value[updated_key]))}")
            elif key.startswith('+') and key.replace('+', '-') not in value:
                lines.append(f"Property '{value_path}' was added "
                             f"with value: {add_quotes(is_complex(val))}")
            elif key.startswith(' '):
                if isinstance(val, dict):
                    walk(val, value_path)
        return '\n'.join(sorted(lines))

    return walk(data)


def main():
    pass


if __name__ == '__main__':
    main()
