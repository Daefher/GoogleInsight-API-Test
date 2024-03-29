import tkinter as tk
from tkinter import ttk

class Table(tk.Frame):

    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column), borderwidth=0, width=20)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
                self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)
            
    def set( self, row, column, value ):
        print("row:",row," col:",column) 
        widget = self._widgets[row][column]
        widget.configure(text=value)
   
                
