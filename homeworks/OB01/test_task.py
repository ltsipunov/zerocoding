from task import Task
task_list = Task()
task_list.add_task("Сделать уборку")
task_list.add_task("Купить молоко",'10.01 00:00')
task_list.add_task("Починить кран")
task_list.add_task("Сделать урок")
task_list.show_tasks()
task_list.mark_tasks_completed("уборк|кран")
task_list.show_tasks()

print( '=========== выполненные задачи: ===============' )
print( task_list.get_completed_tasks() )
print( '=========== задачи в очереди: ===============' )
print( task_list.get_current_tasks() )
