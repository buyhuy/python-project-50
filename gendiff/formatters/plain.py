#!/usr/bin/env python3

lst = ['null', 'true', 'false', '[complex value']


def make_view(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, (int, float)):
        return value
    elif value not in lst:
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
                             f"{make_view(val['old_value'])} to "
                             f"{make_view(val['new_value'])}")
            elif val["status"] == "removed":
                val_path = ".".join((path + " " + str(key)).split())
                lines.append(f"Property '{val_path}' was removed")
            elif val["status"] == "added":
                val_path = ".".join((path + " " + str(key)).split())
                lines.append(f"Property '{val_path}' was added "
                             f"with value: {make_view(val['value'])}")
        return "\n".join(lines)

    return walk(data)


def main():
    pass


if __name__ == '__main__':
    main()
