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

class Movable(metaclass=ABCMeta):
    @abstractmethod
    def movement_allowed(self):
        pass

    @abstractmethod
    def movement_hindered(self):
        pass

    @abstractmethod
    def turn_around_corner(self):
        pass

class Background(GameEntity):
    def __init__(self, size, font, pacman) -> None:
        self.state = cte.PLAYING
        self.pacman = pacman
        self.movables = [pacman,]
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

    def add_movable(self, movable):
        self.movables.append(movable)

    def draw(self, surface):
        match self.state:
            case cte.PLAYING:
                self._draw_playing(surface)
            case cte.PAUSED:
                self._draw_playing(surface)
                self._draw_paused(surface)
            case cte.GAME_OVER:
                self._draw_playing(surface)
                self._draw_game_over(surface)
            case _:
                pass

    def _draw_column(self, surface, row_number, row):
        for j, column in enumerate(row):
            rect_x = j * self.size
            rect_y = row_number * self.size
            color = cte.BLUE if column == 2 else cte.BLACK
            draw.rect(surface, color, (rect_x, rect_y, self.size, self.size), 0)
            if column == 1:
                draw.circle(surface, cte.YELLOW, (rect_x + self.size // 2, rect_y + self.size // 2), self.size // 10, 0)

    def _draw_score(self, surface):
        score_x = 30 * self.size
        img_score = self.font.render(f'Score: {self.score}', True, cte.YELLOW)
        surface.blit(img_score, (score_x, 50))

    def _draw_playing(self, surface):
        for i, row in enumerate(self.matrix):
            self._draw_column(surface, i, row)
        self._draw_score(surface)

    def _draw_text_center(self, surface, text):
        text_img = self.font.render(text, True, cte.YELLOW)
        text_x = (surface.get_width() - text_img.get_width()) // 2
        text_y = (surface.get_height() - text_img.get_height()) // 2

        surface.blit(text_img, (text_x, text_y))

    def _draw_paused(self, surface):
        self._draw_text_center(surface, cte.TEXT_PAUSED)

    def _draw_game_over(self, surface):
        self._draw_text_center(surface, cte.TEXT_GAME_OVER)

    def calculate_rules(self):
        match self.state:
            case cte.PLAYING:
                self._calculate_rules_playing()
            case cte.PAUSED:
                self._calculate_rules_paused()
            case _:
                pass         

    def _calculate_rules_playing(self):
        for movable in self.movables:
            row_intent = int(movable.row_intent)
            col_intent = int(movable.column_intent)
            row = int(movable.row)
            col = int(movable.column)
            directions = self._get_directions(row, col)

            if self._pacman_collided_with_enemy(movable):
                self.state = cte.GAME_OVER
                self.pacman.state = cte.GAME_OVER
                movable.state = cte.GAME_OVER

            if len(directions) >= 3:
                movable.turn_around_corner(directions)

            if self._is_free_space(row_intent, col_intent):
                movable.movement_allowed()
                if isinstance(movable, Pacman) and self.matrix[row][col] == 1:
                    self.score += 1
                    self.matrix[row][col] = 0
            else:
                movable.movement_hindered(directions)

    def _calculate_rules_paused(self):
        pass

    def process_events(self, events):
        for e in events:
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN:
                if e.key == K_p:
                    if self.state == 0:
                        self.state = 1
                    else:
                        self.state = 0

    def _get_directions(self, row, column):
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
    
    def _is_free_space(self, row, column):
        return 0 <= column < 28 and 0 <= row < 29 and self.matrix[row][column] != 2
    
    def _pacman_collided_with_enemy(self, movable):
        return isinstance(movable, Enemy) and movable.row == self.pacman.row and movable.column == self.pacman.column

class Pacman(GameEntity, Movable):
    def __init__(self, size) -> None:
        self.state = cte.PLAYING
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

    def calculate_rules(self) -> None:
        match self.state:
            case cte.PLAYING:
                self._calculate_rules_playing()
            case cte.PAUSED:
                self._calculate_rules_paused()
            case _:
                pass

    def _calculate_rules_playing(self):
        self.column_intent += self.vel_x
        self.row_intent += self.vel_y
        self.center_x = int(self.column * self.size + self.radius)
        self.center_y = int(self.row * self.size + self.radius)
    
    def _calculate_rules_paused(self):
        pass

    def movement_allowed(self):
        self.column = self.column_intent
        self.row = self.row_intent

    def movement_hindered(self, directions):
        self.column_intent -= self.vel_x
        self.row_intent -= self.vel_y

    def turn_around_corner(self, directions):
        return super().turn_around_corner()

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

class Enemy(GameEntity, Movable):
    def __init__(self, color, size) -> None:
        self.state = cte.PLAYING
        self.column = 6
        self.row = 2
        self.color = color
        self.size = size
        self.vel = cte.SPEED
        self.direction = cte.DOWN
        self.column_intent = self.column
        self.row_intent = self.row

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
        
    def calculate_rules(self) -> None:
        match self.state:
            case cte.PLAYING:
                self._calculate_rules_playing()
            case cte.PAUSED:
                self._calculate_rules_paused()
            case _:
                pass

    def _calculate_rules_playing(self):
        match self.direction:
            case cte.UP:
                self.row_intent -= self.vel
            case cte.RIGHT: 
                self.column_intent += self.vel
            case cte.DOWN:
                self.row_intent += self.vel
            case cte.LEFT:
                self.column_intent -= self.vel
            case _:
                raise ValueError('Unsupported direction value')
            
    def _calculate_rules_paused(self):
        pass

    def process_events(self, events):
        pass

    def change_directions(self, directions):
        self.direction = random.choice(directions)

    def turn_around_corner(self, directions):
        self.change_directions(directions)

    def movement_allowed(self):
        self.column = self.column_intent
        self.row = self.row_intent

    def movement_hindered(self, directions):
        self.column_intent = self.column
        self.row_intent = self.row
        self.change_directions(directions)