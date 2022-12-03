with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")

x = c[0].split("\n")

# Part 1
total = 0
for i in x:
    a, b = i.split()
    if b == "X":
        total += 1
    if b == "Y":
        total += 2
    if b == "Z":
        total += 3
    if a == "A" and b == "X" or a == "B" and b == "Y" or a == "C" and b == "Z":
        total += 3
    if a == "A" and b == "Y" or a == "B" and b == "Z" or a == "C" and b == "X":
        total += 6
print(total)

# A: R 1 B: P 2 C:S 3
# X: Lose Y: Draw Z: Win

# Part 2
total2 = 0

for i in x:
    a, b = i.split()
    if b == "X":
        if a == "A":
            total2 += 3
        elif a == "B":
            total2 += 1
        else:
            total2 += 2
    if b == "Y":
        if a == "A":
            total2 += 1
        elif a == "B":
            total2 += 2
        else:
            total2 += 3
        total2 += 3
    if b == "Z":
        if a == "A":
            total2 += 2
        elif a == "B":
            total2 += 3
        else:
            total2 += 1
        total2 += 6

print(total2)
