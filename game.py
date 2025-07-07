import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
ball_img = pygame.image.load(os.path.join(ASSETS_DIR, 'ball.png'))
basket_img = pygame.image.load(os.path.join(ASSETS_DIR, 'basket.png'))
ball_img = pygame.transform.scale(ball_img, (40, 40))
basket_img = pygame.transform.scale(basket_img, (100, 60))

# Font and clock
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

def game_loop():
    basket_x = WIDTH // 2
    basket_y = HEIGHT - 60
    basket_speed = 8

    ball_x = random.randint(0, WIDTH - 40)
    ball_y = 0
    ball_speed = 5

    score = 0
    running = True

    def draw_game():
        screen.fill(WHITE)
        screen.blit(basket_img, (basket_x, basket_y))
        screen.blit(ball_img, (ball_x, ball_y))
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - 100:
            basket_x += basket_speed

        # Move ball
        ball_y += ball_speed

        # Collision
        if basket_y < ball_y + 40 < basket_y + 10 and basket_x < ball_x < basket_x + 100:
            score += 1
            ball_y = 0
            ball_x = random.randint(0, WIDTH - 40)

        if ball_y > HEIGHT:
            ball_y = 0
            ball_x = random.randint(0, WIDTH - 40)

        draw_game()

    pygame.quit()

if __name__ == "__main__":
    game_loop()
