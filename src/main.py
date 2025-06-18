import tkinter as tk
from tkinter import ttk

'''
File:       main.py
Author:     Garret Wilson
Purpose:    generates the main window of the mass-to-count estimator application
'''


class App:

    def __init__(self):
        # create root
        #
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Mass-To-Count Estimator")

        # fake menu bar
        #
        self.toolbar = tk.Frame(self.root, background="gray25")
        self.toolbar.pack_configure(side=tk.TOP, fill=tk.X)

        # help menu
        #
        self.help_button = tk.Menubutton(self.toolbar, text="Help", background="gray25",
                                         borderwidth=1)
        self.help_button.pack(side=tk.LEFT, padx=(5, 0), pady=2)
        self.help_menu = tk.Menu(self.help_button)
        self.help_menu.add_command(label="About", command=self.print_nothing)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="How to use", command=self.print_nothing)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="How it works", command=self.print_nothing)
        self.help_button.config(menu=self.help_menu)

        # inventory memory menu
        #
        self.inventory_memory_button = tk.Menubutton(self.toolbar, text="Inventory Memory",
                                                     background="gray25", borderwidth=1)
        self.inventory_memory_button.pack(side=tk.LEFT)
        self.inventory_memory_menu = tk.Menu(self.inventory_memory_button)
        self.inventory_memory_menu.add_command(label="View inventory memory",
                                               command=self.print_nothing)
        self.inventory_memory_button.config(menu=self.inventory_memory_menu)

        # history menu
        #
        self.history_button = tk.Menubutton(self.toolbar, text="History", background="gray25",
                                            relief="flat", borderwidth=1)
        self.history_button.pack(side=tk.LEFT)
        self.history_menu = tk.Menu(self.history_button)
        self.history_menu.add_command(label="Previously generated results",
                                      command=self.print_nothing)
        self.history_button.config(menu=self.history_menu)

        # frame widget in root
        #
        self.mainframe = ttk.Frame(self.root, padding="20 1 20 20")
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        # title widget in mainframe
        #
        self.label = ttk.Label(self.mainframe, text="Mass-To-Count Estimator", font=("impact", 22),
                               padding="10 10 10 10").pack()

        # canvas widget and scrollbar in mainframe
        #
        self.canvas = tk.Canvas(self.mainframe, background="gray85", relief="ridge",
                                borderwidth=4.5)
        self.scrollbar = ttk.Scrollbar(self.mainframe, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack_configure(side="right", fill="y")
        self.canvas.pack_configure(side="left", fill="both", expand=True)

        # frame widget inside canvas
        #
        self.canvas_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

        self.canvas_frame.bind("<Configure>", self.on_configure)

        for x in range(100):
            ttk.Label(self.canvas_frame, text=f"the number {x}", font=("Arial", 18)).pack_configure(
                padx=20, pady=20)

        self.root.mainloop()

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def print_nothing(self):
        print("nothing")


def main():
    App()


if __name__ == "__main__":
    main()
