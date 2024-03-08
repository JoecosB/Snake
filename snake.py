import pygame
import random
import sys

#定义蛇类
class snake:
    """蛇！"""
    def __init__(self, body, direction):
        '''初始化类'''
        self.body = body
        self.d = direction
    
    def move(self):
        '''蛇的移动'''
        move_list = [(0, -10), (10, 0), (0, 10), (-10, 0)]
        x = self.body[0][0]+move_list[self.d][0]
        y = self.body[0][1]+move_list[self.d][1]
        if x < 11:
            x = 501
        if x > 501:
            x = 11
        if y < 11:
            y = 501
        if y > 501:
            y = 11            
        self.body.insert(0, (x,y))
        screen.blit(s_void, self.body.pop())

    def grow(self):
        self.body.append(self.body[-1])
    
def apple():
    '''在随机空白位置画苹果'''
    blank = []
    for x in range(11, 501, 10):
        for y in range(11, 501, 10):
            if screen.get_at((x, y)) == (0,0,0,255):
                blank.append((x, y))
    location = blank[random.randint(0, len(blank)-1)]
    screen.blit(a_block, location)
    return location

def s_draw(body):
    '''将蛇画在屏幕上'''
    for block in body[1:]:
        screen.blit(s_block, block)
    screen . blit(s_head, body[0])

def apple_eat(location):
    '''检测是不是吃到苹果'''
    if s.body[0] == location:
        return True
    else:
        return False
    
def collision():
    '''检测蛇头是否与蛇身碰撞'''
    colli = False
    for block in s.body[1:]:
        if s.body[0] == block:
            colli = True
    return colli

#初始化显示，创建一个520*520的窗口，标题为Snake。
pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((520,520))
arena = pygame.Surface((500, 500), flags=pygame.HWSURFACE)
s_block = pygame.Surface((10,10), flags=pygame.HWSURFACE)
s_head = pygame.Surface((10,10), flags=pygame.HWSURFACE)
s_void = pygame.Surface((10,10), flags=pygame.HWSURFACE)
a_block = pygame.Surface((10,10), flags=pygame.HWSURFACE)
screen.fill('white')
arena.fill('black')
s_block.fill('grey')
s_head.fill('blue')
s_void.fill('black')
a_block.fill('red')
screen.blit(arena, (11,11))
pygame.display.flip()

#初始化蛇
s = snake([(11,481), (11,491), (11,501)], 0)
d_pre= 0
con = True
game_fail = False

#事件监听和刷新显示。
while True:
    if game_fail == False:
        #防止有傻逼原地掉头
        if abs(s.d - d_pre) == 2:
            s.d = d_pre

        #等待一会
        pygame.time.wait(100)

        #将这一次的方向存入d_pre
        d_pre = s.d

        #若果生成条件是true，则生成苹果
        if con == True:
            location = apple()
            con = False

        #移动蛇身并画出来
        s.move()
        s_draw(s.body)

        #如果吃到苹果，就把苹果声称条件改为true，并生长蛇
        if apple_eat(location) == True:
            s.grow()
            con= True

        #检测碰撞，如果碰撞，则游戏结束
        if collision() == True:
            for block in s.body:
                screen.blit(a_block, block)
                game_fail = True

        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                s.d = 0
            elif event.key == pygame.K_RIGHT:
                s.d = 1
            elif event.key == pygame.K_DOWN:
                s.d = 2
            elif event.key == pygame.K_LEFT:
                s.d = 3