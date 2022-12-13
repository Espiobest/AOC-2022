import functools
import json

with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")

pairs = [i.split("\n") for i in c]


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b

    elif isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            cmp = compare(a[i], b[i])
            if cmp is not None:
                return cmp

        if len(a) == len(b):
            return None
        return len(a) < len(b)

    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])

    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)


# Part 1
S = 0
ls = [[[2]], [[6]]]
for i, e in enumerate(pairs, 1):
    first, second = e
    first = json.loads(first)
    second = json.loads(second)
    ls.append(first)
    ls.append(second)
    if compare(first, second) is True:
        S += i

print("Part 1:", S)

# Part 2
ls.sort(key=functools.cmp_to_key(lambda a, b: -compare(a, b)))
ans = (ls.index([[2]]) + 1) * (ls.index([[6]]) + 1)
print("Part 2:", ans)
