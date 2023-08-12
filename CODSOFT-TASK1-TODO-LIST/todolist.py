from tkinter import *
from tkinter import ttk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('680x650')

        self.label = Label(self.root, text='To-Do List App', font='Arial 25 bold', width=10, bd=5, bg='green', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font='Arial 18 bold', width=10, bd=5, bg='yellow', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', font='Arial 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        self.selected_index = None

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            if delete_:
                self.main_text.delete(delete_)

        def clear_all():
            self.main_text.delete(0, END)
            with open('data.txt', 'w') as file:
                file.truncate()

        def update():
            selected_index = self.main_text.curselection()
            if selected_index:
                self.selected_index = selected_index
                content = self.main_text.get(selected_index)
                self.text.delete(1.0, END)
                self.text.insert(END, content)

        self.button_add = Button(self.root, text="Add", font='Arial 20 bold italic', width=10, bd=5, bg='green', fg='black', command=add)
        self.button_add.place(x=30, y=180)

        self.button_delete = Button(self.root, text="Delete", font='Arial 20 bold italic', width=10, bd=5, bg='red', fg='black', command=delete)
        self.button_delete.place(x=30, y=260)

        self.button_clearall = Button(self.root, text="Clearall", font='Arial 20 bold italic', width=10, bd=5, bg='red', fg='black', command=clear_all)
        self.button_clearall.place(x=30, y=330)

        self.button_update = Button(self.root, text="Update", font='Arial 20 bold italic', width=10, bd=5, bg='blue', fg='black', command=update)
        self.button_update.place(x=30, y=400)


def main():
    root = Tk()
    ui = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
