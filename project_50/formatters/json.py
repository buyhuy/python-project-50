#!/usr/bin/env python3

import json as js


def json(data):
    result = js.dumps(data, indent=5, sort_keys=lambda x: x.strip(' +-'))
    return result


def main():
    pass


if __name__ == '__main__':
    main()
