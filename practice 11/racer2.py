import pygame
import random
import sys

# Initialize pygame and sound module
pygame.init()
pygame.mixer.init()

# -----------------------------
# Basic game settings
# -----------------------------
SCREEN_W, SCREEN_H = 400, 600
FPS = 60

# Road boundaries and lane width
ROAD_LEFT = 60
ROAD_RIGHT = 340
LANE_W = (ROAD_RIGHT - ROAD_LEFT) // 3

# -----------------------------
# Colours
# -----------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROAD = (65, 65, 75)
ROAD_DARK = (45, 45, 55)
ROAD_LINE = (240, 240, 180)
SKY_GREEN = (85, 160, 95)
GRASS_DARK = (45, 120, 60)

YELLOW = (255, 215, 0)
GOLD = (200, 160, 0)
SILVER = (190, 190, 190)
BRONZE = (180, 100, 40)

RED = (210, 30, 30)
BLUE = (40, 120, 230)
LT_BLU = (160, 210, 255)
PURPLE = (150, 70, 190)

# -----------------------------
# Coin and speed-up settings
# -----------------------------
COINS_PER_SPEEDUP = 5
SPEEDUP_AMOUNT = 0.5

# Coin types:
# value = how many points the coin gives
# weight = chance of appearing
COIN_TYPES = [
    {"label": "Bronze", "value": 1, "colour": BRONZE, "weight": 60},
    {"label": "Silver", "value": 2, "colour": SILVER, "weight": 30},
    {"label": "Gold", "value": 3, "colour": GOLD, "weight": 10},
]

# -----------------------------
# Window, clock and fonts
# -----------------------------
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 22, bold=True)
big = pygame.font.SysFont("Arial", 48, bold=True)
small = pygame.font.SysFont("Arial", 14, bold=True)

# -----------------------------
# Sounds
# -----------------------------
crash_sound = pygame.mixer.Sound(
    r"C:\Users\kalma\Documents\python\python\practice 10\racer\sound\crash.mp3"
)

coin_sound = pygame.mixer.Sound(
    r"C:\Users\kalma\Documents\python\python\practice 10\racer\sound\coin.mp3"
)


# Randomly chooses a coin type based on its weight.
# Bigger weight means higher chance to appear.
def weighted_choice(items):
    total = sum(item["weight"] for item in items)
    number = random.randint(1, total)

    current = 0
    for item in items:
        current += item["weight"]
        if number <= current:
            return item

    return items[-1]


# Returns a random x-position inside one of the road lanes.
def random_lane_x(obj_width):
    lane = random.randint(0, 2)
    return ROAD_LEFT + lane * LANE_W + (LANE_W - obj_width) // 2


class Road:
    # This class draws and scrolls the road.
    LINE_H = 55
    LINE_GAP = 35
    SEGMENT = LINE_H + LINE_GAP

    def __init__(self):
        self.offset = 0
        self.speed = 5

    # Moves the dashed lane lines down to create movement effect.
    def update(self):
        self.offset = (self.offset + self.speed) % self.SEGMENT

    # Draws grass, road, road borders and lane lines.
    def draw(self, surface):
        surface.fill(SKY_GREEN)

        pygame.draw.rect(surface, GRASS_DARK, (0, 0, ROAD_LEFT, SCREEN_H))
        pygame.draw.rect(surface, GRASS_DARK, (ROAD_RIGHT, 0, SCREEN_W - ROAD_RIGHT, SCREEN_H))

        pygame.draw.rect(surface, ROAD, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, SCREEN_H))
        pygame.draw.rect(surface, ROAD_DARK, (ROAD_LEFT + 25, 0, ROAD_RIGHT - ROAD_LEFT - 50, SCREEN_H))

        pygame.draw.rect(surface, ROAD_LINE, (ROAD_LEFT - 5, 0, 5, SCREEN_H))
        pygame.draw.rect(surface, ROAD_LINE, (ROAD_RIGHT, 0, 5, SCREEN_H))

        for lane in range(1, 3):
            x = ROAD_LEFT + LANE_W * lane - 2
            y = self.offset - self.SEGMENT

            while y < SCREEN_H:
                pygame.draw.rect(surface, WHITE, (x, y, 4, self.LINE_H), border_radius=3)
                y += self.SEGMENT


class PlayerCar:
    # Player-controlled car.
    W, H = 42, 72

    def __init__(self):
        self.x = SCREEN_W // 2 - self.W // 2
        self.y = SCREEN_H - 110
        self.spd = 5

    # Draws the player car using polygon body, windows and wheels.
    def draw(self, surface):
        x, y, w, h = self.x, self.y, self.W, self.H

        points = [
            (x + w // 2, y),
            (x + w - 4, y + 12),
            (x + w, y + h - 10),
            (x + w // 2, y + h),
            (x, y + h - 10),
            (x + 4, y + 12)
        ]
        pygame.draw.polygon(surface, BLUE, points)

        pygame.draw.rect(surface, LT_BLU, (x + 9, y + 12, w - 18, 16), border_radius=5)
        pygame.draw.rect(surface, LT_BLU, (x + 9, y + h - 25, w - 18, 13), border_radius=5)

        pygame.draw.rect(surface, BLACK, (x - 5, y + 14, 8, 16), border_radius=3)
        pygame.draw.rect(surface, BLACK, (x + w - 3, y + 14, 8, 16), border_radius=3)
        pygame.draw.rect(surface, BLACK, (x - 5, y + h - 30, 8, 16), border_radius=3)
        pygame.draw.rect(surface, BLACK, (x + w - 3, y + h - 30, 8, 16), border_radius=3)

    # Moves the player car with arrow keys.
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > ROAD_LEFT:
            self.x -= int(self.spd)

        if keys[pygame.K_RIGHT] and self.x + self.W < ROAD_RIGHT:
            self.x += int(self.spd)

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= int(self.spd)

        if keys[pygame.K_DOWN] and self.y + self.H < SCREEN_H:
            self.y += int(self.spd)

    # Collision rectangle for player car.
    def rect(self):
        return pygame.Rect(self.x + 5, self.y + 5, self.W - 10, self.H - 10)


class EnemyCar:
    # Enemy car moves down from the top of the screen.
    W, H = 42, 72

    def __init__(self, speed):
        self.x = random_lane_x(self.W)
        self.y = -self.H - random.randint(0, 60)
        self.spd = speed
        self.col = random.choice([RED, PURPLE, (230, 120, 40)])

    # Draws enemy car with a different rounded shape.
    def draw(self, surface):
        x, y, w, h = self.x, self.y, self.W, self.H

        pygame.draw.ellipse(surface, self.col, (x, y, w, h))
        pygame.draw.rect(surface, self.col, (x + 4, y + 10, w - 8, h - 20), border_radius=10)

        pygame.draw.rect(surface, LT_BLU, (x + 9, y + h - 28, w - 18, 15), border_radius=5)

        pygame.draw.rect(surface, BLACK, (x - 4, y + 15, 8, 15), border_radius=3)
        pygame.draw.rect(surface, BLACK, (x + w - 4, y + 15, 8, 15), border_radius=3)
        pygame.draw.rect(surface, BLACK, (x - 4, y + h - 30, 8, 15), border_radius=3)
        pygame.draw.rect(surface, BLACK, (x + w - 4, y + h - 30, 8, 15), border_radius=3)

    # Moves enemy down.
    def update(self):
        self.y += self.spd

    # Checks whether enemy is outside the screen.
    def off_screen(self):
        return self.y > SCREEN_H

    # Collision rectangle for enemy car.
    def rect(self):
        return pygame.Rect(self.x + 5, self.y + 5, self.W - 10, self.H - 10)


class Coin:
    # Coin has different value and random chance of appearing.
    R = 12

    def __init__(self, speed):
        coin_type = weighted_choice(COIN_TYPES)

        self.label = coin_type["label"]
        self.value = coin_type["value"]
        self.colour = coin_type["colour"]

        self.x = random.randint(ROAD_LEFT + self.R + 2, ROAD_RIGHT - self.R - 2)
        self.y = -self.R
        self.spd = speed

    # Draws coin and its value.
    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.R)
        pygame.draw.circle(surface, BLACK, (self.x, self.y), self.R, 2)

        value_text = small.render(str(self.value), True, BLACK)
        surface.blit(
            value_text,
            (self.x - value_text.get_width() // 2, self.y - value_text.get_height() // 2)
        )

    # Moves coin down.
    def update(self):
        self.y += self.spd

    # Checks if coin left the screen.
    def off_screen(self):
        return self.y - self.R > SCREEN_H

    # Collision rectangle for coin.
    def rect(self):
        return pygame.Rect(self.x - self.R, self.y - self.R, self.R * 2, self.R * 2)


# Draws score, coins and current enemy speed.
def draw_hud(surface, score, coins, next_speedup, enemy_speed):
    hud = pygame.Surface((SCREEN_W, 70), pygame.SRCALPHA)
    hud.fill((0, 0, 0, 130))
    surface.blit(hud, (0, 0))

    s = font.render(f"Score: {score}", True, WHITE)
    c = font.render(f"Coins: {coins}/{next_speedup}", True, YELLOW)
    sp = small.render(f"Enemy speed: {enemy_speed:.1f}", True, WHITE)

    surface.blit(s, (10, 8))
    surface.blit(c, (SCREEN_W - c.get_width() - 10, 8))
    surface.blit(sp, (10, 42))


# Shows coin types and their values at the top center.
def draw_coin_legend(surface):
    x = SCREEN_W // 2 - 65
    y = 8

    for coin_type in COIN_TYPES:
        pygame.draw.circle(surface, coin_type["colour"], (x, y + 8), 7)

        label = small.render(
            f"{coin_type['label']} +{coin_type['value']}",
            True,
            WHITE
        )

        surface.blit(label, (x + 15, y))
        y += 18


# Draws game over screen.
def draw_game_over(surface, score, coins):
    overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 170))
    surface.blit(overlay, (0, 0))

    lines = [
        (big, "GAME OVER", RED),
        (font, f"Score: {score}", WHITE),
        (font, f"Coins: {coins}", YELLOW),
        (font, "R - restart   Q - quit", WHITE),
    ]

    y = 190
    for f, text, color in lines:
        txt = f.render(text, True, color)
        surface.blit(txt, (SCREEN_W // 2 - txt.get_width() // 2, y))
        y += txt.get_height() + 14


# Main game function.
def main():
    road = Road()
    player = PlayerCar()

    enemies = []
    coins = []

    score = 0
    coin_count = 0

    base_speed = 4
    enemy_speed = base_speed
    coin_speed = base_speed

    # Shows how many coins are needed for the next speed increase.
    next_speedup = COINS_PER_SPEEDUP

    game_over = False
    crash_played = False

    enemy_timer = 0
    enemy_interval = 80

    coin_timer = 0
    coin_interval = random.randint(90, 170)

    while True:
        clock.tick(FPS)

        # Handles quit and restart events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    main()
                    return

                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        # Updates game objects only while the game is not over.
        if not game_over:
            keys = pygame.key.get_pressed()
            player.move(keys)
            road.update()

            # Spawns enemy cars at random time intervals.
            enemy_timer += 1
            if enemy_timer >= enemy_interval:
                enemies.append(EnemyCar(enemy_speed))
                enemy_timer = 0
                enemy_interval = random.randint(55, 110)

            # Spawns coins at random time intervals.
            coin_timer += 1
            if coin_timer >= coin_interval:
                coins.append(Coin(coin_speed))
                coin_timer = 0
                coin_interval = random.randint(90, 200)

            # Updates enemies and checks collision with player.
            for enemy in enemies[:]:
                enemy.update()

                if enemy.off_screen():
                    enemies.remove(enemy)
                    score += 1

                elif enemy.rect().colliderect(player.rect()):
                    if not crash_played:
                        crash_sound.play()
                        crash_played = True
                    game_over = True

            # Updates coins and checks if player collected them.
            for coin in coins[:]:
                coin.update()

                if coin.off_screen():
                    coins.remove(coin)

                elif coin.rect().colliderect(player.rect()):
                    coins.remove(coin)

                    coin_count += 1
                    score += coin.value

                    coin_sound.play()

                    # Every 5 collected coins increase difficulty.
                    if coin_count >= next_speedup:
                        enemy_speed += SPEEDUP_AMOUNT
                        coin_speed += SPEEDUP_AMOUNT
                        road.speed += SPEEDUP_AMOUNT
                        player.spd += 0.3
                        next_speedup += COINS_PER_SPEEDUP

        # Draws all game objects.
        road.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        for coin in coins:
            coin.draw(screen)

        player.draw(screen)

        draw_hud(screen, score, coin_count, next_speedup, enemy_speed)
        draw_coin_legend(screen)

        if game_over:
            draw_game_over(screen, score, coin_count)

        pygame.display.flip()


if __name__ == "__main__":
    main()