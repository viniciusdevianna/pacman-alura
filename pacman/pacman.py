import pygame

# Const parameters
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SPEED = 1
RADIUS = 30
SIZE = 600 // 30

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
font = pygame.font.SysFont('arial', 24, True, False)

class Background:
    def __init__(self, size, pacman) -> None:
        self.pacman = pacman
        self.size = size
        self.score = 0
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def draw_score(self, surface):
        score_x = 30 * self.size
        img_score = font.render(f'Score: {self.score}', True, YELLOW)
        surface.blit(img_score, (score_x, 50))


    def draw(self, surface):
        for i, row in enumerate(self.matrix):
            self._draw_column(surface, i, row)
        self.draw_score(surface)

    def _draw_column(self, surface, row_number, row):
        for j, column in enumerate(row):
            rect_x = j * self.size
            rect_y = row_number * self.size
            color = BLUE if column == 2 else BLACK
            pygame.draw.rect(surface, color, (rect_x, rect_y, self.size, self.size), 0)
            if column == 1:
                pygame.draw.circle(screen, YELLOW, (rect_x + self.size // 2, rect_y + self.size // 2), self.size // 10, 0)

    def calculate_rules(self):
        column = self.pacman.column_intent
        row = self.pacman.row_intent
        if 0 <= column < 28 and 0 <= row < 29:
            if self.matrix[row][column] != 2:
                self.pacman.movement_allowed()
                if self.matrix[row][column] == 1:
                    self.score += 1
                    self.matrix[row][column] = 0
            else:
                self.pacman.movement_hindered()
        else:
            self.pacman.movement_hindered()


class Pacman:
    def __init__(self, size) -> None:
        self.column = 1
        self.row = 1
        self.center_x = 400
        self.center_y = 300
        self.size = size
        self.radius = self.size // 2
        self.vel_x = 0
        self.vel_y = 0
        self.column_intent = self.column
        self.row_intent = self.row

    def draw(self, surface):
        # Drawing pacman body
        pygame.draw.circle(surface, YELLOW, (self.center_x, self.center_y), self.radius)

        # Drawing pacman mouth
        mouth_corner = (self.center_x, self.center_y)
        sup_lip = (self.center_x + self.radius, self.center_y - self.radius)
        inf_lip = (self.center_x + self.radius, self.center_y)
        points = [mouth_corner, sup_lip, inf_lip]

        pygame.draw.polygon(surface, BLACK, points, 0)

        # Drawing pacman eye
        eye_x = int(self.center_x + self.radius / 3)
        eye_y = int(self.center_y - self.radius * 0.7)
        eye_radius = int(self.radius / 10)

        pygame.draw.circle(surface, BLACK, (eye_x, eye_y), eye_radius, 0)

    def calculate_rules(self):
        self.column_intent += self.vel_x
        self.row_intent += self.vel_y
        self.center_x = int(self.column * self.size + self.radius)
        self.center_y = int(self.row * self.size + self.radius)

    def movement_allowed(self):
        self.column = self.column_intent
        self.row = self.row_intent

    def movement_hindered(self):
        self.column_intent -= self.vel_x
        self.row_intent -= self.vel_y

    def event_processing(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = SPEED
                if e.key == pygame.K_LEFT:
                    self.vel_x = -SPEED
                if e.key == pygame.K_UP:
                    self.vel_y = -SPEED
                if e.key == pygame.K_DOWN:
                    self.vel_y = SPEED
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                if e.key == pygame.K_LEFT:
                    self.vel_x = 0
                if e.key == pygame.K_UP:
                    self.vel_y = 0
                if e.key == pygame.K_DOWN:
                    self.vel_y = 0


if __name__ == '__main__':
    pacman = Pacman(SIZE)
    background = Background(SIZE, pacman)

    # Game loop
    while True:
        # Rules
        pacman.calculate_rules()
        background.calculate_rules()
        
        # Draw
        screen.fill(BLACK)
        background.draw(screen)
        pacman.draw(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
        pacman.event_processing(events)