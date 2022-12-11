from collections import deque
from dataclasses import dataclass
from functools import reduce
from operator import add, mul
from typing import List, Deque, Callable
import pathlib


def read_data():
    with open("data.txt") as raw_data:
        return [line.strip() for line in raw_data.readlines()]


@dataclass
class Item:
    worry: int


@dataclass
class Var:
    pass


@dataclass
class Const:
    value: int


Arg = Const | Var


@dataclass
class Operation:
    left: Arg
    right: Arg
    op: Callable[[int, int], int]

    def __call__(self, item: Item) -> int:
        return self.op(self.left.value if isinstance(self.left, Const) else item.worry,
                       self.right.value if isinstance(self.right, Const) else item.worry)


@dataclass
class Test:
    divisor: int
    true_target: int
    false_target: int

    def __call__(self, item: Item) -> int:
        return self.true_target if item.worry % self.divisor == 0 else self.false_target


@dataclass
class Monkey:
    items: Deque[Item]
    operation: Operation
    test: Test
    worry_drop: bool
    reductor: int = 0
    num_inspections: int = 0

    def add_item(self, item: Item):
        self.items.append(item)

    def inspect_all(self, monkeys: List['Monkey']):
        while True:
            try:
                item = self.items.popleft()
                self.num_inspections += 1
            except:
                return

            item.worry = self.operation(item)
            if self.worry_drop:
                item.worry //= 3
            if self.reductor:
                item.worry %= self.reductor
            monkeys[self.test(item)].add_item(item)


def execute_rounds(monkeys: List[Monkey], rounds: int):
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect_all(monkeys)


def parse_monkeys(data: List[str], worry_drop: bool) -> List[Monkey]:
    monkeys: List[Monkey] = []
    data = iter(data)
    while True:
        # Monkey <int>:
        next(data)

        # Starting items: <int>, ...
        line = next(data)
        items = deque([Item(int(num)) for num in line[len("Starting items: "):].split(", ")])

        # Operation: new = <'old'|int> <'+'|'*'> <'old'|int>
        line = next(data)
        left, op, right = line[len("Operation: new = "):].split()
        operation = Operation(Var() if left == "old" else Const(int(left)),
                              Var() if right == "old" else Const(int(right)),
                              add if op == "+" else mul)

        # Test: divisible by <int>
        # If true: throw to monkey <int>
        # If false: throw to monkey <int>
        line = next(data)
        line_true = next(data)
        line_false = next(data)
        test = Test(int(line.split()[-1]),
                    int(line_true.split()[-1]),
                    int(line_false.split()[-1]), )

        monkeys.append(Monkey(items, operation, test, worry_drop))

        try:
            # empty line
            next(data)
        except:
            break

    if not worry_drop:
        lcm = reduce(mul, [m.test.divisor for m in monkeys])
        for m in monkeys:
            m.reductor = lcm

    return monkeys


def part1(data: List[str]) -> int:
    monkeys = parse_monkeys(data, True)
    execute_rounds(monkeys, 20)
    monkeys = sorted(monkeys, key=lambda m: m.num_inspections)
    print([i.num_inspections for i in monkeys])
    print({0: 529, 1: 482, 2: 479, 3: 64, 4: 29, 5: 545, 6: 75, 7: 70})
    return monkeys[-1].num_inspections * monkeys[-2].num_inspections


def part2(data: List[str]) -> int:
    monkeys = parse_monkeys(data, False)
    execute_rounds(monkeys, 10000)
    monkeys = sorted(monkeys, key=lambda m: m.num_inspections)
    return monkeys[-1].num_inspections * monkeys[-2].num_inspections


def main():
    data = read_data()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()