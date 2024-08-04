'''
10
8
3
2
99
'''

width,height,cutwidth,cutheight,steps = [int(input()) for _ in range(5)]
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

def canGo(coorx,coory):
    if not inBounds(coorx,coory):
        return False
    if spiralmap[coory][coorx]=='#':
        return False
    return True 


def nextTile():
    
    global currenty,currentx,gravity
    spiralmap[currenty][currentx]='#'

    # so you can do if right:
    right = (currentx+1,currenty)
    left = (currentx-1,currenty)
    up = (currentx,currenty-1)
    down = (currentx,currenty+1)
    if (not canGo(up[0],up[1])) and (not canGo(right[0],right[1])) and (not canGo(down[0],down[1])) and (not canGo(left[0],left[1])):
        return True
    #print(currentx,currenty)

    # print(gravity)
    if gravity: # Gravity is to the right
        if inBounds(right[0],right[1]) and spiralmap[right[1]][right[0]]=='o':
            currentx+=1
            return False
        if not inBounds(right[0],right[1]) or spiralmap[right[1]][right[0]]=='#':
            if inBounds(down[0],down[1]) and spiralmap[down[1]][down[0]]=='o':
                # we have encounterd the wall or the outer bound go down
                currenty+=1
                return False

        #if the right side is blocked and the down is blocked go left
        #blocked as in out of bounds or a # tile

        if (not inBounds(right[0],right[1]) or spiralmap[right[1]][right[0]]=='#') and (not inBounds(down[0],down[1]) or spiralmap[down[1]][down[0]]=='#'):
            if inBounds(left[0],left[1]) and spiralmap[left[1]][left[0]]=='o':
                currentx-=1
                return False


        #if down is out of bounds and left is blocked switch gravity
        #if not inBounds(down[0],down[1]) and spiralmap[left[1]][left[0]]=='#':
        if (not canGo(down[0],down[1])) and (not canGo(left[0],left[1])):
            gravity=False
            #nextTile()

    if not gravity: # not gravity
        #lol i just did the opposite
        if inBounds(left[0],left[1]) and spiralmap[left[1]][left[0]]=='o':
            currentx-=1
            return False
        if not inBounds(left[0],left[1]) or spiralmap[left[1]][left[0]]=='#':
            if inBounds(up[0],up[1]) and spiralmap[up[1]][up[0]]=='o':
                currenty-=1
                return False
        if (not inBounds(left[0],left[1]) or spiralmap[left[1]][left[0]]=='#') and (not inBounds(up[0],up[1]) or spiralmap[up[1]][up[0]]=='#'):
            if inBounds(right[0],right[1]) and spiralmap[right[1]][right[0]]=='o':
                currentx+=1
                return False
            
        #if not inBounds(up[0],up[1]) and spiralmap[right[1]][right[0]]=='#':
        if (not canGo(up[0],up[1])) and (not canGo(right[0],right[1])):
            #after this does nothing tho
            gravity=True
            nextTile()
        

for i in range(steps):
    # m = input()
    # if m!='':
    #     exit()
        
    if nextTile() or i >= steps-1:
        # spiralmap[currenty][currentx]='A'
        # for row in spiralmap:
        #     print(row)
        print(currentx+1)
        print(currenty+1)
        break
    # print(i)
    # for row in spiralmap:
    #     print(row)


"""
7
5
3
2
8

10 
15 
2 
3 
70
"""
