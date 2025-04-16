import pygame
import random

# 초기화
pygame.init()

# 화면 크기
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (128, 0, 128),  # Purple
    (0, 255, 0),    # Green
    (255, 0, 0)     # Red
]

# 테트리스 블록 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("테트리스")

# 게임 그리드
grid = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]

# 블록 클래스
class Block:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(COLORS)
        self.x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

# 블록 그리기
def draw_block(block):
    for i, row in enumerate(block.shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    block.color,
                    pygame.Rect(
                        (block.x + j) * BLOCK_SIZE,
                        (block.y + i) * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE
                    )
                )

# 충돌 감지
def check_collision(block, dx, dy):
    for i, row in enumerate(block.shape):
        for j, cell in enumerate(row):
            if cell:
                new_x = block.x + j + dx
                new_y = block.y + i + dy
                if new_x < 0 or new_x >= len(grid[0]) or new_y >= len(grid) or grid[new_y][new_x]:
                    return True
    return False

# 블록 고정
def fix_block(block):
    for i, row in enumerate(block.shape):
        for j, cell in enumerate(row):
            if cell:
                grid[block.y + i][block.x + j] = 1

# 라인 제거
def clear_lines():
    global grid
    grid = [row for row in grid if any(cell == 0 for cell in row)]
    while len(grid) < SCREEN_HEIGHT // BLOCK_SIZE:
        grid.insert(0, [0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])

# 게임 루프
def main():
    clock = pygame.time.Clock()
    current_block = Block(random.choice(SHAPES))
    running = True
    fall_time = 0

    while running:
        screen.fill(BLACK)
        draw_block(current_block)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(current_block, -1, 0):
                    current_block.x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(current_block, 1, 0):
                    current_block.x += 1
                elif event.key == pygame.K_DOWN and not check_collision(current_block, 0, 1):
                    current_block.y += 1
                elif event.key == pygame.K_UP:
                    current_block.rotate()
                    if check_collision(current_block, 0, 0):
                        current_block.rotate()
                        current_block.rotate()
                        current_block.rotate()
                elif event.key == pygame.K_SPACE:
                    while not check_collision(current_block, 0, 1):
                        current_block.y += 1

        fall_time += clock.get_rawtime()
        clock.tick(30)

        if fall_time > 500:
            fall_time = 0
            if not check_collision(current_block, 0, 1):
                current_block.y += 1
            else:
                fix_block(current_block)
                clear_lines()
                current_block = Block(random.choice(SHAPES))
                if check_collision(current_block, 0, 0):
                    running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()