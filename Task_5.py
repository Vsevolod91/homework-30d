from Task_1_and_2 import *

class TodoList():

    def __init__(self):
        self.tasks = [None]*1
        self.start = 0
        self.stop = 0
        self.step = 1

    def __str__(self):
        return str(self.tasks)

    def __iter__(self):
        self.value = - 1
        return self

    def __next__(self):
        self.stop = len(self.tasks)
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.tasks[self.value]
        else:
            raise StopIteration

    def __setitem__(self, key, value):
        try:
            self.tasks[key] = value
        except IndexError:
            self.tasks.append(None)
            self.tasks[key] = value

    # def __getitem__(self, item):
    #     return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')
todo_list[2] = Task('Выйти на пробежку')

for item in todo_list:
    print(item)


