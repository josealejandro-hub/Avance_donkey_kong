import pygame

pygame.init()

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong – Avance Visual")
clock = pygame.time.Clock()

# ---------------- COLORES ----------------
BLACK = (0, 0, 0)
PINK = (225, 51, 129)
BROWN = (139, 69, 19)
BLUE = (100, 200, 255)

# ---------------- DONKEY KONG ----------------
dk_img = pygame.image.load(
    r"C:\Users\Estudiante\Downloads\donkey_kong.png.png"
).convert_alpha()
dk_img = pygame.transform.scale(dk_img, (130, 130))
dk_x, dk_y = 30, 20

# ---------------- RIELES ----------------
rails = [
    (100, 150, 20, 4),
    (80, 240, 20, -4),
    (100, 330, 20, 4),
    (80, 420, 20, -4),
    (100, 510, 20, 4),
]

SECTION_W = 30

def draw_bridge(start_x, start_y, sections, slope):
    for i in range(sections):
        x = start_x + i * SECTION_W
        y = start_y - i * slope

        pygame.draw.line(screen, PINK, (x, y), (x+30, y), 6)
        pygame.draw.line(screen, PINK, (x, y+12), (x+30, y+12), 6)
        pygame.draw.line(screen, PINK, (x, y+12), (x+15, y), 6)
        pygame.draw.line(screen, PINK, (x+15, y), (x+30, y+12), 6)

# ---------------- ESCALERAS ----------------
ladders = [
    pygame.Rect(250, 170, 20, 70),
    pygame.Rect(500, 260, 20, 70),
    pygame.Rect(350, 350, 20, 70),
    pygame.Rect(600, 440, 20, 70),
]

def draw_ladders():
    for ladder in ladders:
        pygame.draw.rect(screen, BLUE, ladder)
        for i in range(ladder.top, ladder.bottom, 15):
            pygame.draw.line(screen, BLACK, (ladder.left, i), (ladder.right, i), 2)

# ---------------- BARRIL ----------------
class Barrel:
    def __init__(self):
        self.radius = 10
        self.speed = 2
        self.current_rail = 0
        self.direction = 1
        self.x = 0
        self.y = 0
        self.set_on_rail()

    def set_on_rail(self):
        start_x, start_y, sections, slope = rails[self.current_rail]
        self.x = start_x if self.direction == 1 else start_x + sections * SECTION_W
        self.update_y()

    def update_y(self):
        start_x, start_y, sections, slope = rails[self.current_rail]
        progress = (self.x - start_x) / SECTION_W
        self.y = start_y - (progress * slope)

    def update(self):
        start_x, start_y, sections, slope = rails[self.current_rail]
        end_x = start_x + sections * SECTION_W

        self.x += self.speed * self.direction
        self.update_y()

        if self.direction == 1 and self.x >= end_x:
            self.next_rail()
        elif self.direction == -1 and self.x <= start_x:
            self.next_rail()

    def next_rail(self):
        self.current_rail += 1
        self.direction *= -1

        if self.current_rail >= len(rails):
            self.current_rail = 0
            self.direction = 1

        self.set_on_rail()

    def draw(self):
        pygame.draw.circle(
            screen, BROWN,
            (int(self.x), int(self.y)), self.radius
        )
        pygame.draw.line(
            screen, BLACK,
            (self.x - self.radius, self.y),
            (self.x + self.radius, self.y), 2
        )

barrel = Barrel()

# ---------------- LOOP ----------------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    barrel.update()

    screen.fill(BLACK)

    screen.blit(dk_img, (dk_x, dk_y))

    for r in rails:
        draw_bridge(*r)

    draw_ladders()
    barrel.draw()

    pygame.display.flip()

pygame.quit()
