import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Màn hình game
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bắn Gà")

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Máy bay
plane_width, plane_height = 50, 50
plane_x = WIDTH // 2 - plane_width // 2
plane_y = HEIGHT - 2 * plane_height
plane_speed = 5
plane_health = 100

# Danh sách viên đạn
bullets = []
bullet_speed = 7

# Danh sách kẻ thù
enemies = []
enemy_speed = 1
enemy_spawn_rate = 25
enemy_health = 10

# Điểm số
score = 0

# Thời gian chơi
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

# Font
font = pygame.font.SysFont(None, 36)

def spawn_enemy():
    enemy_x = random.randint(0, WIDTH - 50)
    enemy_y = -50
    enemies.append([enemy_x, enemy_y, enemy_health])

def draw_health_bar():
    pygame.draw.rect(screen, RED, (plane_x, plane_y - 15, plane_health, 10))

def draw_score():
    score_text = font.render(f"Điểm: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Vòng lặp chính
while True:
    screen.fill((0, 0, 0))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển máy bay
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and plane_x > 0:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT] and plane_x < WIDTH - plane_width:
        plane_x += plane_speed

    # Bắn đạn
    if keys[pygame.K_SPACE] and len(bullets) < 100:
        bullets.append([plane_x + plane_width // 2, plane_y])

    # Di chuyển viên đạn và kiểm tra va chạm
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Kiểm tra va chạm máy bay với kẻ thù
    for enemy in enemies:
        enemy[1] += enemy_speed
        if (
            plane_x < enemy[0] < plane_x + plane_width
            and plane_y < enemy[1] < plane_y + plane_height
        ):
            plane_health -= 10
            enemies.remove(enemy)

        for bullet in bullets:
            if (
                enemy[0] < bullet[0] < enemy[0] + 50
                and enemy[1] < bullet[1] < enemy[1] + 50
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10

    # Nạp đạn
    if len(bullets) == 0:
        bullets = [[plane_x + plane_width // 2, plane_y]]

    # Xuất hiện kẻ thù ngẫu nhiên
    if random.randint(1, enemy_spawn_rate) == 1:
        spawn_enemy()

    # Vẽ máy bay và viên đạn
    pygame.draw.rect(screen, WHITE, (plane_x, plane_y, plane_width, plane_height))
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (bullet[0], bullet[1]), 5)

    # Vẽ kẻ thù
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], 50, 50))

    # Vẽ thanh máu
    draw_health_bar()

    # Vẽ điểm số
    draw_score()

    # Kiểm tra thanh máu và kết thúc game
    if plane_health <= 0:
        game_over()

    # Tính thời gian chơi
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    # Tăng tốc độ kẻ thù theo thời gian
    if elapsed_time % 10 == 0 and enemy_speed < 5:
        enemy_speed += 0.1

    pygame.display.flip()
    clock.tick(60)