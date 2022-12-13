from collections import deque
with open('data.txt', 'r') as r:
    c = r.read().strip().split("\n\n")

board = [list(i) for i in c[0].split("\n")]


def get_neighbors(pos):
    x, y = pos
    for nx, ny in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
        if nx < 0 or ny < 0 or nx >= len(board[0]) or ny >= len(board):
            continue
        cur = ord(board[y][x])
        nxt = ord(board[ny][nx])
        if nxt - cur <= 1:
            yield nx, ny


def solve(start, end):
    q = deque([[start, 0]])
    dist = {start: 0}
    while q:
        pos, steps = q.popleft()
        for n in get_neighbors(pos):
            if n not in dist:
                dist[n] = steps + 1
                q.append((n, steps+1))
    if end in dist:
        return dist[end]


start = (0, 0)
end = (-1, -1)
possible_starts = [start]
for i in range(len(board[0])):
    for j in range(len(board)):
        if board[j][i] == "S":
            start = (i, j)
            board[j][i] = "a"
        elif board[j][i] == "E":
            end = (i, j)
            board[j][i] = "z"
        if board[j][i] == "a":
            possible_starts.append((i, j))

print("Part 1:", solve(start, end))

dists = [solve(s, end) for s in possible_starts]
dists = [*filter(None, dists)]
print("Part 2:", min(dists))
