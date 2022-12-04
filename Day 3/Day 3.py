import string
with open('data.txt', 'r') as r:
    c = r.read().split("\n\n")

x = c[0].split("\n")

# Part 1
s = 0
for i in x:
    a, b = i[:len(i)//2], i[len(i)//2:]
    for j in set(a):
        if j in b:
            s += string.ascii_letters.index(j) + 1
print(s)

# Part 2
s2 = 0
for i in range(0, len(x), 3):
    a, b, c = x[i:i + 3]
    for j in set(a):
        if j in b and j in c:
            s2 += string.ascii_letters.index(j) + 1

print(s2)
