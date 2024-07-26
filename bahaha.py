'''
10
8
3
2
'''

width,height,cutwidth,cutheight = 10,8,3,2#[int(input()) for _ in range(4)]
spiralmap = [['o' for _ in range(width)] if cutheight<y<=(height-cutheight) else ['o' if cutwidth<x<=(width-cutwidth) else '#' for x in range(1,width+1)] for y in range(1,height+1)]

currentx = cutwidth
currenty = 0

gravity = True

#go right until it reaches a wall
#if its a wall or out of bounds try to go down
#if it cant go down go left
#if wall on left gravity turns false and do opposite

def inBounds(coorx,coory):
    if 0<=coorx<width and 0<=coory<height:
        return True
    return False


def nextTile():
    global currenty,currentx
    spiralmap[currenty][currentx]='#'
    if gravity: # Gravity is to the right
        if inBounds(currentx+1,currenty):
            if spiralmap[currenty][currenty+1]=='o':
                currentx+=1
        elif not inBounds(currentx+1,currenty) or spiralmap[currenty][currentx+1]=='#':
            if spiralmap[currenty+1][currentx]=='o':
                currenty+=1


while True:
    input()
    nextTile()
    for row in spiralmap:
        print(row)