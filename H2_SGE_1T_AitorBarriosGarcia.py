import customtkinter as ctk
import tkinter as tk
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from tkinter import messagebox,ttk,Scrollbar,Label,Entry,Button,END

ventana = ctk.CTk()
ventana.title("H2_SistemasGestionEmpresarial_1T_AitorBarriosGarcía")
ventana.resizable(False,False)
ventana.geometry("1000x850")

cat = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//categoria.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//categoria.png"),size=(70,70))
cli = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//cliente.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//cliente.png"),size=(100,80))
pro = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//producto.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//producto.png"),size=(70,70))
ped = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//pedido.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//pedido.png"),size=(70,70))
det = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//detalle.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//detalle.png"),size=(70,70))
bus = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//busqueda.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//busqueda.png"),size=(70,70))
gra = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//grafico.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//grafico.png"),size=(70,70))
exl = ctk.CTkImage(light_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//excel.png"),
                    dark_image=Image.open("G://Mi unidad//2ºDAM//Sistemas de Gestión Empresarial//HITOS//H2_SistemasGestionEmpresarial_1T_Aitor_BarriosGarcia//img//excel.png"),size=(70,70))

def vCat():
    def crear_reg():
        id_cat = entCat_id.get()
        nombre_cat = entCat_nombre.get()

        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Categoria (idcat,nombre) VALUES (?,?)",(id_cat,nombre_cat))
            conn.commit()
            mostrar_reg()
            messagebox.showinfo("✔","Categoría Creada")

    def leer_reg():
        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()
            cursor.execute("select * from Categoria")
            registros = cursor.fetchall()
        return registros
    
    def mostrar_reg():
        lista_reg.delete(*lista_reg.get_children())
        for registro in leer_reg():
            lista_reg.insert("","end",values=registro)

    def eliminar_reg():
        seleccion = lista_reg.selection()
        if seleccion:

            id_seleccionado = lista_reg.item(seleccion, "values")[0]
            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                cursor.execute("DELETE FROM Categoria WHERE idcat = ?", id_seleccionado)
                conn.commit()
                mostrar_reg()
                messagebox.showinfo("✔", "Categoria Eliminada")

    def modificar_reg():
        seleccion = lista_reg.selection()
        if seleccion:
            id_select = lista_reg.item(seleccion,"values")[0]

            nuevo_id=entCat_id.get()
            nuevo_nombre=entCat_nombre.get()

            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                try:
                    cursor.execute("UPDATE Categoria SET idcat=?,nombre=? where idcat=?",(nuevo_id,nuevo_nombre,id_select))
                    conn.commit()
                    mostrar_reg()
                    messagebox.showinfo("✔","Categoria Modificada")
                except sqlite3.Error as e:
                    messagebox.showerror("❌",f"No se pudo modificar: {e}")


    vCat = ctk.CTkToplevel(ventana)
    vCat.title("Categoría")
    vCat.resizable(False,False)
    vCat.geometry("1000x850")

    lblCat_id = ctk.CTkLabel(vCat,text="ID")
    lblCat_id.grid(row=0,column=0,padx=10,pady=10)
    entCat_id = ctk.CTkEntry(vCat)
    entCat_id.grid(row=0,column=1)

    lblCat_nombre = ctk.CTkLabel(vCat,text="Nombre")
    lblCat_nombre.grid(row=1,column=0,padx=10,pady=10)
    entCat_nombre = ctk.CTkEntry(vCat)
    entCat_nombre.grid(row=1,column=1)

    bt_crear = ctk.CTkButton(vCat,text="Crear",command=crear_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_crear.grid(row=0,column=2,padx=10,pady=10)
    bt_eliminar = ctk.CTkButton(vCat,text="Eliminar",command=eliminar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_eliminar.grid(row=0,column=3,padx=10,pady=10)
    bt_modificar = ctk.CTkButton(vCat,text="Modificar",command=modificar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_modificar.grid(row=1,column=2,padx=10,pady=10)

    def ordenar_columna(tree, col, reverse):
        data = [ (tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for i, item in enumerate(data):
            tree.move(item[1], '', i)
        tree.heading(col, command=lambda: ordenar_columna(tree, col, not reverse))

    lista_reg = ttk.Treeview(vCat,columns=("ID","Nombre"),show="headings",selectmode="browse")
    lista_reg.heading("ID",text="ID", command=lambda: ordenar_columna(lista_reg, "ID", False))
    lista_reg.heading("Nombre",text="Nombre", command=lambda: ordenar_columna(lista_reg, "Nombre", False))
    lista_reg.column("ID",width=200)
    lista_reg.column("Nombre",width=200)

    estilo=ttk.Style()
    estilo.configure("Treeview",background="#565b5e",foreground="white",rowheight=25)
    estilo.map("Treeview",background=[('selected','#6954a7')])
    lista_reg.grid(row=2, column=0, rowspan=6, padx=10, pady=10, sticky="nsew")
    scrollbar = Scrollbar(vCat, orient="vertical", command=lista_reg.yview)
    scrollbar.grid(row=2, column=1, rowspan=6, sticky="ns")
    lista_reg.configure(yscrollcommand=scrollbar.set)

    mostrar_reg()
    vCat.mainloop()

def vCli():
    def crear_reg():
        id_cli = entCli_id.get()
        nombre_cli = entCli_nombre.get()
        apellido_cli = entCli_apellido.get()
        telefono_cli = entCli_telefono.get()
        mail_cli = entCli_mail.get()
        direccion_cli = entCli_direccion.get()

        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO cliente (idcli,nombre,apellido,telefono,mail,direccion) VALUES (?,?,?,?,?,?)",(id_cli,nombre_cli,apellido_cli,telefono_cli,mail_cli,direccion_cli))
            conn.commit()
            mostrar_reg()
            messagebox.showinfo("✔","Cliente Creado")

    def leer_reg():
        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cliente")
            registros = cursor.fetchall()
        return registros
    
    def mostrar_reg():
        lista_reg.delete(*lista_reg.get_children())
        for registro in leer_reg():
            lista_reg.insert("","end",values=registro)

    def eliminar_reg():
        seleccion = lista_reg.selection()
        if seleccion:

            id_seleccionado = lista_reg.item(seleccion, "values")[0]
            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                cursor.execute("DELETE FROM cliente WHERE idcli = ?", id_seleccionado)
                conn.commit()
                mostrar_reg()
                messagebox.showinfo("✔", "Cliente Eliminado")

    def modificar_reg():
        seleccion = lista_reg.selection()
        if seleccion:
            id_select = lista_reg.item(seleccion,"values")[0]

            nuevo_id=entCli_id.get()
            nuevo_nombre=entCli_nombre.get()
            nuevo_apellido=entCli_apellido.get()
            nuevo_telefono=entCli_telefono.get()
            nuevo_mail=entCli_mail.get()
            nuevo_direccion=entCli_direccion.get()

            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                try:
                    cursor.execute("UPDATE cliente SET idcli=?,nombre=?,apellido=?,telefono=?,mail=?,direccion=? where idcli=?",
                                    (nuevo_id,nuevo_nombre,nuevo_apellido,nuevo_telefono,nuevo_mail,nuevo_direccion,id_select))
                    conn.commit()
                    mostrar_reg()
                    messagebox.showinfo("✔","Cliente Modificado")
                except sqlite3.Error as e:
                    messagebox.showerror("❌",f"No se pudo modificar: {e}")

    vCli = ctk.CTkToplevel(ventana)
    vCli.title("Cliente")
    vCli.resizable(False,False)
    vCli.geometry("1000x850")

    lblCli_id = ctk.CTkLabel(vCli,text="ID")
    lblCli_id.grid(row=0,column=0,padx=10,pady=10)
    entCli_id = ctk.CTkEntry(vCli)
    entCli_id.grid(row=0,column=1)

    lblCli_nombre = ctk.CTkLabel(vCli,text="Nombre")
    lblCli_nombre.grid(row=1,column=0,padx=10,pady=10)
    entCli_nombre = ctk.CTkEntry(vCli)
    entCli_nombre.grid(row=1,column=1)

    lblCli_apellido = ctk.CTkLabel(vCli,text="Apellido")
    lblCli_apellido.grid(row=2,column=0,padx=10,pady=10)
    entCli_apellido = ctk.CTkEntry(vCli)
    entCli_apellido.grid(row=2,column=1)

    lblCli_telefono = ctk.CTkLabel(vCli,text="Telefono")
    lblCli_telefono.grid(row=3,column=0,padx=10,pady=10)
    entCli_telefono = ctk.CTkEntry(vCli)
    entCli_telefono.grid(row=3,column=1)

    lblCli_mail = ctk.CTkLabel(vCli,text="Mail")
    lblCli_mail.grid(row=4,column=0,padx=10,pady=10)
    entCli_mail = ctk.CTkEntry(vCli)
    entCli_mail.grid(row=4,column=1)

    lblCli_direccion = ctk.CTkLabel(vCli,text="Dirección")
    lblCli_direccion.grid(row=5,column=0,padx=10,pady=10)
    entCli_direccion = ctk.CTkEntry(vCli)
    entCli_direccion.grid(row=5,column=1)

    bt_crear = ctk.CTkButton(vCli,text="Crear",command=crear_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_crear.grid(row=6,column=0,padx=10,pady=10)
    bt_eliminar = ctk.CTkButton(vCli,text="Eliminar",command=eliminar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_eliminar.grid(row=7,column=0,padx=10,pady=10)
    bt_modificar = ctk.CTkButton(vCli,text="Modificar",command=modificar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_modificar.grid(row=8,column=0,padx=10,pady=10)

    def ordenar_columna(tree, col, reverse):
        data = [ (tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for i, item in enumerate(data):
            tree.move(item[1], '', i)
        tree.heading(col, command=lambda: ordenar_columna(tree, col, not reverse))

    lista_reg = ttk.Treeview(vCli,columns=("ID","Nombre","Apellido","Telefono","Mail","Direccion"),show="headings",selectmode="browse")
    lista_reg.heading("ID",text="ID", command=lambda: ordenar_columna(lista_reg, "ID", False))
    lista_reg.heading("Nombre",text="Nombre", command=lambda: ordenar_columna(lista_reg, "Nombre", False))
    lista_reg.heading("Apellido",text="Apellido", command=lambda: ordenar_columna(lista_reg, "Apellido", False))
    lista_reg.heading("Telefono",text="Telefono", command=lambda: ordenar_columna(lista_reg, "Telefono", False))
    lista_reg.heading("Mail",text="Mail", command=lambda: ordenar_columna(lista_reg, "Mail", False))
    lista_reg.heading("Direccion",text="Direccion", command=lambda: ordenar_columna(lista_reg, "Direccion", False))
    lista_reg.column("ID",width=110)
    lista_reg.column("Nombre",width=110)
    lista_reg.column("Apellido",width=110)
    lista_reg.column("Telefono",width=110)
    lista_reg.column("Mail",width=110)
    lista_reg.column("Direccion",width=110)
    estilo=ttk.Style()
    estilo.configure("Treeview",background="#565b5e",foreground="white",rowheight=25)
    estilo.map("Treeview",background=[('selected','#6954a7')])
    lista_reg.grid(row=0, column=2, rowspan=6, padx=10, pady=10, sticky="nsew")
    scrollbar = Scrollbar(vCli, orient="vertical", command=lista_reg.yview)
    scrollbar.grid(row=0, column=3, rowspan=6, sticky="ns")
    lista_reg.configure(yscrollcommand=scrollbar.set)

    mostrar_reg()
    vCli.mainloop()

def vPro():
    def crear_reg():
        id_Pro = entPro_id.get()
        nombre_Pro = entPro_nombre.get()
        stock_Pro = entPro_stock.get()
        precio_Pro = entPro_precio.get()
        idcat_Pro = entPro_idcategoria.get()

        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO producto (idpro,nombre,stock,precio,idcat) VALUES (?,?,?,?,?)",(id_Pro,nombre_Pro,stock_Pro,precio_Pro,idcat_Pro))
            conn.commit()
            mostrar_reg()
            messagebox.showinfo("✔","Producto Creado")

    def leer_reg():
        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM producto")
            registros = cursor.fetchall()
        return registros
    
    def mostrar_reg():
        lista_reg.delete(*lista_reg.get_children())
        for registro in leer_reg():
            lista_reg.insert("","end",values=registro)

    def eliminar_reg():
        seleccion = lista_reg.selection()
        if seleccion:

            id_seleccionado = lista_reg.item(seleccion, "values")[0]
            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                cursor.execute("DELETE FROM producto WHERE idpro = ?", id_seleccionado)
                conn.commit()
                mostrar_reg()
                messagebox.showinfo("✔", "Producto Eliminado")

    def modificar_reg():
        seleccion = lista_reg.selection()
        if seleccion:
            id_select = lista_reg.item(seleccion,"values")[0]

            nuevo_id=entPro_id.get()
            nuevo_nombre=entPro_nombre.get()
            nuevo_stock=entPro_stock.get()
            nuevo_precio=entPro_precio.get()
            nuevo_idcat=entPro_idcategoria.get()

            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                try:
                    cursor.execute("UPDATE producto SET idpro=?,nombre=?,stock=?,precio=?,idcat=? where idpro=?",
                                    (nuevo_id,nuevo_nombre,nuevo_stock,nuevo_precio,nuevo_idcat,id_select))
                    conn.commit()
                    mostrar_reg()
                    messagebox.showinfo("✔","Producto Modificado")
                except sqlite3.Error as e:
                    messagebox.showerror("❌",f"No se pudo modificar: {e}")

    vPro = ctk.CTkToplevel(ventana)
    vPro.title("Producto")
    vPro.resizable(False,False)
    vPro.geometry("1000x850")

    lblPro_id = ctk.CTkLabel(vPro,text="ID")
    lblPro_id.grid(row=0,column=0,padx=10,pady=10)
    entPro_id = ctk.CTkEntry(vPro)
    entPro_id.grid(row=0,column=1)

    lblPro_nombre = ctk.CTkLabel(vPro,text="Nombre")
    lblPro_nombre.grid(row=1,column=0,padx=10,pady=10)
    entPro_nombre = ctk.CTkEntry(vPro)
    entPro_nombre.grid(row=1,column=1)

    lblPro_stock = ctk.CTkLabel(vPro,text="Stock")
    lblPro_stock.grid(row=2,column=0,padx=10,pady=10)
    entPro_stock = ctk.CTkEntry(vPro)
    entPro_stock.grid(row=2,column=1)

    lblPro_precio = ctk.CTkLabel(vPro,text="Precio")
    lblPro_precio.grid(row=3,column=0,padx=10,pady=10)
    entPro_precio = ctk.CTkEntry(vPro)
    entPro_precio.grid(row=3,column=1)

    lblPro_idcategoria = ctk.CTkLabel(vPro,text="ID Categoria")
    lblPro_idcategoria.grid(row=4,column=0,padx=10,pady=10)
    entPro_idcategoria = ctk.CTkEntry(vPro)
    entPro_idcategoria.grid(row=4,column=1)

    bt_crear = ctk.CTkButton(vPro,text="Crear",command=crear_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_crear.grid(row=5,column=0,padx=10,pady=10)
    bt_eliminar = ctk.CTkButton(vPro,text="Eliminar",command=eliminar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_eliminar.grid(row=6,column=0,padx=10,pady=10)
    bt_modificar = ctk.CTkButton(vPro,text="Modificar",command=modificar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_modificar.grid(row=7,column=0,padx=10,pady=10)

    def ordenar_columna(tree, col, reverse):
        data = [ (tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for i, item in enumerate(data):
            tree.move(item[1], '', i)
        tree.heading(col, command=lambda: ordenar_columna(tree, col, not reverse))

    lista_reg = ttk.Treeview(vPro,columns=("ID","Nombre","Stock","Precio","ID Categoria"),show="headings",selectmode="browse")
    lista_reg.heading("ID",text="ID", command=lambda: ordenar_columna(lista_reg, "ID", False))
    lista_reg.heading("Nombre",text="Nombre", command=lambda: ordenar_columna(lista_reg, "Nombre", False))
    lista_reg.heading("Stock",text="Stock", command=lambda: ordenar_columna(lista_reg, "Stock", False))
    lista_reg.heading("Precio",text="Precio", command=lambda: ordenar_columna(lista_reg, "Precio", False))
    lista_reg.heading("ID Categoria",text="ID Categoria", command=lambda: ordenar_columna(lista_reg, "ID Categoria", False))
    lista_reg.column("ID",width=120)
    lista_reg.column("Nombre",width=120)
    lista_reg.column("Stock",width=120)
    lista_reg.column("Precio",width=120)
    lista_reg.column("ID Categoria",width=120)
    estilo=ttk.Style()
    estilo.configure("Treeview",background="#565b5e",foreground="white",rowheight=25)
    estilo.map("Treeview",background=[('selected','#6954a7')])
    lista_reg.grid(row=0, column=2, rowspan=6, padx=10, pady=10, sticky="nsew")
    scrollbar = Scrollbar(vPro, orient="vertical", command=lista_reg.yview)
    scrollbar.grid(row=0, column=3, rowspan=6, sticky="ns")
    lista_reg.configure(yscrollcommand=scrollbar.set)

    mostrar_reg()
    vPro.mainloop()

def vPed():
    def crear_reg():
        id_Ped = entPed_id.get()
        idcli_Ped = entPed_idcliente.get()
        idpro_Ped = entPed_idproducto.get()
        fecha_Ped = entPed_fecha.get()

        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO pedido (idped,idcli,idpro,fecha) VALUES (?,?,?,?)",(id_Ped,idcli_Ped,idpro_Ped,fecha_Ped))
            conn.commit()
            mostrar_reg()
            messagebox.showinfo("✔","Pedido Creado")

    def leer_reg():
        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pedido")
            registros = cursor.fetchall()
        return registros
    
    def mostrar_reg():
        lista_reg.delete(*lista_reg.get_children())
        for registro in leer_reg():
            lista_reg.insert("","end",values=registro)

    def eliminar_reg():
        seleccion = lista_reg.selection()
        if seleccion:

            id_seleccionado = lista_reg.item(seleccion, "values")[0]
            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                cursor.execute("DELETE FROM pedido WHERE idped = ?", id_seleccionado)
                conn.commit()
                mostrar_reg()
                messagebox.showinfo("✔", "Pedido Eliminado")

    def modificar_reg():
        seleccion = lista_reg.selection()
        if seleccion:
            id_select = lista_reg.item(seleccion,"values")[0]

            nuevo_id=entPed_id.get()
            nuevo_idcli=entPed_idcliente.get()
            nuevo_idprod=entPed_idproducto.get()
            nuevo_fecha=entPed_fecha.get()

            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                try:
                    cursor.execute("UPDATE pedido SET idped=?,idcli=?,idpro=?,fecha=? where idped=?",
                                    (nuevo_id,nuevo_idcli,nuevo_idprod,nuevo_fecha,id_select))
                    conn.commit()
                    mostrar_reg()
                    messagebox.showinfo("✔","Pedido Modificado")
                except sqlite3.Error as e:
                    messagebox.showerror("❌",f"No se pudo modificar: {e}")

    vPed = ctk.CTkToplevel(ventana)
    vPed.title("Pedido")
    vPed.resizable(False,False)
    vPed.geometry("1000x850")

    lblPed_id = ctk.CTkLabel(vPed,text="ID")
    lblPed_id.grid(row=0,column=0,padx=10,pady=10)
    entPed_id = ctk.CTkEntry(vPed)
    entPed_id.grid(row=0,column=1)

    lblPed_idcliente = ctk.CTkLabel(vPed,text="ID Cliente")
    lblPed_idcliente.grid(row=1,column=0,padx=10,pady=10)
    entPed_idcliente = ctk.CTkEntry(vPed)
    entPed_idcliente.grid(row=1,column=1)

    lblPed_idproducto = ctk.CTkLabel(vPed,text="ID Producto")
    lblPed_idproducto.grid(row=2,column=0,padx=10,pady=10)
    entPed_idproducto = ctk.CTkEntry(vPed)
    entPed_idproducto.grid(row=2,column=1)

    lblPed_fecha = ctk.CTkLabel(vPed,text="Fecha")
    lblPed_fecha.grid(row=3,column=0,padx=10,pady=10)
    entPed_fecha = ctk.CTkEntry(vPed)
    entPed_fecha.grid(row=3,column=1)

    bt_crear = ctk.CTkButton(vPed,text="Crear",command=crear_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_crear.grid(row=4,column=0,padx=10,pady=10)
    bt_eliminar = ctk.CTkButton(vPed,text="Eliminar",command=eliminar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_eliminar.grid(row=5,column=0,padx=10,pady=10)
    bt_modificar = ctk.CTkButton(vPed,text="Modificar",command=modificar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_modificar.grid(row=6,column=0,padx=10,pady=10)

    def ordenar_columna(tree, col, reverse):
        data = [ (tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for i, item in enumerate(data):
            tree.move(item[1], '', i)
        tree.heading(col, command=lambda: ordenar_columna(tree, col, not reverse))

    lista_reg = ttk.Treeview(vPed,columns=("ID","ID Cliente","ID Producto","Fecha"),show="headings",selectmode="browse")
    lista_reg.heading("ID",text="ID", command=lambda: ordenar_columna(lista_reg, "ID", False))
    lista_reg.heading("ID Cliente",text="ID Cliente", command=lambda: ordenar_columna(lista_reg, "ID Cliente", False))
    lista_reg.heading("ID Producto",text="ID Producto", command=lambda: ordenar_columna(lista_reg, "ID Producto", False))
    lista_reg.heading("Fecha",text="Fecha", command=lambda: ordenar_columna(lista_reg, "Fecha", False))
    lista_reg.column("ID",width=150)
    lista_reg.column("ID Cliente",width=150)
    lista_reg.column("ID Producto",width=150)
    lista_reg.column("Fecha",width=150)
    estilo=ttk.Style()
    estilo.configure("Treeview",background="#565b5e",foreground="white",rowheight=25)
    estilo.map("Treeview",background=[('selected','#6954a7')])
    lista_reg.grid(row=0, column=2, rowspan=6, padx=10, pady=10, sticky="nsew")
    scrollbar = Scrollbar(vPed, orient="vertical", command=lista_reg.yview)
    scrollbar.grid(row=0, column=3, rowspan=6, sticky="ns")
    lista_reg.configure(yscrollcommand=scrollbar.set)

    mostrar_reg()
    vPed.mainloop()

def vDet():
    def crear_reg():
        id_Det = entDet_id.get()
        idcli_Det = entDet_idcliente.get()
        idped_Det = entDet_idpedido.get()
        cantidad_Det = entDet_cantidad.get()

        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO detalle (iddet,idcli,idped,cantidad) VALUES (?,?,?,?)",(id_Det,idcli_Det,idped_Det,cantidad_Det))
            conn.commit()
            mostrar_reg()
            messagebox.showinfo("✔","Detalle Creado")

    def leer_reg():
        with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM detalle")
            registros = cursor.fetchall()
        return registros
    
    def mostrar_reg():
        lista_reg.delete(*lista_reg.get_children())
        for registro in leer_reg():
            lista_reg.insert("","end",values=registro)

    def eliminar_reg():
        seleccion = lista_reg.selection()
        if seleccion:

            id_seleccionado = lista_reg.item(seleccion, "values")[0]
            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                cursor.execute("DELETE FROM detalle WHERE iddet = ?", id_seleccionado)
                conn.commit()
                mostrar_reg()
                messagebox.showinfo("✔", "Detalle Eliminado")

    def modificar_reg():
        seleccion = lista_reg.selection()
        if seleccion:
            id_select = lista_reg.item(seleccion,"values")[0]

            nuevo_id=entDet_id.get()
            nuevo_idcli=entDet_idcliente.get()
            nuevo_idped=entDet_idpedido.get()
            nuevo_cantidad=entDet_cantidad.get()

            with sqlite3.connect("H2_SGE_1T_AitorBarriosGarcia.db") as conn:
                cursor = conn.cursor()

                try:
                    cursor.execute("UPDATE detalle SET iddet=?,idcli=?,idped=?,cantidad=? where iddet=?",
                                    (nuevo_id,nuevo_idcli,nuevo_idped,nuevo_cantidad,id_select))
                    conn.commit()
                    mostrar_reg()
                    messagebox.showinfo("✔","Pedido Modificado")
                except sqlite3.Error as e:
                    messagebox.showerror("❌",f"No se pudo modificar: {e}")

    vDet = ctk.CTkToplevel(ventana)
    vDet.title("Detalle")
    vDet.resizable(False,False)
    vDet.geometry("1000x850")

    lblDet_id = ctk.CTkLabel(vDet,text="ID")
    lblDet_id.grid(row=0,column=0,padx=10,pady=10)
    entDet_id = ctk.CTkEntry(vDet)
    entDet_id.grid(row=0,column=1)

    lblDet_idcliente = ctk.CTkLabel(vDet,text="ID Cliente")
    lblDet_idcliente.grid(row=1,column=0,padx=10,pady=10)
    entDet_idcliente = ctk.CTkEntry(vDet)
    entDet_idcliente.grid(row=1,column=1)

    lblDet_idpedido = ctk.CTkLabel(vDet,text="ID Pedido")
    lblDet_idpedido.grid(row=2,column=0,padx=10,pady=10)
    entDet_idpedido = ctk.CTkEntry(vDet)
    entDet_idpedido.grid(row=2,column=1)

    lblDet_cantidad = ctk.CTkLabel(vDet,text="Cantidad")
    lblDet_cantidad.grid(row=3,column=0,padx=10,pady=10)
    entDet_cantidad = ctk.CTkEntry(vDet)
    entDet_cantidad.grid(row=3,column=1)

    bt_crear = ctk.CTkButton(vDet,text="Crear",command=crear_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_crear.grid(row=4,column=0,padx=10,pady=10)
    bt_eliminar = ctk.CTkButton(vDet,text="Eliminar",command=eliminar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_eliminar.grid(row=5,column=0,padx=10,pady=10)
    bt_modificar = ctk.CTkButton(vDet,text="Modificar",command=modificar_reg, fg_color="#565b5e", hover_color="#6954a7")
    bt_modificar.grid(row=6,column=0,padx=10,pady=10)

    def ordenar_columna(tree, col, reverse):
        data = [ (tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for i, item in enumerate(data):
            tree.move(item[1], '', i)
        tree.heading(col, command=lambda: ordenar_columna(tree, col, not reverse))

    lista_reg = ttk.Treeview(vDet,columns=("ID","ID Cliente","ID Pedido","Cantidad"),show="headings",selectmode="browse")
    lista_reg.heading("ID",text="ID", command=lambda: ordenar_columna(lista_reg, "ID", False))
    lista_reg.heading("ID Cliente",text="ID Cliente", command=lambda: ordenar_columna(lista_reg, "ID Cliente", False))
    lista_reg.heading("ID Pedido",text="ID Pedido", command=lambda: ordenar_columna(lista_reg, "ID Pedido", False))
    lista_reg.heading("Cantidad",text="Cantidad", command=lambda: ordenar_columna(lista_reg, "Cantidad", False))
    lista_reg.column("ID",width=150)
    lista_reg.column("ID Cliente",width=150)
    lista_reg.column("ID Pedido",width=150)
    lista_reg.column("Cantidad",width=150)
    estilo=ttk.Style()
    estilo.configure("Treeview",background="#565b5e",foreground="white",rowheight=25)
    estilo.map("Treeview",background=[('selected','#6954a7')])
    lista_reg.grid(row=0, column=2, rowspan=6, padx=10, pady=10, sticky="nsew")
    scrollbar = Scrollbar(vDet, orient="vertical", command=lista_reg.yview)
    scrollbar.grid(row=0, column=3, rowspan=6, sticky="ns")
    lista_reg.configure(yscrollcommand=scrollbar.set)

    mostrar_reg()
    vDet.mainloop()

def vBus():
    def buscar_reg():
        id_det = ent_IDBUS.get()

        my_conn = sqlite3.connect('H2_SGE_1T_AitorBarriosGarcia.db')
        cursor = my_conn.execute('''SELECT detalle.iddet, cliente.nombre, cliente.direccion, pedido.fecha, detalle.cantidad FROM detalle INNER JOIN cliente ON detalle.idcli = cliente.idcli INNER JOIN pedido ON detalle.idped = pedido.idped WHERE detalle.iddet = ?''', (id_det,))

        i = 1
        for registro in cursor:
            for j in range(len(registro)):
                e = Entry(vBus, width=10, fg='blue')
                e.grid(row=i, column=j+1)
                e.insert(END, registro[j])
            i = i + 1

    vBus = ctk.CTkToplevel(ventana)
    vBus.title("Busqueda")
    vBus.resizable(False, False)
    vBus.geometry("1000x850")

    lbl_IDBUS = ctk.CTkLabel(vBus, text="Dime el ID del Detalle para buscar:", font=("Algerian", 15))
    lbl_IDBUS.grid(row=0, column=0, padx=10, pady=10)
    ent_IDBUS = ctk.CTkEntry(vBus)
    ent_IDBUS.grid(row=1, column=0, padx=10, pady=10)
    bt_IDBUS = ctk.CTkButton(vBus, text="Buscar", fg_color="#565b5e", hover_color="#6954a7", command=buscar_reg)
    bt_IDBUS.grid(row=2, column=0, padx=10, pady=10)
    lbl_id = ctk.CTkLabel(vBus,text="ID", font=("Algerian", 10))
    lbl_id.grid(row=0,column=1,columnspan=5)
    lbl_cli = ctk.CTkLabel(vBus,text="Cliente", font=("Algerian", 10))
    lbl_cli.grid(row=0,column=2,columnspan=5)
    lbl_direc = ctk.CTkLabel(vBus,text="Direccion", font=("Algerian", 10))
    lbl_direc.grid(row=0,column=3,columnspan=5)
    lbl_fecha = ctk.CTkLabel(vBus,text="Fecha", font=("Algerian", 10))
    lbl_fecha.grid(row=0,column=4,columnspan=5)
    lbl_cant = ctk.CTkLabel(vBus,text="Cantidad", font=("Algerian", 10))
    lbl_cant.grid(row=0,column=5,columnspan=5)

    vBus.mainloop()

def vGra1():

    dataframe = pd.read_excel("H2_SGE_1T_AitorBarriosGarcia.xlsx",sheet_name="producto")

    datos = dataframe.iloc[1:,2]
    productos = dataframe.iloc[1:,2]


    fig, ax = plt.subplots()

    ax.set_xlabel('Productos')
    ax.set_ylabel('Cantidad de Stock')
    ax.bar(productos,datos)
    plt.show()

def vGra2():

    dataframe = pd.read_excel("H2_SGE_1T_AitorBarriosGarcia.xlsx",sheet_name="pedido")

    datos = dataframe.iloc[1:,2]
    productos = dataframe.iloc[1:,2]


    fig, ax = plt.subplots()

    ax.set_xlabel('Productos')
    ax.set_ylabel('Cantidad de Stock')
    ax.bar(productos,datos)
    plt.show()

def vGra3():

    dataframe = pd.read_excel("H2_SGE_1T_AitorBarriosGarcia.xlsx",sheet_name="pedido")

    datos = dataframe.iloc[1:,2]
    productos = dataframe.iloc[1:,2]


    fig, ax = plt.subplots()

    ax.set_xlabel('Productos')
    ax.set_ylabel('Cantidad de Stock')
    ax.bar(productos,datos)
    plt.show()


def exportar():
    conn = sqlite3.connect('H2_SGE_1T_AitorBarriosGarcia.db')

    tablas = ['categoria', 'cliente', 'producto', 'pedido', 'detalle']

    archivo_excel = 'H2_SGE_1T_AitorBarriosGarcia.xlsx'

    with pd.ExcelWriter(archivo_excel, engine='xlsxwriter') as writer:
        for tabla in tablas:
            query = f'SELECT * FROM {tabla}'
            
            df = pd.read_sql_query(query, conn)
            
            df.to_excel(writer, sheet_name=tabla, index=False)

    conn.close()

    print(f'Datos exportados exitosamente a {archivo_excel}')
    messagebox.showinfo("✔","Datos exportados")


lbl_TITULO = ctk.CTkLabel(ventana,text="BIENVENIDO A SUPERBARRIOS",font=("Algerian",25))
lbl_TITULO.grid(row=0,column=0,padx=10,pady=10)
lbl_SUBTITULO = ctk.CTkLabel(ventana,text="Esta aplicación le permitirá gestionar su tienda SuperBarrios",font=("Algerian",15))
lbl_SUBTITULO.grid(row=1,column=0,padx=10,pady=10)

bt_CATEGORIA = ctk.CTkButton(ventana, height=125, width=125,text="", command=vCat, fg_color='#9be3c7', hover_color="#FFFFFF",image=cat)#
bt_CATEGORIA.grid(row=1,column=1, padx=10, pady=10)
lbl_CATEGORIA = ctk.CTkLabel(ventana,text="Categoría", font=("Algerian",15))
lbl_CATEGORIA.grid(row=2,column=1, padx=10,pady=10)

bt_CLIENTE = ctk.CTkButton(ventana, height=125, width=125,text="", command=vCli, fg_color='#9be3c7', hover_color="#FFFFFF",image=cli)#
bt_CLIENTE.grid(row=1,column=2, padx=10, pady=10)
lbl_CLIENTE = ctk.CTkLabel(ventana,text="Cliente", font=("Algerian",15))
lbl_CLIENTE.grid(row=2,column=2, padx=10,pady=10)

bt_PRODUCTO = ctk.CTkButton(ventana, height=125, width=125,text="", command=vPro, fg_color='#9be3c7', hover_color="#FFFFFF",image=pro)#
bt_PRODUCTO.grid(row=1,column=3, padx=10, pady=10)
lbl_PRODUCTO = ctk.CTkLabel(ventana,text="Producto", font=("Algerian",15))
lbl_PRODUCTO.grid(row=2,column=3, padx=10,pady=10)

bt_PEDIDO = ctk.CTkButton(ventana, height=125, width=125,text="", command=vPed, fg_color='#9be3c7', hover_color="#FFFFFF",image=ped)#
bt_PEDIDO.grid(row=3,column=1, padx=10, pady=10)
lbl_PEDIDO = ctk.CTkLabel(ventana,text="Pedido", font=("Algerian",15))
lbl_PEDIDO.grid(row=4,column=1, padx=10,pady=10)

bt_DETALLE = ctk.CTkButton(ventana, height=125, width=125,text="", command=vDet, fg_color='#9be3c7', hover_color="#FFFFFF",image=det)#
bt_DETALLE.grid(row=3,column=2, padx=10, pady=10)
lbl_DETALLE = ctk.CTkLabel(ventana,text="Detalle", font=("Algerian",15))
lbl_DETALLE.grid(row=4,column=2, padx=10,pady=10)

bt_BUSQUEDA = ctk.CTkButton(ventana, height=125, width=125,text="", command=vBus, fg_color='#9be3c7', hover_color="#FFFFFF",image=bus)#
bt_BUSQUEDA.grid(row=3,column=3, padx=10, pady=10)
lbl_BUSQUEDA = ctk.CTkLabel(ventana,text="Busqueda", font=("Algerian",15))
lbl_BUSQUEDA.grid(row=4,column=3, padx=10,pady=10)

bt_GRAFICO = ctk.CTkButton(ventana, height=125, width=125,text="", command=vGra1, fg_color='#9be3c7', hover_color="#FFFFFF",image=gra)#
bt_GRAFICO.grid(row=5,column=1, padx=10, pady=10)
lbl_GRAFICO = ctk.CTkLabel(ventana,text="Grafico 1", font=("Algerian",15))
lbl_GRAFICO.grid(row=6,column=1, padx=10,pady=10)

bt_GRAFICO2 = ctk.CTkButton(ventana, height=125, width=125,text="", command=vGra2, fg_color='#9be3c7', hover_color="#FFFFFF",image=gra)#
bt_GRAFICO2.grid(row=5,column=2, padx=10, pady=10)
lbl_GRAFICO2 = ctk.CTkLabel(ventana,text="Grafico 2", font=("Algerian",15))
lbl_GRAFICO2.grid(row=6,column=2, padx=10,pady=10)

bt_GRAFICO3 = ctk.CTkButton(ventana, height=125, width=125,text="", command=vGra3, fg_color='#9be3c7', hover_color="#FFFFFF",image=gra)#
bt_GRAFICO3.grid(row=5,column=3, padx=10, pady=10)
lbl_GRAFICO3 = ctk.CTkLabel(ventana,text="Grafico 3", font=("Algerian",15))
lbl_GRAFICO3.grid(row=6,column=3, padx=10,pady=10)

bt_EXPORTAR = ctk.CTkButton(ventana, height=125, width=125,text="", command=exportar, fg_color='#9be3c7', hover_color="#FFFFFF",image=exl)#
bt_EXPORTAR.grid(row=7,column=1, padx=10, pady=10)
lbl_EXPORTAR = ctk.CTkLabel(ventana,text="Exportar", font=("Algerian",15))
lbl_EXPORTAR.grid(row=8,column=1, padx=10,pady=10)


ventana.mainloop()