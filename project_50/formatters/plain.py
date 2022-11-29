#!/usr/bin/env python3


def is_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    return value


def quotes(value):
    lst = ['null', 'true', 'false', '[complex value]']
    if value not in lst:
        return f"'{value}'"
    return value


def plain(data):

    def walk(value, path="", lines=[]):

        if not isinstance(value, dict):
            return

        for key, val in value.items():
            if val["status"] == "same":
                val_path = ".".join((path + " " + str(key)).split())
                walk(val["value"], val_path)
            elif val["status"] == "changed":
                val_path = ".".join((path + " " + str(key)).split())
                lines.append(f"Property '{val_path}' was updated. From "
                             f"{quotes(is_complex(val['old_value']))} to "
                             f"{quotes(is_complex(val['new_value']))}")
            elif val["status"] == "removed":
                val_path = ".".join((path + " " + str(key)).split())
                lines.append(f"Property '{val_path}' was removed")
            elif val["status"] == "added":
                val_path = ".".join((path + " " + str(key)).split())
                lines.append(f"Property '{val_path}' was added "
                             f"with value: {quotes(is_complex(val['value']))}")
        return "\n".join(lines)

    return walk(data)


def main():
    pass


if __name__ == '__main__':
    main()
