#!/usr/bin/python3
"""Input and output python module."""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_from_json_file').save_from_json_file

try:
    item_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    item_list = []
input_arguments = sys.argv[1:]
item_list.extend(input_arguments)
save_to_json_file(item_list, 'add_item.json')
