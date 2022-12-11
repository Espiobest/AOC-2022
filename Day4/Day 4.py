with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")

c = c[0].split("\n")

# Part 1
x = 0
for i in c:
    a, b = i.split(",")
    s, e = map(int, a.split("-"))
    q, w = map(int, b.split("-"))
    r1 = set(range(s, e + 1))
    r2 = set(range(q, w + 1))
    x += q >= s and w <= e or s >= q and e <= w

print(x)

# Part 2

x = 0

for i in c:
    a, b = i.split(",")
    s, e = map(int, a.split("-"))
    q, w = map(int, b.split("-"))
    r1 = set(range(s, e + 1))
    r2 = set(range(q, w + 1))
    if r1.intersection(r2):
        x += 1

print(x)
