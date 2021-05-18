import pygame

pygame.init() #초기화 꼭 시켜줘야됨

screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("This is a new game") #게임이름


#FPS (Frame Per Second)
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/yuzat/Desktop/pythonexercise/game/pygame_basic/background.png")

#call your sprite

character = pygame.image.load("C:/Users/yuzat/Desktop/pythonexercise/game/pygame_basic/character.png")
character_size = character.get_rect().size # take the size of the image
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2) # x_ position of the sprite
character_y_pos = screen_height - character_height # y position of the character


#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 1.5

#set the enemy

enemy = pygame.image.load("C:/Users/yuzat/Desktop/pythonexercise/game/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # take the size of the image
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2) # x_ position of the sprite
enemy_y_pos = screen_height/2 - enemy_height/2 # y position of the character



#이벤트 루프
running = True

while running:
    dt = clock.tick(100) # set FPS 게임화면의 초당 프레임 수를 설정
    #움직임의 부자연스러움이 생기는건 당연한거지만, 속도가 달라져서는 안된다
    # 캐릭터가 1초동안에 100만큼 이동해야돼(일정값으로 정해진)
    # 10fps 1초동안에 10번 동작, 즉 1번에 10만큼 이동 
    # 20fps 1초동안에 20번 동작, 즉 1번에 5만큼 이동
    # 하지만 속도가 바뀌면 안돼기 때문에 바꿔야된다

    

    #print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가

        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생함
            running = False #더이상 진행 ㄴㄴ
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt


    #가로 경곗값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경곗값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("!!!!!!Boom!!!!!!")
        running = False





    #screen.fill((0,0,255)) 배경화면 색상을 채우기
    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #draw the sprite
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #draw the enemy

    pygame.display.update()# 게임 화면을 계속계속 다시 업데이트

#파이게임 종료
pygame.quit()
