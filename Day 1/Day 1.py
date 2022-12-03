with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")
x = []
for i in c:
    x.append(sum(map(int, i.replace("\n", " ").split(" "))))
# Part 1
print(max(x))
# Part 2
y = sorted(x)
print(sum(y[-3:]))
