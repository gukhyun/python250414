import pygame
import random
import time

# 초기화
pygame.init()

# 화면 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("뱀 게임: 사람 vs 기계")

# 시계 객체
clock = pygame.time.Clock()

# 뱀 초기화
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# 기계 뱀 초기화
ai_snake_pos = [300, 200]
ai_snake_body = [[300, 200], [290, 200], [280, 200]]
ai_snake_direction = 'LEFT'

# 음식 초기화
food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
food_spawn = True

# 점수
player_score = 0
ai_score = 0

# 점수 표시 함수
def show_score():
    font = pygame.font.SysFont('times new roman', 20)
    player_text = font.render(f'Player: {player_score}', True, WHITE)
    ai_text = font.render(f'AI: {ai_score}', True, YELLOW)
    screen.blit(player_text, (10, 10))
    screen.blit(ai_text, (SCREEN_WIDTH - 100, 10))

# 게임 종료 함수
def game_over():
    screen.fill(BLACK)
    font = pygame.font.SysFont('times new roman', 50)
    if player_score > ai_score:
        message = "Player Wins!"
    elif player_score < ai_score:
        message = "AI Wins!"
    else:
        message = "It's a Tie!"
    text = font.render(message, True, RED)
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# AI 뱀 움직임
def move_ai_snake():
    global ai_snake_direction
    if ai_snake_pos[0] < food_pos[0] and ai_snake_direction != 'LEFT':
        ai_snake_direction = 'RIGHT'
    elif ai_snake_pos[0] > food_pos[0] and ai_snake_direction != 'RIGHT':
        ai_snake_direction = 'LEFT'
    elif ai_snake_pos[1] < food_pos[1] and ai_snake_direction != 'UP':
        ai_snake_direction = 'DOWN'
    elif ai_snake_pos[1] > food_pos[1] and ai_snake_direction != 'DOWN':
        ai_snake_direction = 'UP'

    if ai_snake_direction == 'UP':
        ai_snake_pos[1] -= BLOCK_SIZE
    if ai_snake_direction == 'DOWN':
        ai_snake_pos[1] += BLOCK_SIZE
    if ai_snake_direction == 'LEFT':
        ai_snake_pos[0] -= BLOCK_SIZE
    if ai_snake_direction == 'RIGHT':
        ai_snake_pos[0] += BLOCK_SIZE

# 게임 루프
def main():
    global snake_pos, snake_body, snake_direction, change_to, food_pos, food_spawn, player_score
    global ai_snake_pos, ai_snake_body, ai_snake_direction, ai_score

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not snake_direction == 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and not snake_direction == 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and not snake_direction == 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and not snake_direction == 'LEFT':
                    change_to = 'RIGHT'

        # 방향 변경
        snake_direction = change_to

        # 뱀 이동
        if snake_direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        if snake_direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE
        if snake_direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        if snake_direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE

        # AI 뱀 이동
        move_ai_snake()

        # 뱀 몸 길이 증가
        snake_body.insert(0, list(snake_pos))
        ai_snake_body.insert(0, list(ai_snake_pos))

        if snake_pos == food_pos:
            player_score += 10
            food_spawn = False
        else:
            snake_body.pop()

        if ai_snake_pos == food_pos:
            ai_score += 10
            food_spawn = False
        else:
            ai_snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                        random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]
        food_spawn = True

        # 화면 그리기
        screen.fill(BLACK)
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        for pos in ai_snake_body:
            pygame.draw.rect(screen, BLUE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # 경계 충돌
        if (snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH or
                snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT):
            game_over()

        if (ai_snake_pos[0] < 0 or ai_snake_pos[0] >= SCREEN_WIDTH or
                ai_snake_pos[1] < 0 or ai_snake_pos[1] >= SCREEN_HEIGHT):
            game_over()

        # 자기 자신과 충돌
        for block in snake_body[1:]:
            if snake_pos == block:
                game_over()

        for block in ai_snake_body[1:]:
            if ai_snake_pos == block:
                game_over()

        # 점수 표시
        show_score()

        # 화면 업데이트
        pygame.display.flip()

        # 게임 속도
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()