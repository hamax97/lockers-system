import Tkinter as tk
import tkMessageBox
import MySQLdb
import re
"Clase que sirve para poder verificar, notificar y liberar el contenido de los casilleros"
class Lockers:
    

    def __init__(self, master):
        "Clase contructor"
        #Initialize MySQL variables
        self.db = MySQLdb.connect("localhost", "root", "Xk97jrul97", "locker_system")
        self.cursor = self.db.cursor()
        query = "SELECT idCasillero FROM casillero WHERE locker_system.casillero.contenido != '' "
        self.cursor.execute(query)
        self.lockerList = [i[0] for i in self.cursor.fetchall()]

        self.buttonsList = []
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Verificar Lockers")
        self.master.minsize(width = 240, height = 200)
        self.initialize_lockers()


        self.frame.grid()
        
        tk.Label(self.frame, text = "Seleccione el locker que desea revisar:").grid(row = 0, columnspan = 4)
        
        j = 0
        while j < len(self.lockerList):
            test = int(self.lockerList[j])
            self.buttonsList[test-1].grid(columnspan = 4)
            j += 1

        tk.Label(self.frame, text = "").grid(columnspan = 4)
        self.quitButton = tk.Button(self.frame, text = 'Salir', width = 8, command = self.close_windows)
        self.quitButton.grid(column = 1, columnspan = 2)

        

        
    def close_windows(self):
        "This function destroys the window"
        self.master.destroy() #This way of close the window produces the bug
        
    def initialize_lockers(self):
        "Function to initialize all the lockers"
        size = 15
        
        i = 0
        #while i < len(self.lockerList):
        #    test = self.lockerList[i]
        #    self.buttonsList.append(tk.Button(self.frame, text = "Locker "+ test, width = size, command=self.open_locker(test)))
        #    print test
        #    i += 1
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 1", width = size, command = lambda: self.open_locker(1)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 2", width = size, command = lambda: self.open_locker(2)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 3", width = size, command = lambda: self.open_locker(3)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 4", width = size, command = lambda: self.open_locker(4)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 5", width = size, command = lambda: self.open_locker(5)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 6", width = size, command = lambda: self.open_locker(6)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 7", width = size, command = lambda: self.open_locker(7)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 8", width = size, command = lambda: self.open_locker(8)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 9", width = size, command = lambda: self.open_locker(9)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 10", width = size, command = lambda: self.open_locker(10)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 11", width = size, command = lambda: self.open_locker(11)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 12", width = size, command = lambda: self.open_locker(12)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 13", width = size, command = lambda: self.open_locker(13)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 14", width = size, command = lambda: self.open_locker(14)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 15", width = size, command = lambda: self.open_locker(15)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 16", width = size, command = lambda: self.open_locker(16)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 17", width = size, command = lambda: self.open_locker(17)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 18", width = size, command = lambda: self.open_locker(18)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 19", width = size, command = lambda: self.open_locker(19)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 20", width = size, command = lambda: self.open_locker(20)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 21", width = size, command = lambda: self.open_locker(21)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 22", width = size, command = lambda: self.open_locker(22)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 23", width = size, command = lambda: self.open_locker(23)))
        self.buttonsList.append(tk.Button(self.frame, text = "Locker 24", width = size, command = lambda: self.open_locker(24)))
        
    def open_locker(self, number):
        "Indicates to the arduino to open the locker number: number"

        self.objWindow = tk.Toplevel(self.master)
        self.app = Objects(self.objWindow, number)
    

class Objects:
    
    def __init__(self, master, number):
        "Class constructor"
        self.db = MySQLdb.connect("localhost", "root", "Xk97jrul97", "locker_system")
        self.cursor = self.db.cursor()
        "Busca el contenido en la base de datos, los separa por comas y los guarda en un arreglo para su posterior visualizacion"
        query = "SELECT contenido FROM casillero WHERE locker_system.casillero.idCasillero = '%s' " % str(number)
        self.cursor.execute(query)
        content = "%s" % self.cursor.fetchone()
        pattern = re.compile("^\s+|\s*,\s*|\s+$")
        self.objectsList =  [x for x in pattern.split(content) if x]

        self.number = number
        self.master = master
        self.master.title("Objetos")
        self.master.minsize(180, 100)
        self.frame = tk.Frame(self.master)
        
        tk.Label(self.frame, text = "        Locker: " + str(number)).grid(row = 0, columnspan = 5)

        #Buttons
        self.freeLocker = tk.Button(self.frame, text = "Liberar", width = 7, command = lambda: self.free_locker(number))
        self.pending = tk.Button(self.frame, text = "Pendiente", width = 7, command = lambda: self.pending_locker(number))
        self.quitButton = tk.Button(self.frame, text = 'Salir', width = 5, command = self.close_windows)

        #Labels: Son utilizadas para mostrar los objetos del arreglo donde se encuentra el contenido
        i = 0
        while i < len(self.objectsList):
            tk.Label(self.frame, text = "- " + self.objectsList[i]).grid(row = i + 1, columnspan = 4)
            i += 1

        tk.Label(self.frame, text="").grid()
        i += 1
        self.freeLocker.grid(row = i+1, column = 2, columnspan = 2)
        self.pending.grid(row = i+1, column = 4, columnspan = 2)
        self.quitButton.grid(row = i+2, column = 3, columnspan = 2)
        self.frame.grid()

    def free_locker(self, number):
        "Esta funcion elimina todo el contenido asociado a un usuario, y al usuario en si de la base de datos"
        
        
        query = "Select casillero.usuario_idCodigo FROM casillero WHERE casillero.idCasillero = %s" % (str(number))
        self.cursor.execute(query)
        code = "%s" % self.cursor.fetchone()
        print str(code)
        query = "DELETE FROM locker_system.usuario where codigo = %s " % str(code)
        self.cursor.execute(query)
        #self.cursor.execute("DELETE FROM locker_system.usuario where codigo = %s", code)
        self.db.commit()
        query = "UPDATE locker_system.casillero SET usuario_idCodigo = '',contenido = ''  WHERE idCasillero = %s" % str(number)
        self.cursor.execute(query)
        self.db.commit()
        print "Casillero liberado"
        self.objWindow2 = tk.Toplevel(self.master)
        self.obje = Lockers(self.objWindow2)
        self.buttonsList[number - 1].destroy()
        self.master.destroy()

    def pending_locker(self, number):
        "Funcion que envia un mensaje de alerta al estudiante"
        query = "Select usuario.mail FROM casillero INNER JOIN usuario ON casillero.usuario_idCodigo = usuario.codigo WHERE casillero.idCasillero = %s" % str(number)
        self.cursor.execute(query)
        mail = "%s" % self.cursor.fetchone()
        tkMessageBox.showinfo("Advertencia Enviada", "Correo electronico de reclamo enviado al estudiante: %s" % mail, parent = self.frame)

    def close_windows(self):
        "This function destroys the window"
        self.master.destroy()
