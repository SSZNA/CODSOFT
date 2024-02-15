from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("500x500")
main.title("TO-DO-LIST")
main.config(bg="indigo")
main.minsize(400, 400)
main.maxsize(600, 500)

label = Label(text='''WELCOME TO YOUR TO-DO-LIST ORGANIZER''', bg="#FFFDD0", fg="black", padx=10, pady=10,
              font="comicsansms 13 bold", borderwidth=5, relief=RIDGE)
label.pack()

entry = Entry(main, font=("Helvetica", 13), bg="#FFFDD0")
entry.pack(pady=20)

frame = Frame(main, bg="#FFFDD0")
frame.pack(side=RIGHT)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
task_listbox = Listbox(frame, width=30, height=14, font=('Helvetica', 14), borderwidth=5, relief=RIDGE, fg="black",
                       selectbackground="grey", yscrollcommand=scrollbar.set)
task_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=task_listbox.yview)

tasks = []


def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Kindly enter a task")
    else:
        task_listbox.insert(END, task)
        tasks.append(task)
        write_tasks_in_file()
        entry.delete(0, END)


add_task_button = Button(text="Add task", bg="light pink", fg="black", command=add_task)
add_task_button.pack(pady=30)


def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        task_listbox.delete(selected_index)
        write_tasks_in_file()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")


delete_task_button = Button(text="Delete task", bg="light green", fg="black", command=delete_task)
delete_task_button.pack(pady=10)


def write_tasks_in_file():
    with open("list.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def load_from_file():
    try:
        with open("list.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
                task_listbox.insert(END, line.strip())
    except FileNotFoundError:
        pass


def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        updated_task = entry.get()
        if updated_task.strip() == "":
            messagebox.showwarning("Warning", "Please enter an updated task.")
        else:
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, updated_task)
            tasks[selected_index] = updated_task
            write_tasks_in_file()
            entry.delete(0, END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")


update_task_button = Button(text="Update task",bg="light blue", fg="black", command=update_task)
update_task_button.pack(pady=10)

load_from_file()

main.mainloop()
