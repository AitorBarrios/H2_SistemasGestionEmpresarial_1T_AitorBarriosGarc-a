import sqlite3
my_conn = sqlite3.connect('H2_SGE_1T_AitorBarriosGarcia.db')
###### end of connection ####

##### tkinter window ######
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x250") 

r_set=my_conn.execute('''SELECT detalle.iddet,cliente.nombre,cliente.direccion FROM detalle INNER JOIN cliente ON detalle.idcli = cliente.idcli WHERE detalle.iddet = 1''');
i=0 # row value inside the loop 
for student in r_set: 
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1
my_w.mainloop()