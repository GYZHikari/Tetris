# Copyright: Guangyu Zhong all rights reserved
# Author Guangyu Zhong: Guangyuzhonghikari@gmail.com
# date 2015-04-26
# Description: Tetris game based on Python 2.7 + pygame
import prepare
import pygame
import random
import os
from pygame.locals import *


class Grid:
    def __init__(self, name):
        self.grid_image = prepare.load_image(name)
        self.grid_width = self.grid_image.get_width()
        self.grid_height = self.grid_image.get_height()
        col = 0
        row = 0
        self.grid_matrix = [[0 for col in range(10)] for row in range(21)]
        self.grid_mode = [[0 for col in range(10)] for row in range(21)]
        for i in range(10):
            self.grid_matrix[20][i] = 1

    def drawImage(self, x, y):
        screen.blit(self.grid_image, (x, y))

    def drawAddImage(self, x, y):
        for i in range(20):
            for j in range(10):
                if self.grid_matrix[i][j] == 1:
                    draw_x = x + j * 20
                    draw_y = y + i * 20
                    draw_image = prepare.load_image(str(grid.grid_mode[i][j]) + '.png')
                    screen.blit(draw_image, (draw_x, draw_y))

    def addGrid(self, x, y):
        self.grid_matrix[x][y] = 1

    def detecCollision(self, WholeBlock, direct):
        # down
        if direct == 0:
            flag = 0
            for i in range(4):
                temp_y = WholeBlock.blocks[i].y + WholeBlock.yVal + 1
                temp_x = WholeBlock.blocks[i].x + WholeBlock.xVal + 4
                #print temp_y, temp_x, self.grid_matrix[temp_y][temp_x]
                if self.grid_matrix[temp_y][temp_x] == 1:
                    flag = 1
        #left
        elif direct == 1:
            flag = 0
            for i in range(4):
                temp_y = WholeBlock.blocks[i].y + WholeBlock.yVal
                temp_x = WholeBlock.blocks[i].x + WholeBlock.xVal + 4 - 1
                if self.grid_matrix[temp_y][temp_x] == 1:
                    flag = 1
        #right
        elif direct == 2:
            flag = 0
            for i in range(4):
                temp_y = WholeBlock.blocks[i].y + WholeBlock.yVal
                temp_x = WholeBlock.blocks[i].x + WholeBlock.xVal + 4 + 1
                if self.grid_matrix[temp_y][temp_x] == 1:
                    flag = 1
        return flag

    def detectRemove(self):
        for i in range(19, 0, -1):
            if sum(self.grid_matrix[i]) == 10:
                #print i
                for j in range(10):
                    self.grid_matrix[i][j] = 0
                    self.grid_mode[i][j] = 0
                for k in range(i, 1, -1):
                    for j in range(10):
                        if self.grid_matrix[k][j] == 1:
                            self.grid_mode[k+1][j] = self.grid_mode[k][j]
                            self.grid_matrix[k][j] = 0
                            self.grid_matrix[k+1][j] = 1
                            self.grid_mode[k][j] = 0

    def detectGameOver(self):
        flag = 0
        for i in range(10):
            if self.grid_matrix[0][i] == 1:
                flag = 1
            for j in range(4):
                temp_x = next_block.blocks[j].x + next_block.xVal + 4
                temp_y = next_block.blocks[j].y + next_block.yVal
                if self.grid_matrix[temp_y][temp_x] == 1:
                    flag = 1

        return flag

class UnitBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WholeBlock:
    def __init__(self, mode):
        self.xVal = 0
        self.yVal = 0
        self.state = 0
        self.collision = 0
        self.mode = mode
        if mode == 0:
            # I#
            self.blocks_image = prepare.load_image("0.png")
            self.blocks = [UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(1, 2), UnitBlock(1, 3)]
        elif mode == 1:
            # J#
            self.blocks_image = prepare.load_image("1.png")
            self.blocks = [UnitBlock(0, 0), UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(2, 1)]
        elif mode == 2:
            # L#
            self.blocks_image = prepare.load_image("2.png")
            self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(2, 1), UnitBlock(2, 0)]
        elif mode == 3:
            # 0#
            self.blocks_image = prepare.load_image("3.png")
            self.blocks = [UnitBlock(0, 0), UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(1, 0)]
        elif mode == 4:
            # S#
            self.blocks_image = prepare.load_image("4.png")
            self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(1, 0), UnitBlock(2, 0)]
        elif mode == 5:
            # T#
            self.blocks_image = prepare.load_image("5.png")
            self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(1, 0), UnitBlock(2, 1)]
        elif mode == 6:
            # Z#
            self.blocks_image = prepare.load_image("6.png")
            self.blocks = [UnitBlock(0, 0), UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(2, 1)]
        self.size = self.blocks_image.get_width()

    def rotation(self):
        if self.mode == 0:
            # I#
            if self.state == 0:
                self.blocks = [UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(1, 2), UnitBlock(1, 3)]
            elif self.state == 1:
                self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(2, 1), UnitBlock(3, 1)]
        elif self.mode == 1:
            # J#
            if self.state == 0:
                self.blocks = [UnitBlock(0, 0), UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(2, 1)]
            elif self.state == 1:
                self.blocks = [UnitBlock(1, 0), UnitBlock(0, 0), UnitBlock(0, 1), UnitBlock(0, 2)]
            elif self.state == 2:
                self.blocks = [UnitBlock(0, 0), UnitBlock(1, 0), UnitBlock(2, 0), UnitBlock(2, 1)]
            elif self.state == 3:
                self.blocks = [UnitBlock(0, 2), UnitBlock(1, 2), UnitBlock(1, 1), UnitBlock(1, 0)]
        elif self.mode == 2:
            # L#
            if self.state == 0:
                self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(2, 1), UnitBlock(2, 0)]
            elif self.state == 1:
                self.blocks = [UnitBlock(0, 0), UnitBlock(0, 1), UnitBlock(0, 2), UnitBlock(1, 2)]
            elif self.state == 2:
                self.blocks = [UnitBlock(0, 0), UnitBlock(1, 0), UnitBlock(2, 0), UnitBlock(0, 1)]
            elif self.state == 3:
                self.blocks = [UnitBlock(0, 0), UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(1, 2)]
        elif self.mode == 3:
            # 0#
            if self.state == 0:
                self.blocks = [UnitBlock(0, 0), UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(1, 0)]
        elif self.mode == 4:
            # S#
            if self.state == 0:
                self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(1, 0), UnitBlock(2, 0)]
            elif self.state == 1:
                self.blocks = [UnitBlock(0, 0), UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(1, 2)]
        elif self.mode == 5:
            # T#
            if self.state == 0:
                self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(1, 0), UnitBlock(2, 1)]
            elif self.state == 1:
                self.blocks = [UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(1, 2), UnitBlock(2, 1)]
            elif self.state == 2:
                self.blocks = [UnitBlock(0, 1), UnitBlock(1, 1), UnitBlock(2, 1), UnitBlock(1, 2)]
            elif self.state == 3:
                self.blocks = [UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(1, 2), UnitBlock(0, 1)]
        elif self.mode == 6:
            # Z#
            if self.state == 0:
                self.blocks = [UnitBlock(0, 0), UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(2, 1)]
            elif self.state == 1:
                self.blocks = [UnitBlock(1, 0), UnitBlock(1, 1), UnitBlock(0, 1), UnitBlock(0, 2)]

    def judgeRotation(self):
        rotation_flag = 1
        #print rotation_flag
        posLeft = min(self.blocks[0].x, self.blocks[1].x, self.blocks[2].x, self.blocks[3].x) + self.xVal
        posRight = max(self.blocks[0].x, self.blocks[1].x, self.blocks[2].x, self.blocks[3].x) + self.xVal
        posTop = min(self.blocks[0].y, self.blocks[1].y, self.blocks[2].y, self.blocks[3].y) + self.yVal
        posDown = max(self.blocks[0].y, self.blocks[1].y, self.blocks[2].y, self.blocks[3].y) + self.yVal

        if (posLeft <= -5) or (posRight >= 6) or (posTop <= -1) or (posDown >= 20):
            rotation_flag = 0
        else:
            for i in range(4):
                temp_x = self.blocks[i].x + self.xVal + 4
                temp_y = self.blocks[i].y + self.yVal
                if (temp_x >= 0) and (temp_x < 10) and (temp_y >= 0) and (temp_y < 20):
                    if grid.grid_matrix[temp_y][temp_x] == 1:
                        rotation_flag = 0
        #print rotation_flag
        if rotation_flag == 1:
            return 1
        else:
            return 0

    def clockwise(self):
        if self.mode == 0 or self.mode == 4 or self.mode == 6:
            self.state = (self.state + 1) % 2
            '''print 'state tobe: ', self.state'''
            self.rotation()
            if self.judgeRotation() == 0:
                self.state = (self.state - 1) % 2
                self.rotation()
        elif self.mode == 1 or self.mode == 2 or self.mode == 5:
            self.state = (self.state + 1) % 4
            '''print 'state tobe: ', self.state'''
            self.rotation()
            if self.judgeRotation() == 0:
                self.state = (self.state - 1) % 4
                self.rotation()
        '''print 'final state: ', self.state'''

    def anticlockwise(self):
        if self.mode == 0 or self.mode == 4 or self.mode == 6:
            self.state = (self.state + 2 - 1) % 2
            '''print 'state tobe: ', self.state'''
            self.rotation()
            '''print 'judge: ', self.judge'''
            if self.judgeRotation() == 0:
                self.state = (self.state + 2 + 1) % 2
                self.rotation()
        elif self.mode == 1 or self.mode == 2 or self.mode == 5:
            self.state = (self.state + 4 - 1) % 4
            '''print 'state tobe: ', self.state'''
            self.rotation()

            '''print 'judge: ', self.judge()'''
            if self.judgeRotation() == 0:
                self.state = (self.state + 4 + 1) % 4
                self.rotation()
        '''print 'final state: ', self.state'''

    def move2left(self):
        min_x = min(self.blocks[0].x, self.blocks[1].x, self.blocks[2].x, self.blocks[3].x)
        if (min_x + self.xVal) > -4:
            if Grid.detecCollision(grid, self, 1) == 0:
                self.xVal -= 1

    def move2right(self):
        max_x = max(self.blocks[0].x, self.blocks[1].x, self.blocks[2].x, self.blocks[3].x)
        if (max_x + self.xVal) < 5:
            if Grid.detecCollision(grid, self, 2) == 0:
                self.xVal += 1

    def move2down(self):
        max_y = max(self.blocks[0].y, self.blocks[1].y, self.blocks[2].y, self.blocks[3].y)
        if (max_y + self.yVal) <= 19:
            if Grid.detecCollision(grid, self, 0) == 0:
                self.yVal += 1
            else:
                self.collision = 1
                for i in range(4):
                    add_x = self.blocks[i].y + self.yVal
                    add_y = self.blocks[i].x + self.xVal + 4
                    #print add_x, add_y
                    Grid.addGrid(grid, add_x, add_y)
                    grid.grid_mode[add_x][add_y] = self.mode

    def fall(self):
        self.yVal += 1

    def drawblocks(self, x, y):
        for i in range(0, 4):
            drawx = x + (self.blocks[i].x + self.xVal) * self.size
            drawy = y + (self.blocks[i].y + self.yVal) * self.size
            screen.blit(self.blocks_image, (drawx, drawy))
def game(block, in_posx, next_posx, next_block, fall_counter, pause_flag):
    while 1:
        restart = 0
        #print next_block.mode
        grid.drawImage(0, 0)
        grid.drawAddImage(0, 0)
            #print block.mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
                #print block.mode
                if event.key == K_DOWN:
                    block.move2down()
                    #print block.collision
                elif event.key == K_LEFT:
                    block.move2left()
                    '''print 'xVal: ', block.xVal'''
                elif event.key == K_RIGHT:
                    block.move2right()
                    '''print 'xVal: ', block.xVal'''
                elif event.key == K_z:
                    block.anticlockwise()
                elif event.key == K_x:
                    block.clockwise()
                elif event.key == K_p:
                    pause_flag = (pause_flag + 1) % 2
                elif event.key == K_r:
                    block.__init__(random.randint(0, 6))
                    next_mode = random.randint(0, 6)
                    next_block.__init__(next_mode)
                    grid.__init__("back1.jpg")
                    pause_flag = 0
                    fall_counter = 0
                    restart = 1

        if restart == 0:
            if grid.detectGameOver():
                print next_block.mode
                over(block, next_block, in_posx, next_posx, overimg)
            elif pause_flag == 0:
                if fall_counter > 100:
                    block.move2down()
                    fall_counter = 0
                block.drawblocks(in_posx, 0)
                grid.detectRemove()
                next_block.drawblocks(next_posx, 0)
            else:
                pause(block, next_block, in_posx, next_posx, pauseimg)
        pygame.display.update()
        return (block.collision, fall_counter, pause_flag)

def pause(block, next_block, in_posx, next_posx, img):
    grid.drawImage(0, 0)
    grid.drawAddImage(0, 0)
    #print block.xVal, block.yVal
    block.drawblocks(in_posx, 0)
    next_block.drawblocks(next_posx, 0)
    screen.blit(img, (40, 180))
    return 1

def over(block, next_block, in_posx, next_posx, img):
    grid.drawImage(0, 0)
    grid.drawAddImage(0, 0)
    #print block.xVal, block.yVal
    block.drawblocks(in_posx, 0)
    next_block.drawblocks(next_posx, 0)
    screen.blit(img, (40, 180))

def main(next_block):
    pause_flag = 0
    fall_counter = 0
    restart = 0
    while 1:
            (flag,  fall_counter, pause_flag) = game(block, in_posx, next_posx, next_block, fall_counter, pause_flag)
            fall_counter += 1
            if flag == 1:
                mode = next_block.mode
                block.__init__(mode)
                next_mode = random.randint(0, 6)
                next_block = WholeBlock(next_mode)

pygame.init()
grid = Grid("back.png")
overimg = prepare.load_image("over.png")
pauseimg = prepare.load_image("pause.png")
#print grid.grid_width, grid.grid_height

screen = pygame.display.set_mode((grid.grid_width, grid.grid_height))
block = WholeBlock(random.randint(0, 6))
in_posx = block.size * 4
next_posx = block.size * 11
next_mode = random.randint(0, 6)
next_block = WholeBlock(next_mode)
#print next_block.mode
clock = pygame.time.Clock()
clock.tick(30)

main(next_block)
