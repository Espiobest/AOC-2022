with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")


def turn(part=1):
    monkeys = [[j.strip() for j in i.split("\n")] for i in c]
    monkeyItems = {index: [int(item.strip(",")) for item in monkey[1].split()[2:]] for index, monkey in
                   enumerate(monkeys)}
    numInspection = {i: 0 for i in monkeyItems}

    end = 20 if part == 1 else 10000
    mod = 1
    if part == 2:
        for monkey in monkeys:
            testNum = int(monkey[3].split("divisible by ")[-1])
            mod *= testNum

    for _ in range(end):
        for index, monkey in enumerate(monkeys):
            items = monkeyItems.get(index)
            operation = monkey[2].split("= ")[1]
            _, op, num = operation.split()
            testNum = int(monkey[3].split("divisible by ")[-1])
            ifTrue = int(monkey[4].split("throw to monkey ")[-1])
            ifFalse = int(monkey[5].split("throw to monkey ")[-1])

            for worry in items:
                change = worry if num == "old" else int(num)
                if op == "+":
                    worryLevel = worry + change
                else:
                    worryLevel = worry * change
                if part == 1:
                    worryLevel //= 3
                else:
                    worryLevel %= mod
                if worryLevel % testNum == 0:
                    monkeyItems[ifTrue].append(worryLevel)
                else:
                    monkeyItems[ifFalse].append(worryLevel)
                numInspection[index] += 1
            monkeyItems[index] = []
    return numInspection


# Part 1
numInspections = turn(1)
last, secondLast, *_ = sorted(numInspections.values(), reverse=True)
print("Part 1:", last * secondLast)

# Part 2
numInspections = turn(2)
last, secondLast, *_ = sorted(numInspections.values(), reverse=True)
print("Part 2:", last * secondLast)
