with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")

# Part 1
sequence = c[0]
for i in range(0, len(sequence)):
    if len(set(sequence[i:i+4])) == 4:
        print(i + 4)
        break

# Part 2
for i in range(0, len(sequence)):
    if len(set(sequence[i:i+14])) == 14:
        print(i + 14)
        break
