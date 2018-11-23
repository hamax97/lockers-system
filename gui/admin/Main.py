#!/usr/bin/python

import Tkinter as tk
import gui

def main():
    root = tk.Tk()
    root.title("Ingresar")
    app = gui.LogIn(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
