with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n")


def checkCycles(signals):
    if cycles in [20, 60, 100, 140, 180, 220]:
        signals += cycles * register
    return signals


def draw():
    if abs(register - (cycles - 1) % 40) <= 1:
        screen[(cycles - 1) // 40][(cycles - 1) % 40] = "#"


register = 1
signals = 0
cycles = 0
screen = [[" " for _ in range(40)] for _ in range(6)]
for i in c:
    instr = i.split()
    if len(instr) == 1:
        cycles += 1
        signals = checkCycles(signals)
        draw()
    else:
        for _ in range(2):
            cycles += 1
            signals = checkCycles(signals)
            draw()
        num = int(instr[1])
        register += num
# Part 1
print(signals)
# Part 2
for i in screen:
    print("".join(i))
