#!/usr/bin/python
import MainView
import Tkinter as tk

def main():
    root = tk.Tk()
    root.title("Casillero")
    app = MainView.MainView(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
