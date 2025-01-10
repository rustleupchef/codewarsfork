import os
import re

def normalize(name):
    return set(re.sub(r'[^0-9a-zA-Z]+', ' ', name).upper().split())

dir_name = input().strip()
arr = []
for name in os.listdir(f"files/{dir_name}"):
    arr.append((name, normalize(name)))

def compare(item):
    _, item_words = item
    res = 0
    for x in words:
        if x in item_words:
            res += 1
    return res

while True:
    name = input()
    if name == "END": break
    words = normalize(name)
    file_name, _ = max(arr, key=compare)
    print(f"{name} -> {file_name}")
