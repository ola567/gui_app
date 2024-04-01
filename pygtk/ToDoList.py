class ToDoList:
    def __init__(self):
        self.list = []

    def add(self, task: tuple):
        self.list.append({'task_title': task[0], 'task_description': task[1], 'task_finish_date': task[2], 'task_done': task[3]})

    def edit(self, task_index: int, new_task: tuple):
        self.list[task_index]['task_title'] = new_task[0]
        self.list[task_index]['task_description'] = new_task[1]
        self.list[task_index]['task_finish_date'] = new_task[2]

    def delete(self, task_number: int):
        self.list.pop(task_number)
