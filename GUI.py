import subprocess
import tkinter as tk
from tkinter import ttk

class MyWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Set custom color scheme
        bg_color = '#e1d8b9'
        fg_color = '#3d3d3d'
        btn_bg_color = '#3d3d3d'
        btn_fg_color = '#e1d8b9'
        entry_bg_color = '#ffffff'
        entry_fg_color = '#3d3d3d'

        # Configure window
        self.master.configure(bg=bg_color)
        self.master.title('Anaconda Prompt')
        self.master.geometry('400x200')

        # Create style object to configure buttons
        style = ttk.Style()
        style.configure('TButton', background=btn_bg_color, foreground=btn_fg_color, font=('Arial', 20), padding=10)

        # Create widgets
        ''' self.label = ttk.Label(self, text='Enter a command:', foreground=fg_color, background=bg_color, font=('Arial', 14))
        self.label.pack(side='top', pady=10)
        self.entry = ttk.Entry(self, background=entry_bg_color, foreground=entry_fg_color, font=('Arial', 12))
        self.entry.pack(pady=10)'''
        self.button = ttk.Button(self, text='Activate Gaze Pointer', command=self.execute_command, cursor='hand2')
        self.button.pack(pady=50)

    def execute_command(self):
        command = "python mouse-cursor-control.py"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = result.stdout.decode('utf-8')
        if output:
            output_label = ttk.Label(self, text=output, foreground='#008000', background='#ffffff', font=('Arial', 12, 'bold'))
            output_label.pack(side='top', pady=10)

root = tk.Tk()
window = MyWindow(master=root)
window.mainloop()
