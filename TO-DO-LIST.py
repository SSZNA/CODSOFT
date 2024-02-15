from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("500x500")
main.title("TO-DO-LIST")
main.config(bg="indigo")
main.minsize(400,400)
main.maxsize(600,500)

Label = Label(text='''WELCOME TO YOUR TO-DO-LIST ORGANISER''',bg="#FFFDD0",fg="black",padx=10,pady=10,font="comicsanms 13 bold",borderwidth=5,relief=RIDGE)
Label.pack()

Entry = Entry(main,font=("Helvetica",13),bg="#FFFDD0")
Entry.pack(pady=20)

frame=Frame(main,bg="#FFFDD0")
frame.pack(side=RIGHT)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)
list=Listbox(frame,width=30,height=14,font=('Helvetica',14),borderwidth=5,relief=RIDGE,fg="black",selectbackground="grey",yscrollcommand = scrollbar.set)
list.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=list.yview)
tasks=["Breakfast","Go to school","Lunch","Take a nap","Prepare for test","Play football","Watch tv","Exercise","Study maths","Read newspaper","Read story book","Arranging wardrobe","cooking a meal","Meeting relatives","Hanging out with friends"]
for item in tasks:
    list.insert(END,item)

def AddTask():
    task=Entry.get()
    if  task=="":
        messagebox.showwarning("Warning","Kindly enter a task")
    else:
        list.insert(END,task)
        Entry.delete(0, END)


add_task_button=Button(text="Add task",bg="light pink",fg="black",command=AddTask)
add_task_button.pack(pady=30)

def DeleteTask():
    list.delete(ANCHOR)
delete_task_button=Button(text="Delete task",bg="light green",fg="black",command=DeleteTask)
delete_task_button.pack(pady=10)


def WriteTasksInFile():
    with open("list.txt","w") as f:
        for task in tasks:
            f.write(task + "\n")
def loadFromFile():
    try:
        with open("list.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
                list.insert(END, line.strip())
    except FileNotFoundError:
        pass
def UpdateTask():
    try:
        task_index = list.curselection()[0]
        updated_task = Entry.get()
        if updated_task.strip() == "":
            messagebox.showwarning("Warning", "Please enter an updated task.")
        else:
            list.delete(task_index)
            list.insert(task_index, updated_task)
            tasks[task_index] = updated_task
            WriteTasksInFile()
            Entry.delete(0, END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

update_task_button=Button(text="Update task",bg="light blue",fg="black",command=UpdateTask)
update_task_button.pack(pady=10)
loadFromFile()

main.mainloop()
