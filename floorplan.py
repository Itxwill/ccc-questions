'''
105
14
16
IIIIIIIIIIIIIIII
I......I.......I
I......III.....I
I........I.....I
I........IIIIIII
IIIIIIIIII.....I
I.I......I.....I
III..III.I.....I
I....I.IIIII...I
I....I.....III.I
I....I.......I.I
I....I.....III.I
I....I.....I...I
IIIIIIIIIIIIIIII

13
2
3
.I.
.I.
'''
#grid[y][x]
# y is from 0 to rows-1 inclusive
# x is from 0 to collums-1 inclusive


floors = int(input())
rows = int(input())
collums = int(input())

grid = [list(map(lambda x:0 if x=='.' else 1, [*input()])) for _ in range(rows)]

# for row in grid:
#     print (''.join(list(map(lambda x:'I' if x==1 else '.', [*row]))))

def inBounds(node):
    #check x then y
    if node == None:
        return False
    if 0<=node[0]<=collums-1 and 0<=node[1]<=rows-1:
        return True
    return False

def flood(x,y):
    visited = []
    queue = [(x,y)]
    tiles = 1
    while queue:
        #input()#used to pause before iteration
        firstqueue=queue[0]
        x = firstqueue[0]
        y = firstqueue[1]
        left  = (x-1,y) if (x-1,y) not in visited and (x-1,y) not in queue else None
        right = (x+1,y) if (x+1,y) not in visited and (x+1,y) not in queue else None
        upper = (x,y+1) if (x,y+1) not in visited and (x,y+1) not in queue else None
        lower = (x,y-1) if (x,y-1) not in visited and (x,y-1) not in queue else None

        if inBounds(left)  and grid[left[1]][left[0]] == 0:
            tiles+=1
            queue.append(left)
        if inBounds(right) and grid[right[1]][right[0]]==0:
            tiles+=1
            queue.append(right)
        if inBounds(upper) and grid[upper[1]][upper[0]]==0:
            tiles+=1
            queue.append(upper)
        if inBounds(lower) and grid[lower[1]][lower[0]]==0:
            tiles+=1
            queue.append(lower)


        #after we use the node we troll them
        visited.append(firstqueue)
        grid[firstqueue[1]][firstqueue[0]]=1
        queue.pop(0)

        # for x in range(5):
        #     print('\n')
        # for row in grid:
        #     print (''.join(list(map(lambda x:'I' if x==1 else '.', [*row]))))
        # print(tiles)

    return tiles

rooms = []
for x in range(collums):
    for y in range(rows):
        if grid[y][x]==0:
            rooms.append(flood(x,y))


doogit = True
for room,tiles in enumerate(sorted(rooms,reverse=True)):
    if floors-tiles>=0:
        floors-=tiles
    else:
        if room>1 or room<=0:
            print(f'{room} rooms, {floors} square metre(s) left over')
        else:
            print(f'{room} room, {floors} square metre(s) left over')
        doogit = False
        break
if doogit:
    if room>1 or room<=0:
        print(f'{len(rooms)} rooms, {floors} square metre(s) left over')
    else:
        print(f'{len(rooms)} room, {floors} square metre(s) left over')