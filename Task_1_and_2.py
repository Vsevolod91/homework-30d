import datetime as dt

class Task():

    def __init__(self, content):
        self.verify_content(content)
        self.content = content
        self.date = dt.datetime.now().strftime("%y-%m-%d %H:%M:%S")

    def __repr__(self):
        return str(f"{self.content} (создано {self.date})")

    def __str__(self):
        return str(f"{self.content} (создано {self.date})")

    def __hash__(self):
        return hash(self.content)

    def __eq__(self, other):
        return self.content == self.verify_content(other)

    def __len__(self):
        return len(self.content)

    @classmethod
    def verify_content(self, content):
        if isinstance(content, (str, Task)):
            return content
        else:
            raise TypeError("Введите строку")

if __name__ == "__main__":
    todo_set = set()

    todo_set.add(Task('Сделать домашку'))
    todo_set.add(Task('Выпить кофе'))
    todo_set.add(Task('Выйти на пробежку'))
    todo_set.add(Task('Сделать домашку'))

    for item in todo_set:
        print(item)

    t1 = Task('Сделать домашку')
    print(t1)

    todo_list = []
    todo_list.append(Task('Сделать домашку'))
    todo_list.append(Task(''))
    todo_list.append(Task('Выйти на пробежку'))
    todo_list.append(Task(''))
    todo_list.append(Task(''))

    non_empty_tasks = [item for item in todo_list if item]
    print(non_empty_tasks)

    print(len([item for item in todo_list if not item]))
