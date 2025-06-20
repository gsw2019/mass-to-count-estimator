import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Mass-To-Count Estimator")

        # Toolbar / menubar
        self.toolbar = tk.Frame(self.root, bg="gray25")
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Fake "Help" button with styled appearance
        self.help_button = tk.Button(
            self.toolbar,
            text="Help",
            bg="gray1",
            fg="black",
            activebackground="gray40",
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            padx=8,
            pady=2,
            highlightthickness=0,
            command=self.show_help_menu
        )
        self.help_button.pack(side=tk.LEFT, padx=(5, 0), pady=2)

        # Real dropdown menu (invisible until triggered)
        self.help_menu = tk.Menu(
            self.root,
            tearoff=0,
            bg="white",
            fg="white",
            activebackground="gray30",
            activeforeground="snow"
        )
        self.help_menu.add_command(label="About", command=self.print_nothing)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="How to use", command=self.print_nothing)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="How it works", command=self.print_nothing)

    def show_help_menu(self):
        # Position the menu right below the button
        x = self.help_button.winfo_rootx()
        y = self.help_button.winfo_rooty() + self.help_button.winfo_height()
        self.help_menu.tk_popup(x, y+4)

    def print_nothing(self):
        print("Clicked menu item")

root = tk.Tk()
app = App(root)
root.mainloop()
