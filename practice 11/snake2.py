import pygame
import random
import sys

# -----------------------------
# MAIN GAME SETTINGS
# -----------------------------
CELL = 20
COLS = 30
ROWS = 28
HUD_H = 55

SCREEN_W = COLS * CELL
SCREEN_H = ROWS * CELL + HUD_H

FPS = 10

# -----------------------------
# DIRECTIONS
# -----------------------------
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# -----------------------------
# COLOURS
# -----------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BG = (235, 246, 255)
GRID_LINE = (210, 230, 245)

HUD_BG = (22, 75, 120)
HUD_LINE = (255, 205, 80)

SNAKE_HEAD = (255, 170, 70)
SNAKE_BODY = (40, 155, 130)
SNAKE_EYE = (255, 255, 255)

RED = (230, 70, 70)
YELLOW = (255, 220, 70)
ORANGE = (255, 145, 60)
PURPLE = (160, 80, 210)
SILVER = (220, 230, 235)

# -----------------------------
# FOOD TYPES
# value = how many points the food gives
# weight = chance of appearing
# lifetime = how long it stays on screen
# -----------------------------
FOOD_TYPES = [
    {"label": "Apple", "value": 1, "colour": RED, "weight": 50, "lifetime": None},
    {"label": "Orange", "value": 2, "colour": ORANGE, "weight": 30, "lifetime": 50},
    {"label": "Grape", "value": 3, "colour": PURPLE, "weight": 15, "lifetime": 30},
    {"label": "Star", "value": 5, "colour": YELLOW, "weight": 5, "lifetime": 20},
]

MAX_FOOD_ON_SCREEN = 4


# Chooses food randomly according to its weight
def weighted_choice(items):
    total = sum(item["weight"] for item in items)
    number = random.randint(1, total)

    current = 0
    for item in items:
        current += item["weight"]
        if number <= current:
            return item

    return items[-1]


class Food:
    # Creates one food item in a random free position
    def __init__(self, occupied_cells):
        food_type = weighted_choice(FOOD_TYPES)

        self.label = food_type["label"]
        self.value = food_type["value"]
        self.colour = food_type["colour"]
        self.lifetime = food_type["lifetime"]
        self.age = 0

        all_cells = {(c, r) for c in range(COLS) for r in range(ROWS)}
        free_cells = list(all_cells - occupied_cells)

        if free_cells:
            self.pos = random.choice(free_cells)
        else:
            self.pos = (COLS // 2, ROWS // 2)

    # Updates timer for food that can disappear
    def update(self):
        if self.lifetime is not None:
            self.age += 1
            return self.age >= self.lifetime
        return False

    # Calculates remaining lifetime
    def time_fraction(self):
        if self.lifetime is None:
            return None
        return max(0.0, 1.0 - self.age / self.lifetime)

    # Draws food on the game field
    def draw(self, surface):
        col, row = self.pos

        px = col * CELL + CELL // 2
        py = row * CELL + CELL // 2 + HUD_H

        fraction = self.time_fraction()

        if fraction is not None:
            radius = int((CELL // 2 - 2) * (0.7 + 0.3 * fraction))
            pygame.draw.circle(surface, self.colour, (px, py), radius)
            pygame.draw.circle(surface, WHITE, (px, py), CELL // 2 - 1, 2)
        else:
            pygame.draw.circle(surface, self.colour, (px, py), CELL // 2 - 2)

        font_s = pygame.font.SysFont("arial", 11, bold=True)
        text_colour = BLACK if self.colour == YELLOW else WHITE
        txt = font_s.render(str(self.value), True, text_colour)
        surface.blit(txt, txt.get_rect(center=(px, py)))


class Snake:
    # Creates the snake in the centre of the field
    def __init__(self):
        mid_col = COLS // 2
        mid_row = ROWS // 2

        self.body = [
            (mid_col, mid_row),
            (mid_col - 1, mid_row),
            (mid_col - 2, mid_row)
        ]

        self.direction = RIGHT
        self.grew = False

    # Changes direction but does not allow instant reverse
    def change_direction(self, new_dir):
        opposite = (-self.direction[0], -self.direction[1])

        if new_dir != opposite:
            self.direction = new_dir

    # Moves snake one cell forward
    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        self.body.insert(0, new_head)

        if not self.grew:
            self.body.pop()
        else:
            self.grew = False

    def head(self):
        return self.body[0]

    # Checks if snake hits wall or itself
    def is_dead(self):
        hx, hy = self.head()

        if hx < 0 or hx >= COLS:
            return True

        if hy < 0 or hy >= ROWS:
            return True

        if self.head() in self.body[1:]:
            return True

        return False

    def occupied_cells(self):
        return set(self.body)

    # Draws snake with rounded parts and eyes
    def draw(self, surface):
        for index, (col, row) in enumerate(self.body):
            px = col * CELL
            py = row * CELL + HUD_H

            colour = SNAKE_HEAD if index == 0 else SNAKE_BODY

            pygame.draw.rect(
                surface,
                colour,
                (px + 2, py + 2, CELL - 4, CELL - 4),
                border_radius=7
            )

        hx, hy = self.body[0]
        cx = hx * CELL + CELL // 2
        cy = hy * CELL + CELL // 2 + HUD_H

        dx, dy = self.direction
        perp = (-dy, dx)

        for side in (+1, -1):
            ex = cx + dx * 4 + perp[0] * side * 4
            ey = cy + dy * 4 + perp[1] * side * 4

            pygame.draw.circle(surface, SNAKE_EYE, (ex, ey), 3)
            pygame.draw.circle(surface, BLACK, (ex + dx, ey + dy), 1)


class SnakeGame:
    # Main class that controls the whole game
    FOOD_SPAWN_INTERVAL = 25

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 22, bold=True)
        self.big_font = pygame.font.SysFont("arial", 48, bold=True)
        self.small_font = pygame.font.SysFont("arial", 13)

        self.reset()

    # Starts a new game
    def reset(self):
        self.snake = Snake()
        self.foods = []
        self.score = 0
        self.frame = 0
        self.game_over = False
        self.running = True

        self.try_spawn_food()

    # Main game loop
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()

            if not self.game_over:
                self.update()

            self.draw()

        pygame.quit()
        sys.exit()

    # Handles keyboard actions
    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.snake.change_direction(UP)

                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.snake.change_direction(DOWN)

                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.snake.change_direction(LEFT)

                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.snake.change_direction(RIGHT)

                elif event.key == pygame.K_r and self.game_over:
                    self.reset()

                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    # Updates snake, food, score and collisions
    def update(self):
        self.frame += 1
        self.snake.move()

        if self.snake.is_dead():
            self.game_over = True
            return

        head = self.snake.head()

        for food in self.foods[:]:
            if food.pos == head:
                self.score += food.value
                self.snake.grew = True
                self.foods.remove(food)

        for food in self.foods[:]:
            if food.update():
                self.foods.remove(food)

        if self.frame % self.FOOD_SPAWN_INTERVAL == 0:
            self.try_spawn_food()

    # Adds new food if there is space
    def try_spawn_food(self):
        if len(self.foods) < MAX_FOOD_ON_SCREEN:
            occupied = self.snake.occupied_cells() | {food.pos for food in self.foods}
            self.foods.append(Food(occupied))

    # Draws all game elements
    def draw(self):
        self.screen.fill(BG)

        self.draw_grid()

        for food in self.foods:
            food.draw(self.screen)

        self.snake.draw(self.screen)

        self.draw_hud()
        self.draw_legend()

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    # Draws a soft grid
    def draw_grid(self):
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.rect(
                    self.screen,
                    GRID_LINE,
                    (c * CELL, r * CELL + HUD_H, CELL, CELL),
                    1
                )

    # Draws top panel with score and controls
    def draw_hud(self):
        pygame.draw.rect(self.screen, HUD_BG, (0, 0, SCREEN_W, HUD_H))
        pygame.draw.line(self.screen, HUD_LINE, (0, HUD_H), (SCREEN_W, HUD_H), 3)

        score_txt = self.font.render(f"Score: {self.score}", True, YELLOW)
        length_txt = self.font.render(f"Length: {len(self.snake.body)}", True, WHITE)
        ctrl_txt = self.small_font.render("Move: Arrows / WASD   |   Restart: R   |   Quit: ESC", True, SILVER)

        self.screen.blit(score_txt, (12, 10))
        self.screen.blit(length_txt, (190, 10))
        self.screen.blit(ctrl_txt, (12, 36))

    # Draws small food legend on the right side of top panel
    def draw_legend(self):
        x = SCREEN_W - 220
        y = 6

        pygame.draw.rect(self.screen, (16, 58, 95), (x - 8, 4, 215, 44), border_radius=8)

        for i, food_type in enumerate(FOOD_TYPES):
            lx = x + (i % 2) * 105
            ly = y + (i // 2) * 20

            pygame.draw.circle(self.screen, food_type["colour"], (lx + 7, ly + 7), 7)

            label = f"{food_type['label']} +{food_type['value']}"
            txt = self.small_font.render(label, True, WHITE)

            self.screen.blit(txt, (lx + 18, ly))

    # Draws game over screen
    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        overlay.fill((20, 30, 40, 165))
        self.screen.blit(overlay, (0, 0))

        title = self.big_font.render("GAME OVER", True, RED)
        score = self.font.render(f"Score: {self.score} | Length: {len(self.snake.body)}", True, YELLOW)
        restart = self.font.render("Press R to restart or ESC to quit", True, WHITE)

        center_x = SCREEN_W // 2
        center_y = SCREEN_H // 2

        self.screen.blit(title, title.get_rect(center=(center_x, center_y - 50)))
        self.screen.blit(score, score.get_rect(center=(center_x, center_y + 10)))
        self.screen.blit(restart, restart.get_rect(center=(center_x, center_y + 50)))


# Program starts here
if __name__ == "__main__":
    game = SnakeGame()
    game.run()