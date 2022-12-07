with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")

lines = c[0].split("\n")
sizes = dict()
cur = []

for line in lines:
    cmds = line.split()

    if cmds[1] == "cd":
        if cmds[2] == "..":
            cur.pop()
        else:
            cur.append(cmds[2])

    if cmds[0].isdigit():
        size = int(cmds[0])
        for i in range(len(cur)):
            path = "/".join(cur[:i+1])
            if path not in sizes:
                sizes[path] = 0
            sizes["/".join(cur[:i+1])] += size

print(sum(i for i in sizes.values() if i < 100000))

# Part 2

to_free = 7e7 - sizes["/"]

for size in sorted(sizes.values()):
    if to_free + size >= 3e7:
        print(size)
        break
