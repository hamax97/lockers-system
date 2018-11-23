import Tkinter as tk
import tkMessageBox
import serial
import time
import MySQLdb
"Clase que sirve para prestar objetos a los estudiantes"
class LendObjects:

    lrow = 0
    def __init__(self, master):
        "Constructor of the class"

        #Inicializa las credenciales de la base de datos MySQL, estas se deben cambiar dependiendo de la base de datos
        self.db = MySQLdb.connect("localhost", "root", "Xk97jrul97", "locker_system")
        self.cursor = self.db.cursor()
        #Construye la ventana principal
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Prestar Objetos")
        self.master.minsize(width = 340, height = 180)

        self.arduinoPort = serial.Serial('COM3', 115200, timeout=1) #Define el puerto serial, este por errores haciendo el proyecto debe cambiarse el com por el
                                                                    #correspondiente del arduino

        self.frame.grid()
        #Construye lo que hay dentro de la ventana principal
        self.initLabel = tk.Label(self.frame, text = "                    Acerque el carnet al lector:")
        self.initLabel.grid(row = self.lrow, column = 2, columnspan = 5)
        self.okButton = tk.Button(self.frame, text = 'Ok', width = 10, command = self.initialize_window)
        self.okButton.grid(row = self.lrow + 1, column = 4, columnspan = 6)
        
    #Funcion donde se lee el carnet cuando se presiona el boton ok
    def initialize_window(self):
        "Esta funcion espera por que el carnet este cerca, para comprobarlo y general la ventana"
        self.studentCode = self.arduinoPort.readline()
        while len(self.studentCode) < 8:
            self.arduinoPort.write('c')
            self.studentCode = self.arduinoPort.readline()
            print self.studentCode
            
        self.initLabel.grid_forget()
        self.okButton.grid_forget()
        #Manda un comando a la base de datos para poder verificar que el codigo leido por el rfid, este en esta, y guarda el resultado en la variable code
        self.cursor.execute("SELECT locker_system.usuario.codigo FROM usuario WHERE locker_system.usuario.codigo = '%s'" % self.studentCode)
        code = "%s" % self.cursor.fetchone()
        
        self.quitButton = tk.Button(self.frame, text = 'Salir', width = 10, command = self.close_windows)

        #Si el estudiante ya esta en la base de datos, muestra la información y una ventana por si se deseea actualziar el contenido del casillero
        #Sino, muestra una ventana de registro para poder ingresar los datos y el contenido del casillero
        if code == self.studentCode:
            self.master.minsize(width = 450, height = 180)
            #Obtiene los datos del usuario y los almacena mas abajo
            query = "SELECT nombre, celular, mail FROM usuario WHERE locker_system.usuario.codigo = '%s'" % code
            self.cursor.execute(query)
            results = self.cursor.fetchone()
            stName = results[0]
            stPhone = results[1]
            stMail = results[2]
            #Obtiene el casillero del usuario y el contenido de este
            query = "SELECT idCasillero, contenido FROM casillero WHERE locker_system.casillero.usuario_idCodigo = '%s'" % code
            self.cursor.execute(query)
            results2 = self.cursor.fetchone()
            self.stLocker = results2[0]
            stContent = results2[1]

            self.text = tk.Text(self.frame, width = 27, height = 8, wrap = "word")
            self.updateButton = tk.Button(self.frame, text = 'Actualizar', width = 12, command = self.update_objects)

            #Grid: Construye la ventana con los datos de la base de datos
            tk.Label(self.frame, text = "Estudiante:").grid(row = self.lrow, column = 0, columnspan = 5)
            tk.Label(self.frame, text = "Objetos").grid(row = self.lrow, column = 5, columnspan = 5)
            self.lrow += 1
            tk.Label(self.frame, text = "   Nombre: ").grid(row = self.lrow, column = 0)
            tk.Label(self.frame, text = "%s" % stName).grid(row = self.lrow, column = 1)

            self.text.grid(row = self.lrow, column = 5, rowspan=5)
            query = ""
            self.text.insert('insert', stContent)
            content = self.text.get('1.0', 'end')
            query=""

            self.lrow += 1
            tk.Label(self.frame, text = "   Correo: ").grid(row = self.lrow, column = 0)
            tk.Label(self.frame, text = "%s" % stMail).grid(row = self.lrow, column = 1)
            self.lrow += 1
            tk.Label(self.frame, text = "   Celular:").grid(row = self.lrow, column = 0)
            tk.Label(self.frame, text = "%s" % stPhone).grid(row = self.lrow, column = 1)
            self.lrow += 1
            tk.Label(self.frame, text = "   Casillero:").grid(row = self.lrow, column = 0)
            tk.Label(self.frame, text = "%s" % self.stLocker).grid(row = self.lrow, column = 1)
            self.lrow += 1
            self.lrow += 1
            self.quitButton.grid(row = self.lrow, columnspan = 5)
            self.updateButton.grid(row = self.lrow, column = 5)
            self.lrow += 1
            

            
        else:
    
            #Entries: Entradas de texto
            
            self.studentName = tk.Entry(self.frame, width = 32)
            self.studentMail = tk.Entry(self.frame, width = 32)
            self.studentPhone = tk.Entry(self.frame, width = 32)
            self.studentLocker = tk.Entry(self.frame, width = 32)

            #Buttons
            self.registerButton = tk.Button(self.frame, text = 'Registrar', width = 15, command = self.register_student)

            #Grid
            tk.Label(self.frame, text = "Estudiante:").grid(row = self.lrow, column = 0, columnspan = 5)
            self.lrow += 1
            tk.Label(self.frame, text = "   Nombre:").grid(row = self.lrow, column = 0)
            self.studentName.grid(row = self.lrow, column = 1, columnspan = 4)
            self.lrow += 1
            tk.Label(self.frame, text = "   Correo:").grid(row = self.lrow, column = 0)
            self.studentMail.grid(row = self.lrow, column = 1, columnspan = 4)
            self.lrow += 1
            tk.Label(self.frame, text = "   Celular:").grid(row = self.lrow, column = 0)
            self.studentPhone.grid(row = self.lrow, column = 1, columnspan = 4)
            self.lrow += 1
            tk.Label(self.frame, text = "   Locker:").grid(row = self.lrow, column = 0)
            self.studentLocker.grid(row = self.lrow, column = 1, columnspan = 4)
            self.lrow += 1
            self.registerButton.grid(row = self.lrow, columnspan = 5)
            self.lrow += 1
            self.quitButton.grid(row = self.lrow, columnspan = 5)
            self.lrow += 1
            

    def update_objects(self):
        "Actualiza el contenido de la base de datos si se presiona actualizar en la ventana correspondiente"
        conten = self.text.get("1.0","end") # Esta parte es para obtener el contenido de la caja de texto y que actualice
        self.cursor.execute("UPDATE locker_system.casillero SET contenido = %s  WHERE idCasillero = %s", (conten, self.stLocker))
        self.db.commit()
        "Muestra mensaje de confirmacion"
        tkMessageBox.showinfo("Actualizado", "Se ha actualizado la lista de objetos", parent = self.frame)

    def close_windows(self):
        "Esta funcion cierra la ventena"
        self.arduinoPort.close()
        self.master.destroy()

    def register_student(self):
        "Esta funcion registra al estudiante con la informacion registrada en la base de datos"
        try:
            code = self.studentCode
            name = self.studentName.get()
            mail = self.studentMail.get()
            phone = self.studentPhone.get()
            casillero = self.studentLocker.get()

            query = "Select usuario_idCodigo FROM casillero WHERE idCasillero = %s" % casillero
            self.cursor.execute(query)
            check = "%s" % self.cursor.fetchone()
            print check
            if check != "":
                raise ValueError("Casillero ocupado")
            self.cursor.execute("INSERT INTO locker_system.usuario (codigo, nombre,celular,mail) VALUES (%s,%s,%s,%s)", (code, name, phone, mail))
            self.db.commit()
            self.cursor.execute("UPDATE locker_system.casillero SET usuario_idCodigo = %s  WHERE idCasillero = %s", (code, casillero))
            self.db.commit()
            
            if name == "" or mail == "" or phone == "":
                raise ValueError("Datos incorrectos")
            
        except ValueError as error:
            self.show_alert(repr(error))
        else:
            #Put the student information inside the database
            self.objects_to_lend()

    def objects_to_lend(self):
        "Esta funcion registra los objetos del usuario en la base de datos"
        tk.Label(self.frame, text = "Objetos a prestar").grid(row = self.lrow)
        self.lrow += 1
        self.firstObject = tk.Entry(self.frame, width = 40)
        
        self.firstObject.grid(row = self.lrow, column = 0, columnspan = 6)
        self.lrow += 1
        
        self.assignButton = tk.Button(self.frame, text = "Asginar Locker", width = 15, command = self.assign_locker)
        self.assignButton.grid(row = self.lrow, columnspan = 5)
        self.lrow += 1
        self.quitButton.grid(row = self.lrow, columnspan = 5)
        
    
    def assign_locker(self):
        "Esta funcion sirve para asignar el casillero al usuario, una vez oprimido start"
        numeroCasillero = self.studentLocker.get()
        content = self.firstObject.get()
        try:
            if self.firstObject.get() == "":
                raise ValueError("Inserte por lo menos un objeto")
        except ValueError as error:
            self.show_alert(repr(error))
        else:
            #This part is incomplete, the values 77 and Feb 1 are invented
            #Left to connect to the database
            self.cursor.execute("UPDATE locker_system.casillero SET contenido = %s  WHERE idCasillero = %s", (content, numeroCasillero))
            self.db.commit()
            self.quitButton.grid(row = 12, columnspan = 2)

    def show_alert(self, message):
        "Funcion que muestra un mensaje de error"
        
        tkMessageBox.showinfo("Error", message, parent = self.frame)
  

# Para un posible boton de actualizar
