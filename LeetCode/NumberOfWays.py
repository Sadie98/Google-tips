n = 2

height = 2
width = 3
ans = 0

avail = set('red', 'green', 'yellow')

grid = [[0 for x in range(width)] for y in range(height)]
print(grid)
h = 0
w = 0
for color in avail:
    top = grid[h - 1][w] if h > 0 else 0
    left = grid[h][w - 1] if w > 0 else 0
    bottom = grid[h + 1][w] if h < height - 1 else 0
    right = grid[h][w + 1] if w < width - 1 else 0

    if top:
        avail.discard(top)
    if left:
        avail.discard(left)
    if bottom:
        avail.discard(bottom)
    if right:
        avail.discard(right)

    for colour in avail:
        grid[h][w] = colour
        newAvail = avail

        newAvail.discard(colour)
        if w < width - 1:
            w += 1
        elif h < height - 1:
            h += 1
        else:
            ans += 1

        calc(newAvail, h, w)