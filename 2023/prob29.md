### CodeWars XXVI - 29 - File Name Matchup

### Observation

* Looks like we need to only list one directory (no additionals directory traversals needed).

### The Idea

The simple idea is to generate a *normalized* data for each file name under the specified directory. The normalized data should:
* replace any non-alphanumeric characters with spaces, and then
* split the file name into individual words and put those words in a set.

For each file name to search, we will match it one-by-one with the normalized data which we precalculated as we traversed the specified directory earlier.

The neat way to do this is to just calculate the maximum number of matches against all the precalculated normalized data, given the searched file name.  Look at how we call `max()` function below.  We apply `max()` on the array of precalculated data, but we dictate the scoring criteria based on a function (check function `score()` below).

Basically, the function `score()` will score the normalized words in the filename against each precalculated normalized data.  Scoring is done by counting how many words in the normalized search name match the precalculated file name.  We will just return the precalculated file that has the highest score.

Study that trick, it may come handy in the future.

```python
import os
import re

def normalize(name):
    return set(re.sub(r'[^0-9a-zA-Z]+', ' ', name).upper().split())

dir_name = input().strip()
arr = []
for name in os.listdir(f"files/{dir_name}"):
    arr.append((name, normalize(name)))

def score(item):
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
    file_name, _ = max(arr, key=score)
    print(f"{name} -> {file_name}")
```
