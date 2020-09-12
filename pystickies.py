import tkinter as tk

# Define the main functionality of the app.


class Main:

    def __init__(self, master):
        master.title("Untitled")
        master.geometry("600x400")


# Init root window
if __name__ == '__main__':
    master = tk.Tk()
    pt = Main(master)
    master.mainloop()
