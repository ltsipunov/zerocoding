import re
from datetime import date,datetime as dt, timedelta as td

class Task:
    def __init__(self):
        self.tasks = []  # Список задач, каждая задача - это словарь

    def add_task(self, description, deadline=None):
        if not deadline:
            deadline= dt.now().strftime(  '%d.%m %H:%M')
        try:
            deadline= dt.strptime('25.'+deadline, '%y.%d.%m %H:%M' )
        except ValueError as e:
            print(f"Ошибка! {e} (время должно быть в формате dd.mm hh.mm или пустым)")
            # deadline=dt(deadline)
        task = {
            'description': description,
            'deadline': deadline,
            'is_completed': False
        }
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['is_completed'] = True
        else:
            print("Некорректный индекс задачи.")

    def mark_tasks_completed(self, pattern):
        regex = re.compile(pattern)
        for idx,task in enumerate( self.tasks ):
            if regex.search(task['description']):
                print(f"выполнено: {task['description']}" )
                self.mark_task_completed(idx)

    def get_all_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        return [task for task in self.tasks if task['is_completed']]

    def get_current_tasks(self):
        return [task for task in self.tasks if not task['is_completed']]

    def show_tasks(self):
        if not self.tasks:
            print("Нет задач для отображения.")
            return
        for idx, task in enumerate(self.tasks):
            status = "Выполнено" if task['is_completed'] else "Не выполнено"
            print(f"{idx}. {task['description']} (Срок выполнения: {task['deadline']}, Статус: {status})")