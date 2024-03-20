class ToDoList:
    def __init__(self):
        self.list = []

    def add(self, task: tuple):
        self.list.append({'task_title': task[0], 'task_description': task[1], 'task_finish_date': task[2], 'task_done': task[3]})

    def edit(self, task: dict):
        pass

    def delete(self, task_number: int):
        self.list.pop(task_number)
