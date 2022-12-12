from Task_1_and_2 import *

class TodoList():

    def __init__(self):
        self.tasks = [None]*1

    def __str__(self):
        return str(self.tasks)

    def __setitem__(self, key, value):
        try:
            self.tasks[key] = value
        except IndexError:
            self.tasks.append(None)
            self.tasks[key] = value

    def __getitem__(self, item):
        return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')
print(todo_list)

print(todo_list[0])

del todo_list[0]
print(todo_list)

