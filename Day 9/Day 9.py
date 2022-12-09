with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n")

# Part 1
h_pos = [0, 0]
t_pos = [0, 0]
visited = {(0, 0)}

for i in c:
    direction, step = i.split()
    step = int(step)
    for _ in range(step):
        if direction == "U":
            h_pos[1] += 1
        elif direction == "D":
            h_pos[1] -= 1
        elif direction == "L":
            h_pos[0] -= 1
        elif direction == "R":
            h_pos[0] += 1

        if abs(t_pos[0] - h_pos[0]) > 1 or abs(t_pos[1] - h_pos[1]) > 1:
            if h_pos[0] > t_pos[0]:
                t_pos[0] += 1
            elif h_pos[0] < t_pos[0]:
                t_pos[0] -= 1
            if h_pos[1] > t_pos[1]:
                t_pos[1] += 1
            elif h_pos[1] < t_pos[1]:
                t_pos[1] -= 1
            visited.add((*t_pos,))

print("Part 1:", len(visited))

# Part 2
visited = {(0, 0)}
ropes = [[0, 0] for _ in range(10)]

for a in c:
    direction, step = a.split()
    step = int(step)
    for _ in range(step):
        if direction == "U":
            ropes[0][1] += 1
        elif direction == "D":
            ropes[0][1] -= 1
        elif direction == "L":
            ropes[0][0] -= 1
        elif direction == "R":
            ropes[0][0] += 1

        for i in range(1, len(ropes)):
            cur_pos = ropes[i]
            prev_pos = ropes[i - 1]
            if abs(cur_pos[0] - prev_pos[0]) > 1 or abs(cur_pos[1] - prev_pos[1]) > 1:
                if prev_pos[0] > cur_pos[0]:
                    ropes[i][0] += 1
                elif prev_pos[0] < cur_pos[0]:
                    ropes[i][0] -= 1
                if prev_pos[1] > cur_pos[1]:
                    ropes[i][1] += 1
                elif prev_pos[1] < cur_pos[1]:
                    ropes[i][1] -= 1
        visited.add((*ropes[-1],))

print("Part 2:", len(visited))
