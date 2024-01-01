import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("My App")

        # create four groups of two checkboxes and labels arranged horizontally on the left
        for i in range(8):
            frame = tk.Frame(master)
            frame.pack(side=tk.LEFT)

            label1 = tk.Label(frame, text="Pin0_"+str(i))
            label1.pack(side=tk.LEFT)

            check1 = tk.Checkbutton(frame, text="In")
            check1.pack(side=tk.LEFT)

            check2 = tk.Checkbutton(frame, text="Out")
            check2.pack(side=tk.LEFT)

        # create four more groups of two checkboxes and labels arranged horizontally on the right
        for i in range(8):
            frame = tk.Frame(master)
            frame.pack(side=tk.RIGHT)

            label1 = tk.Label(frame, text="Pin1_"+str(i))
            label1.pack(side=tk.LEFT)

            check1 = tk.Checkbutton(frame, text="In")
            check1.pack(side=tk.LEFT)

            check2 = tk.Checkbutton(frame, text="Out")
            check2.pack(side=tk.LEFT)

root = tk.Tk()
app = App(root)
root.mainloop()