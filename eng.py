import time
import keyboard
import os


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = '█'  # символ для клетки

    def __str__(self):
        return self.image


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {(x, y): Cell(x, y) for x in range(1, width + 1) for y in range(1, height + 1)}
        self.last_update_time = time.time()

    def get_cell(self, x, y):
        return self.cells[(x, y)]

    def handle_keys(self, event):
        # Обработка нажатых клавиш
        pass

    def update(self):
        # Обновление состояния игры
        pass

    def render(self):
        # Отрисовка игры
        output = ''
        for y in range(1, self.height + 1):
            for x in range(1, self.width + 1):
                cell = self.get_cell(x, y)
                output += cell.image
            output += '\n'
        print('\033[H', end='')  # Перемещаем курсор в начало экрана
        print(output, end='')

    def run(self):
        os.system('cls')
        while True:
            if keyboard.is_pressed('q'):
                break

            self.handle_keys(keyboard.read_event())

            current_time = time.time()
            delta_time = current_time - self.last_update_time

            if delta_time >= 0.1:  # Ограничение на частоту обновления экрана
                self.update()
                self.render()
                self.last_update_time = current_time


if __name__ == "__main__":
    field = Field(10, 10)
    field.run()
