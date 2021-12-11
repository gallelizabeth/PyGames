import pygame

from board import Board

FPS = 60


class Life(Board):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.speed = 300  # шагов в минуту
        self.step_time = 60 * 1000 / self.speed
        self.running = False
        self.time = pygame.time.get_ticks()  # в миллисекундах

    def render(self, surface: pygame.Surface):
        super().render(surface)

    def get_click(self, mouse_pos):
        if not self.running:
            super().get_click(mouse_pos)

    def pause(self):
        self.running = not self.running
        if self.running:
            self.time = pygame.time.get_ticks()  # в миллисекундах

    def next_move(self):
        new_board = []
        for i in range(self.height):
            new_row = []
            for j in range(self.width):
                neighbors = self.get_neighbors(i, j)
                if self.board[i][j] == 0 and neighbors == 3:
                    new_row.append(1)
                elif self.board[i][j] == 1 and 2 <= neighbors <= 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
            new_board.append(new_row)
        self.board = new_board
        self.time = pygame.time.get_ticks()  # в миллисекундах

    def get_neighbors(self, row, column):
        neighbors = 0
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if 0 <= i < self.height and 0 <= j < self.width:
                    neighbors += self.board[i][j]
        neighbors -= self.board[row][column]
        return neighbors

    def change_speed(self, difference):
        self.speed += difference
        if self.speed == 0:
            self.speed = 1
        self.step_time = 60 * 1000 / self.speed

    def next(self):
        if self.running:
            time = pygame.time.get_ticks()  # в миллисекундах
            if time - self.time > self.step_time:
                self.next_move()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    board = Life(25, 25)
    board.set_view(50, 50, 20)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    board.pause()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    board.get_click(event.pos)
                elif event.button == pygame.BUTTON_RIGHT:
                    board.pause()
            if event.type == pygame.MOUSEWHEEL:
                board.change_speed(event.y)
        screen.fill((0, 0, 0))
        board.next()
        board.render(screen)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
