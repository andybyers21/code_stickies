import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
__version__ = "0.1.0"


class Core:
    """ Core functionality of the app. """

    def __init__(self, master):
        """ Set the default layout and geometry of the app. """
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

        self.menubar = MenuBar(self)
        self.statusbar = StatusBar(self)

        self.bind_shortcuts()

    def set_window_title(self, name=None):
        """ Set window title based on filename. """
        if name:
            self.master.title(name)
        else:
            self.master.title("Untitled")

    def new_file(self, *args):
        """ Create a new empty file. """
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        """ Open a file. """
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("CSS", "*.css"),
                       ("HTML", "*.html"),
                       ("Javascript", "*.js"),
                       ("Markdown", "*.md"),
                       ("Python", "*.py"),
                       ("ReStructured Text", "*.rst"),
                       ("Text", "*.txt")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
                self.set_window_title(self.filename)

    def save_file(self, *args):
        """ Save an exsisting file """
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, 'w') as f:
                    f.write(textarea_content)
                    self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_file_as()

    def save_file_as(self, *args):
        """ Save a new file in one of the predefined formats """
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("CSS", "*.css"),
                           ("HTML", "*.html"),
                           ("Javascript", "*.js"),
                           ("Markdown", "*.md"),
                           ("Python", "*.py"),
                           ("ReStructured Text", "*.rst"),
                           ("Text", "*.txt")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
                self.statusbar.update_status(True)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        """ Binds keyboard shortcuts for common functionality. """
        self.textarea.bind('<Command-n>', self.new_file)
        self.textarea.bind('<Command-o>', self.open_file)
        self.textarea.bind('<Command-s>', self.save_file)
        self.textarea.bind('<Command-S>', self.save_file_as)
        self.textarea.bind('<Key>', self.statusbar.update_status)


class MenuBar:
    """ Create the menubar and call its functionality. """

    def __init__(self, parent):
        """ Menubar functions. 

        File:
        - New
        - Open 
        - Save
        - Save As

        About:
        - Release Notes
        - About
        """
        font_spec = ("", 14)

        menubar = tk.Menu(parent.master, font=font_spec)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_spec, tearoff=0)
        file_dropdown.add_command(label="New",
                                  accelerator="Cmd+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open",
                                  accelerator="Cmd+O",
                                  command=parent.open_file)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Save",
                                  accelerator="Cmd+S",
                                  command=parent.save_file)
        file_dropdown.add_command(label="Save As",
                                  accelerator="Cmd+Shift+S",
                                  command=parent.save_file_as)

        about_dropdown = tk.Menu(menubar, font=font_spec, tearoff=0)
        about_dropdown.add_command(label="Release Notes",
                                   command=self.release_message)
        about_dropdown.add_command(label="About",
                                   command=self.about_message)

        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="About", menu=about_dropdown)

    def about_message(self):
        """ Define an about message to be displayed when the menubar item is selected. """
        box_title = "About code_stickies"
        box_message = ("Sticky notes for code. \n"
                       "Developed by Andy Byers, 2020")
        messagebox.showinfo(box_title, box_message)

    def release_message(self):
        """ Define the release notes message to be displayed when the menubar item is selected. """
        box_title = "Release Notes"
        box_message = ("Version - 0.1 \n"
                       "14th September, 2020")
        messagebox.showinfo(box_title, box_message)


class StatusBar:
    """ Defines the default displays of the status bar. """
    default_status = "code_stickies - 0.1"

    def __init__(self, parent):

        font_spec = ("", 11)

        self.status = tk.StringVar()
        self.status.set(self.default_status)

        label = tk.Label(parent.textarea, textvariable=self.status,
                         fg="black", bg="grey", anchor='sw', font=font_spec)

        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        """ Update the display of the status bar based on user actions. """
        if isinstance(args[0], bool):
            self.status.set("Saved")
        else:
            self.status.set(self.default_status)


# Initalize root window
if __name__ == '__main__':
    master = tk.Tk()
    pt = Core(master)
    master.mainloop()
