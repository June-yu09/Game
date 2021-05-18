import pygame
import random

###################################################################
#기본 초기화 (반드시 해야되는 것들)
pygame.init()

#초기화 꼭 시켜줘야됨


#화면 크기 설정
#가로크기
screen_width = 480
#세로크기
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
#게임이름
pygame.display.set_caption("Pihagi")


#FPS (Frame Per Second)
clock = pygame.time.Clock()


#####################################################################

#1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표,이동속도, 캐릭터, 폰트 등등)

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/yuzat/Desktop/pythonexercise/game/pygame_basic/background.png")

# 캐릭터만들기
character = pygame.image.load("C:/Users/yuzat/Desktop/pythonexercise/game/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

#이동할 좌표

to_x = 0
to_y = 0

#이동속도
character_speed = 1.5

#폰트정의
game_font = pygame.font.Font(None, 100)
#총 시간
total_time = 50

#시작 시간 정보
start_ticks = pygame.time.get_ticks()


#enemy
enemy = pygame.image.load("C:/Users/yuzat/Desktop/pythonexercise/game/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0



#이벤트 루프
running = True
while running:
    dt = clock.tick(30)

# 
# 
# # set FPS 게임화면의 초당 프레임 수를 설정
    #움직임의 부자연스러움이 생기는건 당연한거지만, 속도가 달라져서는 안된다
    # 캐릭터가 1초동안에 100만큼 이동해야돼(일정값으로 정해진)
    # 10fps 1초동안에 10번 동작, 즉 1번에 10만큼 이동 
    # 20fps 1초동안에 20번 동작, 즉 1번에 5만큼 이동
    # 하지만 속도가 바뀌면 안돼기 때문에 바꿔야된다

    

    #print("fps : " + str(clock.get_fps()))


################2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크

    enemy_y_pos += character_speed*3

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    if character_rect.colliderect(enemy_rect):
        print("Boom")
        running = False

##########3. 게임캐릭터 위치 정의
    #가로 경곗값 처리
    #세로 경곗값 처리

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    






#########5 화면에 그리기
    #screen.fill((0,0,255)) 배경화면 색상을 채우기

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))




    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (100,150,33))
    screen.blit(timer, (10,10))
    if total_time - elapsed_time < 0:
        print("Time out")
        running = False    

###########6. 업데이트 
    pygame.display.update()

#파이게임 종료
pygame.quit()
