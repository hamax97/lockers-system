import Tkinter as tk
import MainMenu as mm
import MySQLdb
import tkMessageBox

class LogIn:
    def __init__(self, master):
        "Constructor of the class"
        #MySQL
        #The third parameter is the password of your mysql
        self.db = MySQLdb.connect("localhost", "root", "Xk97jrul97", "locker_system")

        #A cursor is a virtual table
        self.cursor = self.db.cursor()
        
        self.master = master
        self.master.minsize(width = 250, height = 130)
        self.frame = tk.Frame(self.master)

        #Buttons
        self.quitButton = tk.Button(self.frame, text = 'Salir', width = 4, command = self.close_windows)
        self.logIn = tk.Button(self.frame, text = 'Ingresar', width = 15, command = self.log_in)
        
        #Entries
        self.user = tk.Entry(self.frame)
        self.password = tk.Entry(self.frame)
        self.password.config(show = "*")

        self.frame.grid()

        tk.Label(self.frame, text = "    ").grid(row = 0, column = 0)
        tk.Label(self.frame, text = "Usuario:").grid(row = 0, column = 1, columnspan = 3)
        tk.Label(self.frame, text = "    ").grid(row = 1, column = 0)
        self.user.grid(row = 1, column = 1, columnspan = 3)
        tk.Label(self.frame, text = "    ").grid(row = 2, column = 0)
        tk.Label(self.frame, text = "Password:").grid(row = 2, column = 1, columnspan = 3)
        tk.Label(self.frame, text = "    ").grid(row = 3, column = 0)
        self.password.grid(row = 3, column = 1, columnspan = 3)
        tk.Label(self.frame, text = "").grid(row = 4, column = 1, columnspan = 3)
        self.quitButton.grid(row = 5, column = 1)
        self.logIn.grid(row = 5, column = 2, columnspan = 2)
        
    #This function executes when the button Ingresar is pressed
    def log_in(self):
        "Function to open the main menu"
        try:
            self.cursor.execute("SELECT user_name FROM users WHERE user_name = 'admin'")
            user = "%s" % self.cursor.fetchone()
            self.cursor.execute("SELECT password FROM users WHERE user_name = 'admin'")
            password = "%s" % self.cursor.fetchone()
            
            if(self.user.get() != user):
                raise ValueError("Usuario o contrasena incorrectos")
            if(self.password.get() != password):
                raise ValueError("Usuario o contrasena incorrectos")
        except ValueError as error:
            self.show_alert(repr(error))
        else:
            self.mainMenu = tk.Toplevel(self.master)
            self.app = mm.MainMenu(self.mainMenu)
        
    def close_windows(self):
        "Function to close the window"
        self.master.destroy()

    def show_alert(self, message):
        "Function to show an alert box"
        tkMessageBox.showinfo("Error", message, parent = self.frame)
