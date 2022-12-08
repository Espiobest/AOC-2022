with open('data.txt', 'r') as right:
    trees = right.read().strip().split("\n")

# Part 1
visible = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        leftVisible = False
        rightVisible = False
        upVisible = False
        downVisible = False
        cur = int(trees[i][j])
        if all(int(trees[i][k]) < cur for k in range(j)):
            leftVisible = True
        if all(int(trees[i][k]) < cur for k in range(j+1, len(trees[0]))):
            rightVisible = True
        if all(int(trees[k][j]) < cur for k in range(i)):
            upVisible = True
        if all(int(trees[k][j]) < cur for k in range(i+1, len(trees))):
            downVisible = True

        if leftVisible or rightVisible or upVisible or downVisible:
            visible += 1

print(visible + (2 * len(trees[0])) + (2 * (len(trees)-2)))

# Part 2
scenicScore = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        cur = int(trees[i][j])
        leftScore = 1
        rightScore = 1
        upScore = 1
        bottomScore = 1

        # check left
        for left in range(j-1, 0, -1):
            if int(trees[i][left]) >= cur:
                break
            leftScore += 1

        # check right
        for right in range(j+1, len(trees[0])-1):
            if int(trees[i][right]) >= cur:
                break
            rightScore += 1

        # check top
        for up in range(i-1, 0, -1):
            if int(trees[up][j]) >= cur:
                break
            upScore += 1

        # check bottom
        for bottom in range(i+1, len(trees)-1):
            if int(trees[bottom][j]) >= cur:
                break
            bottomScore += 1

        scenicScore = max(scenicScore, leftScore * rightScore * upScore * bottomScore)

print(scenicScore)
# ANSWER 1 = 1785
# ANSWER 2 = 345168
