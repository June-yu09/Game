import pygame

pygame.init() #초기화 꼭 시켜줘야됨

screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("This is a new game") #게임이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/yuzat/Desktop/pythonexercise/game/pygame_basic/background.png")




#이벤트 루프
running = True

while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생함
            running = False #더이상 진행 ㄴㄴ

    #screen.fill((0,0,255)) 색상을 채우기
    screen.blit(background, (0,0)) #배경 그리기
    pygame.display.update()# 게임 화면을 계속계속 다시 업데이트

#파이게임 종료
pygame.quit()
