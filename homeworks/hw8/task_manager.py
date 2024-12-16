import tkinter as tk
from datetime import datetime as dt

bg_color,bg_box,fg_color,bg_input,fg_input,bg_mark="SkyBlue3","LightBlue1","cyan", "light blue","DarkRed","Magenta"

def add_task():
    task = task_entry.get() # здесь мы получаем слова из поля для ввода
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    task_index = task_list.curselection()
    if task_index:
        task_list.delete(task_index)

def mark_task():
    task_index = task_list.curselection()
    if task_index:
        selected_task = task_list.get(task_index)
        now = dt.now().strftime('%d.%m.%y')

        ready_list.insert(tk.END, f" {selected_task}  ({now})")
        task_list.delete(task_index)

# =============================== LAYOUT =============================================
root = tk.Tk()
root.configure( background=bg_color)
root.title('Task list')
#-------------------------------- INPUT ----------------------------------------------
text1= tk.Label(root,text="Введите вашу задачу:", bg=bg_color)
text1.pack(pady=5)
task_entry= tk.Entry(root, width=30, bg=bg_input,fg=fg_input)
task_entry.pack(pady=10)

# -------------------------------  BUTTONS ---------------------------------------------
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=16)

add_task_button = tk.Button(button_frame, text="Добавить задачу",command=add_task,bg=bg_box)
add_task_button.pack(side=tk.LEFT,padx=10)

delete_button = tk.Button(button_frame, text="Удалить задачу",command=delete_task,bg=bg_box)
delete_button.pack(side=tk.LEFT,padx=8)

mark_button = tk.Button(button_frame, text="Задача выполнена", bg=bg_box, command=mark_task)
mark_button.pack(side=tk.LEFT, padx=8)

# ------------------------------ LISTS ----------------------------------------------------
list_frame = tk.Frame(root, bg=bg_color)
list_frame.pack()
task_frame = tk.Frame(list_frame, bg=bg_color)
task_frame.pack(side=tk.LEFT)
ready_frame = tk.Frame(list_frame, bg=bg_color)
ready_frame.pack(side=tk.LEFT, padx=16)

task_text = tk.Label(task_frame, text="Список задач:", bg=bg_color)
task_text.pack(pady=5)
task_list = tk.Listbox(task_frame, height=10, width=50, bg=bg_box,selectbackground=bg_mark)
task_list.pack(pady=10)

ready_text = tk.Label(ready_frame, text="Выполнено:", bg=bg_color)
ready_text.pack(pady=5)
ready_list = tk.Listbox(ready_frame, height=10, width=50, bg=bg_box,selectbackground=bg_mark)
ready_list.pack(pady=10)

# ------------------------------- RUN ------------------------------------------------------
root.mainloop()