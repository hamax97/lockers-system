import Tkinter as tk
import LendObjects as lo
import Lockers as vl
import MySQLdb
import re
 
class MainMenu:
    def __init__(self, master):
        "Constructor of the class"
        self.db = MySQLdb.connect("localhost", "root", "Xk97jrul97", "locker_system")
        self.cursor = self.db.cursor()

        query = "SELECT contenido FROM casillero WHERE locker_system.casillero.idCasillero = '2' "
        self.cursor.execute(query)
        content = "%s" % self.cursor.fetchone()
        pattern = re.compile("^\s+|\s*,\s*|\s+$")
        content2 =  [x for x in pattern.split(content) if x]
        print content2

        self.master = master
        self.master.minsize(width = 300, height = 300)
        self.frame = tk.Frame(self.master)
        self.master.title("Menu principal")
        self.lendObjectsButton = tk.Button(self.frame, text = 'Prestar Objetos', width = 25, command = self.lend_objects_window)
        self.verifyLockersButton = tk.Button(self.frame, text = 'Verificar Lockers', width = 25, command = self.verify_lockers_window)
        self.exitButton = tk.Button(self.frame, text = 'Salir', width = 15, command = self.close_windows)
        tk.Label(self.frame, text = "").pack()
        self.lendObjectsButton.pack()
        tk.Label(self.frame, text = "").pack()
        tk.Label(self.frame, text = "").pack()
        self.verifyLockersButton.pack()
        tk.Label(self.frame, text = "").pack()
        tk.Label(self.frame, text = "").pack()
        tk.Label(self.frame, text = "").pack()
        self.exitButton.pack()
        self.frame.pack()
        
    def lend_objects_window(self):
        "This function opens a new window for lend objects"
        self.loWindow = tk.Toplevel(self.master)
        self.app = lo.LendObjects(self.loWindow)
        
    def verify_lockers_window(self):
        "This function opens a new window for verify the state of the locker"
        self.vlWindow = tk.Toplevel(self.master)
        self.app = vl.Lockers(self.vlWindow)

    def close_windows(self):
        "This function to close the window"
        self.master.destroy()
