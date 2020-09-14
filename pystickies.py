import tkinter as tk
from tkinter import filedialog


class Menubar:
    def __init__(self, parent):
        font_spec = ("", 14)

        menubar = tk.Menu(parent.master, font=font_spec)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_spec, tearoff=0)
        file_dropdown.add_command(label="New",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open",
                                  command=parent.open_file)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Save",
                                  command=parent.save_file)
        file_dropdown.add_command(label="Save As",
                                  command=parent.save_file_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Quit",
                                  command=parent.master.destroy)
        menubar.add_cascade(label="File", menu=file_dropdown)


class Core:

    def __init__(self, master):
        master.title("Untitled")
        master.geometry("600x400")

        font_spec = ("", 20)

        self.master = master
        self.filename = None

        self.textarea = tk.Text(master, font=font_spec)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)

    def set_window_title(self):
        pass

    def new_file(self):
        pass

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("CSS Files", "*.css"),
                       ("HTML Files", "*.html"),
                       ("Javascript Files", "*.js"),
                       ("Markdown files", "*.md"),
                       ("Python Files", "*.py"),
                       ("Text Files", "*.txt")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())

    def save_file(self):
        pass

    def save_file_as(self):
        pass


# Init root window
if __name__ == '__main__':
    master = tk.Tk()
    pt = Core(master)
    master.mainloop()
