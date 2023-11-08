#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""

import sys
import json
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if not path.exists(filename):
    items = []
else:
    items = load_from_json_file(filename)

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)

print(load_from_json_file(filename))
