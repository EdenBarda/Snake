import random
from tkinter import *

the_game_snake = Tk()


class Snake:
    def __init__(self, the_game):
        self.game = the_game
        self.composition = [(0, 0), (0, 1), (0, 2)]
        self.food = self.random_food()

    def __len__(self):
        return len(self.composition)

    def is_eat(self):
        if self.head() == self.food.get_composition():
            return True
        return False

    def is_dead(self):
        if not (23 >= self.head()[0] >= 0 and 23 >= self.head()[1] >= 0):
            return True
        for i in self.composition[0: -1]:
            if i == self.head():
                return True
        return False

    def is_win(self):
        if (not self.is_dead()) and len(self) == 576:
            print("you won!")
            the_game_snake.quit()
            return
        else:
            return False

    def move_right(self):
        self.composition.append((self.head()[0], self.head()[1] + 1))
        if self.is_dead():
            print("Oh dear! You are dead")
            the_game_snake.quit()
            return
        if not self.is_eat():
            delete_tale = Label(bg='black', width=2)
            delete_tale.grid(row=self.composition[0][0], column=self.composition[0][1])
            self.composition.pop(0)
        else:
            self.food = self.random_food()
        self.one_step()

    def move_left(self):
        if self.head()[1] - 1 < 0:
            print("Oh dear! You are dead")
            the_game_snake.quit()
            return
        self.composition.append((self.head()[0], self.head()[1] - 1))
        if self.is_dead():
            print("Oh dear! You are dead")
            the_game_snake.quit()
        if not self.is_eat():
            delete_tale = Label(bg='black', width=2)
            delete_tale.grid(row=self.composition[0][0], column=self.composition[0][1])
            self.composition.pop(0)
        else:
            self.food = self.random_food()
        self.one_step()

    def move_up(self):
        if self.head()[0] - 1 < 0:
            print("Oh dear! You are dead")
            the_game_snake.quit()
            return
        self.composition.append((self.head()[0] - 1, self.head()[1]))
        if self.is_dead():
            print("Oh dear! You are dead")
            the_game_snake.quit()
        if not self.is_eat():
            delete_tale = Label(bg='black', width=2)
            delete_tale.grid(row=self.composition[0][0], column=self.composition[0][1])
            self.composition.pop(0)
        else:
            self.food = self.random_food()
        self.one_step()

    def move_down(self):
        self.composition.append((self.head()[0] + 1, self.head()[1]))
        if self.is_dead():
            print("Oh dear! You are dead")
            the_game_snake.quit()
            return
        if not self.is_eat():
            delete_tale = Label(bg='black', width=2)
            delete_tale.grid(row=self.composition[0][0], column=self.composition[0][1])
            self.composition.pop(0)
        else:
            self.food = self.random_food()
        self.one_step()

    def one_step(self):
        for i in self.composition:
            draw_snake = Label(bg='blue4', width=2)
            draw_snake.grid(row=i[0], column=i[1])
        head_snake = Label(bg='red4', width=2)
        head_snake.grid(row=self.head()[0], column=self.head()[1])
        self.food.draw()

    def head(self):
        return self.composition[len(self) - 1]

    def random_food(self):
        i = random.randint(0, 23)
        j = random.randint(0, 23)
        food = Food((i, j))
        for k in self.composition:
            if k == food.get_composition():
                return self.random_food()
        return food


class Food:
    def __init__(self, composition):
        self._composition = composition

    def get_composition(self):
        return self._composition

    def draw(self):
        draw_food = Label(bg='red', width=2)
        draw_food.grid(row=self._composition[0], column=self._composition[1])


class PlayGame:
    def __init__(self):
        self.snake = Snake(self)

    def play(self):
        self.draw_board()
        up = Button(text="Up", bg="white", width=5, command=self.snake.move_up)
        up.grid(row=25, column=2, columnspan=3)
        down = Button(text="Down", bg="white", width=5, command=self.snake.move_down)
        down.grid(row=25, column=7, columnspan=3)
        right = Button(text="Right", bg="white", width=5, command=self.snake.move_right)
        right.grid(row=25, column=12, columnspan=3)
        left = Button(text="Left", bg="white", width=5, command=self.snake.move_left)
        left.grid(row=25, column=17, columnspan=3)

        self.snake.food.draw()
        self.snake.one_step()

    @staticmethod
    def draw_board():
        for i in range(24):
            for j in range(24):
                board = Label(bg='black', width=2)
                board.grid(row=i, column=j)


game = PlayGame()
game.play()
the_game_snake.mainloop()
