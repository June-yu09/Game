import pygame

pygame.init() #초기화 반드시 필요

# 화면크기 조정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("This is game") #게임 이름

#이벤트 루프
running = True #게임이 진행중인가를 확인
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했나
        if event.type == pygame.QUIT: # 엑스를 눌러 창이 닫히는 이벤트 발생
            running = False # 게임이 더이상 안돌아감
            
# pygame exit
pygame.quit()