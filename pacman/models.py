from pygame import draw
from pygame.constants import *
from abc import ABCMeta, abstractmethod
import constants as cte
import random

class GameEntity(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, surface) -> None:
        pass

    @abstractmethod
    def calculate_rules(self) -> None:
        pass

    @abstractmethod
    def process_events(self, events) -> None:
        pass

class Background(GameEntity):
    def __init__(self, size, font, pacman, enemy) -> None:
        self.pacman = pacman
        self.enemy = enemy
        self.size = size
        self.font = font
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
        img_score = self.font.render(f'Score: {self.score}', True, cte.YELLOW)
        surface.blit(img_score, (score_x, 50))


    def draw(self, surface):
        for i, row in enumerate(self.matrix):
            self._draw_column(surface, i, row)
        self.draw_score(surface)

    def _draw_column(self, surface, row_number, row):
        for j, column in enumerate(row):
            rect_x = j * self.size
            rect_y = row_number * self.size
            color = cte.BLUE if column == 2 else cte.BLACK
            draw.rect(surface, color, (rect_x, rect_y, self.size, self.size), 0)
            if column == 1:
                draw.circle(surface, cte.YELLOW, (rect_x + self.size // 2, rect_y + self.size // 2), self.size // 10, 0)

    def calculate_rules(self):
        directions = self.get_directions(self.enemy.row, self.enemy.column)
        if len(directions) >= 3:
            self.enemy.corner(directions)
        
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

    def process_events(self, events):
        for e in events:
            if e.type == QUIT:
                exit()

    def get_directions(self, row, column):
        directions = []

        if self.matrix[int(row - 1)][int(column)] != 2:
            directions.append(cte.UP)
        if self.matrix[int(row + 1)][int(column)] != 2:
            directions.append(cte.DOWN)
        if self.matrix[int(row)][int(column - 1)] != 2:
            directions.append(cte.LEFT)
        if self.matrix[int(row)][int(column + 1)] != 2:
            directions.append(cte.RIGHT)
       
        return directions

class Pacman(GameEntity):
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
        draw.circle(surface, cte.YELLOW, (self.center_x, self.center_y), self.radius)

        # Drawing pacman mouth
        mouth_corner = (self.center_x, self.center_y)
        sup_lip = (self.center_x + self.radius, self.center_y - self.radius)
        inf_lip = (self.center_x + self.radius, self.center_y)
        points = [mouth_corner, sup_lip, inf_lip]

        draw.polygon(surface, cte.BLACK, points, 0)

        # Drawing pacman eye
        eye_x = int(self.center_x + self.radius / 3)
        eye_y = int(self.center_y - self.radius * 0.7)
        eye_radius = int(self.radius / 10)

        draw.circle(surface, cte.BLACK, (eye_x, eye_y), eye_radius, 0)

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

    def process_events(self, events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.vel_x = cte.SPEED
                if e.key == K_LEFT:
                    self.vel_x = -cte.SPEED
                if e.key == K_UP:
                    self.vel_y = -cte.SPEED
                if e.key == K_DOWN:
                    self.vel_y = cte.SPEED
            if e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.vel_x = 0
                if e.key == K_LEFT:
                    self.vel_x = 0
                if e.key == K_UP:
                    self.vel_y = 0
                if e.key == K_DOWN:
                    self.vel_y = 0

class Enemy(GameEntity):
    def __init__(self, color, size) -> None:
        self.column = 6
        self.row = 2
        self.color = color
        self.size = size
        self.vel = cte.SPEED
        self.direction = cte.DOWN

    def draw(self, surface):
        slice = self.size // 8
        body_x = int(self.column * self.size)
        body_y = int(self.row * self.size)
        vertices = [
            (body_x, body_y + slice * 8),
            (body_x + slice * 2, body_y + slice // 2),
            (body_x + slice * 3, body_y),
            (body_x + slice * 5, body_y),
            (body_x + slice * 6, body_y + slice // 2),
            (body_x + slice * 7, body_y + slice * 2),
            (body_x + slice * 8, body_y + slice * 8)
        ]
        draw.polygon(surface, self.color, vertices, 0)

        eye_external_radius = slice
        eye_internal_radius = slice // 2

        left_eye_x = int(body_x + slice * 2.5)
        left_eye_y = int(body_y + slice * 2.5)

        right_eye_x = int(body_x + slice * 5.5)
        right_eye_y = int(body_y + slice * 2.5)

        draw.circle(surface, cte.WHITE, (left_eye_x, left_eye_y), eye_external_radius, 0)
        draw.circle(surface, cte.BLACK, (left_eye_x, left_eye_y), eye_internal_radius, 0)
        draw.circle(surface, cte.WHITE, (right_eye_x, right_eye_y), eye_external_radius, 0)
        draw.circle(surface, cte.BLACK, (right_eye_x, right_eye_y), eye_internal_radius, 0)
        

    def calculate_rules(self):
        match self.direction:
            case cte.UP:
                self.row -= self.vel
            case cte.RIGHT: 
                self.column += self.vel
            case cte.DOWN:
                self.row += self.vel
            case cte.LEFT:
                self.column -= self.vel

    def process_events(self, events):
        pass

    def corner(self, directions):
        self.direction = random.choice(directions)