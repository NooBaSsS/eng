import time
import keyboard


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = '█'  # символ для клетки


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {(x, y): Cell(x, y) for x in range(width) for y in range(height)}
        self.last_update_time = time.time()

    def get_cell(self, x, y):
        return self.cells.get((x, y))

    def handle_keys(self, event):
        # Обработка нажатых клавиш
        pass

    def update(self):
        # Обновление состояния игры
        pass

    def render(self):
        # Отрисовка игры
        output = ''
        for y in range(self.height):
            for x in range(self.width):
                cell = self.get_cell(x, y)
                output += cell.char
            output += '\n'
        print('\033[H', end='')  # Перемещаем курсор в начало экрана
        print(output, end='')

    def run(self):
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
