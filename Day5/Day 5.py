with open('data.txt', 'r') as r:
    c = r.read().rstrip().split("\n\n")

stacks = [[] for _ in range(9)]
initial = c[0].split("\n")

for i in initial[:-1]:
    arrangement = i[1::4]
    for j in range(len(arrangement)):
        if arrangement[j] == ' ':
            continue
        stacks[j].append(arrangement[j])

stacks = [stack[::-1] for stack in stacks]
instructions = c[1].split('\n')

stacks_copy = [stack.copy() for stack in stacks]

# Part 1
for i in instructions:
    count = int(i.split()[1])
    box1 = int(i.split()[3]) - 1
    box2 = int(i.split()[5]) - 1

    for _ in range(count):
        stacks[box2].append(stacks[box1].pop())

print("".join(i[-1] for i in stacks))

# Part 2
for i in instructions:
    count = int(i.split()[1])
    box1 = int(i.split()[3]) - 1
    box2 = int(i.split()[5]) - 1

    stacks_copy[box2].extend(stacks_copy[box1][-count:])
    stacks_copy[box1] = stacks_copy[box1][:-count]

print("".join(i[-1] for i in stacks_copy))
