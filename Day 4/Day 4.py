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
    found = False
    a, b = i.split(",")
    s, e = map(int, a.split("-"))
    q, w = map(int, b.split("-"))
    r1 = set(range(s, e + 1))
    r2 = set(range(q, w + 1))

    for j in r1:
        if j in r2:
            x += 1
            found = True
            break
    if not found:
        for k in r2:
            if k in r1:
                x += 1
                break


print(x)
