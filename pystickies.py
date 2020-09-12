import tkinter as tk

# Define the main functionality of the app.


class Main:

    def __init__(self, master):
        master.title("Untitled")
        master.geometry("600x400")

        self.textarea = tk.Text(master)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)


# Init root window
if __name__ == '__main__':
    master = tk.Tk()
    pt = Main(master)
    master.mainloop()
