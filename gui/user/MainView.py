import Tkinter as tk
import serial
import time
import MySQLdb

class MainView:
    def __init__(self, master):
        self.master = master
        self.master.minsize(width = 300, height = 300)
        self.frame = tk.Frame(self.master)
        self.master.title("Casilleros")
        self.frame.grid()
        
        #Arduino
        self.arduinoPort = serial.Serial('COM8', 115200, timeout=1)

        #Mysql
        self.db = MySQLdb.connect("localhost", "root", "Xk97jrul97", "locker_system")
        self.cursor = self.db.cursor()
        
        #Widgets
        self.initLabel = tk.Label(self.frame, text = "                Acerce su carnet al lector")
        self.okButton = tk.Button(self.frame, text = 'Ok', width = 10, command = self.initialize_window)
        self.quitButton = tk.Button(self.frame, text = 'Atras', width = 15, command = self.close_windows)
        self.space1 = tk.Label(self.frame, text="")
        self.space2 = tk.Label(self.frame, text="")
        self.space3 = tk.Label(self.frame, text="")
        self.space4 = tk.Label(self.frame, text="")
        self.space5 = tk.Label(self.frame, text="")

        #Grid
        self.initLabel.grid(row = 0, column = 3,columnspan = 4)
        self.space1.grid()
        self.space2.grid()
        self.space3.grid()
        self.space4.grid()
        self.space5.grid()
        self.okButton.grid(column = 4, columnspan = 4)

    def initialize_window(self):
        "This function waits for put the card close to the antena, and then generates the window"
        self.studentCode = self.arduinoPort.readline()
        while len(self.studentCode) < 8:
            self.arduinoPort.write('c')
            self.studentCode = self.arduinoPort.readline()
        
        print self.studentCode
        
            
        self.initLabel.grid_forget()
        self.okButton.grid_forget()
        self.space1.grid_forget()
        self.space2.grid_forget()
        self.space3.grid_forget()
        self.space4.grid_forget()
        self.space5.grid_forget()

        self.cursor.execute("SELECT codigo FROM usuario WHERE usuario.codigo = '%s'" % self.studentCode)

        code = "%s" % self.cursor.fetchone()
        if code == self.studentCode:
            query = "Select idCasillero From casillero WHERE usuario_idCodigo = %s" % code
            self.cursor.execute(query)
            locker = "%s" % self.cursor.fetchone()
            self.yourLocker = tk.Label(self.frame, text = "                              Su casillero es: " + locker)
            #tk.Label(self.frame, text="").grid()
            
            self.yourLocker.grid(column = 7, columnspan = 6)
            self.space1.grid()
            self.space2.grid()
            self.space3.grid()
            self.space4.grid()
            self.space5.grid()
            self.quitButton.grid(column = 8, columnspan = 6)
            self.arduinoPort.write(locker)
        else:
            tk.Label(self.frame, text="").grid()
            tk.Label(self.frame, text = "      Usted no tiene un casillero asignado").grid(column = 2, columnspan = 3)
            tk.Label(self.frame, text="").grid()
            self.quitButton.grid(column = 2, columnspan = 3)
         
    def close_windows(self):
        "This function destroys the window"
        self.space1.grid_forget()
        self.space2.grid_forget()
        self.space3.grid_forget()
        self.space4.grid_forget()
        self.space5.grid_forget()
        self.yourLocker.destroy()
        self.quitButton.grid_forget()
        #Grid
        self.initLabel.grid(column = 3,columnspan = 4)
        self.space1.grid()
        self.space2.grid()
        self.space3.grid()
        self.space4.grid()
        self.space5.grid()
        self.okButton.grid(column = 4, columnspan = 6)
        