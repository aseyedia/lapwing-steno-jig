import json
from collections import defaultdict

with open("steno-dictionaries/lapwing-base.json") as f1:
    with open("steno-dictionaries/lapwing-proper-nouns.json") as f2:
        lapwing = {**json.load(f1), **json.load(f2)}

inverse = defaultdict(list)
for k, v in lapwing.items():
    inverse[v].append(k)

def key(k):
    return (-k.count('/'), -len(k))

# Modify the inverse dictionary to remove the first element from each list of values if the list has more than one element
for v, ks in inverse.items():
    if len(ks) > 1:
        sorted_ks = sorted(ks, key=key)
        inverse[v] = sorted_ks[1:]

with open("lapwing-translations.js", "w") as f:
    f.write(f'TypeJig.Translations.Lapwing = {json.dumps(inverse)};')
