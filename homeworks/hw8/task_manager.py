import tkinter as tk
bg_color,bg_box,fg_color,bg_input,fg_input,bg_mark="SkyBlue3","LightBlue1","cyan", "light blue","DarkRed","Magenta4sspo"

def add_task():
    task = task_entry.get() # здесь мы получаем слова из поля для ввода
    if task:
        task_listBox.insert(tk.END, task) # с помощью END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END) # здесь очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listBox.curselection() #  передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listBox.delete(selected_task) # удаляем выбранный элемент из списка

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, highlightbackground=bg_mark)

root = tk.Tk()
root.configure( background=bg_color)
root.title('Task list')
text1= tk.Label(root,text="Введите вашу задачу:", bg=bg_color)
text1.pack(pady=5)
task_entry= tk.Entry(root, width=30, bg=bg_input,fg=fg_input)
task_entry.pack(pady=10)
add_task_button = tk.Button(root, text="Добавить задачу",command=add_task,bg=bg_box)
add_task_button.pack(pady=5)
delete_button = tk.Button(root, text="Удалить задачу",command=delete_task,bg=bg_box)
delete_button.pack(pady=5)
text2 = tk.Label(root, text="Список задач:", bg=bg_color)
text2.pack(pady=5)
task_listBox = tk.Listbox(root, height=10, width=50, bg=bg_box,selectbackground=bg_mark)
task_listBox.pack(pady=10)

root.mainloop()