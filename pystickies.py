import tkinter as tk


class Menubar:
    def __init__(self, parent):
        font_spec = ("", 14)

        menubar = tk.Menu(parent.master, font=font_spec)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_spec, tearoff=0)
        file_dropdown.add_command(label="New")
        file_dropdown.add_command(label="Open")
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Save")
        file_dropdown.add_command(label="Save As")
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Quit")

        menubar.add_cascade(label="File", menu=file_dropdown)


class Main:

    def __init__(self, master):
        master.title("Untitled")
        master.geometry("600x400")

        font_spec = ("", 20)

        self.master = master

        self.textarea = tk.Text(master, font=font_spec)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)


# Init root window
if __name__ == '__main__':
    master = tk.Tk()
    pt = Main(master)
    master.mainloop()
