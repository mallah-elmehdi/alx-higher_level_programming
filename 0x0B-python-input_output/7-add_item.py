#!/usr/bin/python3
"""
Module functions:
    * load_from_json_file(filename)
"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    script that adds all arguments to a Python list,
    and then save them to a file

    Return: void
    """
    filename = "add_item.json"
    arg_list = []

    try:
        arg_list = load_from_json_file(filename)
    except Exception as _:
        save_to_json_file([], filename)

    for i in range(1, len(sys.argv)):
        arg_list.append(sys.argv[i])
    save_to_json_file(arg_list, filename)


if __name__ == "__main__":
    main()
