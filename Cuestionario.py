from tkinter import *
root = Tk()
root.title("Preguntas de países")
root.iconbitmap("koala.ico")
root.geometry("400x400")
root.resizable(0,0)

#-----COLECTOR DE RESPUESTAS-----
respuestas_elegidas = {"r1":0, "r2":0, "r3":0}
respuestas_correctas = {"r1":3, "r2":1, "r3":4}

#-----ACOMODO DE FILAS Y COLUMNAS-----
for i in range(6): #cantidad de filas ≡
    root.grid_rowconfigure(i, weight=1)
for j in range(6): #cantidad de columnas ---
    root.grid_columnconfigure(j, weight=1)

#-----FUNCIONES-----
def vaciar_root():  
    minombre = entrada_nombre.get()
    if entrada_nombre.get() != "":
        label_nombre.destroy()
        label_bienvenido.destroy()
        entrada_nombre.destroy()
        boton_start.destroy()
        label_explicacion.config(text= f"""Hola {minombre}!
A continuación se realizarán
preguntas sobre las capitales
de países, suerte!""", font=("Monotype Corsiva", 24), borderwidth=5, relief="groove", bg="black", fg="yellow")
        label_explicacion.grid(row=1, column=1, columnspan=4)
        boton2.place(x=170, y=320)

def vaciar_2daP():
    label_explicacion.destroy()
    boton2.destroy()
    pregunta1.grid(row=0, column=2, columnspan=3)
    for i in range(1,5): #cantidad de filas ≡
        root.grid_rowconfigure(i, weight=0)
    respuesta1.grid(row=1, column=3, sticky="ew")
    respuesta2.grid(row=2, column=3, sticky="ew")
    respuesta3.grid(row=3, column=3, sticky="ew")
    respuesta4.grid(row=4, column=3, sticky="ew")
    boton3.place(x=170, y=320)

def vaciar_3raP():
    capturar_respuesta()
    pregunta1.destroy()
    boton3.destroy()
    pregunta2.grid(row=0, column=2, columnspan=3)
    for i in range(1,5): #cantidad de filas ≡
        root.grid_rowconfigure(i, weight=0)
    respuesta1.destroy()
    respuesta2.destroy()
    respuesta3.destroy()
    respuesta4.destroy()    
    respuesta5.grid(row=1, column=3, sticky="ew")
    respuesta6.grid(row=2, column=3, sticky="ew")
    respuesta7.grid(row=3, column=3, sticky="ew")
    respuesta8.grid(row=4, column=3, sticky="ew")
    boton4.place(x=170, y=320)    

def vaciar_4taP():
    capturar_respuesta2()
    pregunta2.destroy()
    boton4.destroy()
    respuesta5.destroy()
    respuesta6.destroy()
    respuesta7.destroy()
    respuesta8.destroy()
    pregunta3.grid(row=0, column=2, columnspan=3)
    for i in range(1,5): #cantidad de filas ≡
        root.grid_rowconfigure(i, weight=0)
    respuesta9.grid(row=1, column=3, sticky="ew")
    respuesta10.grid(row=2, column=3, sticky="ew")
    respuesta11.grid(row=3, column=3, sticky="ew")
    respuesta12.grid(row=4, column=3, sticky="ew")
    boton_resultados.place(x=120, y=320)

def ver_resultados():
    capturar_respuesta3()
    pregunta3.destroy()
    boton_resultados.destroy()
    respuesta9.destroy()
    respuesta10.destroy()
    respuesta11.destroy()
    respuesta12.destroy()
    root.grid_rowconfigure(1, weight=1)
    label_resultado.grid(row=0, column=2, columnspan=2)
    aciertos2 = suma_resultados()
    label_resultado2.config(text=f"Has acertado {aciertos2} !")
    label_resultado2.grid(row=1, column=2, columnspan=2)
    label_respuesta1.grid(row=2, column=2, columnspan=2)
    label_respuesta2.grid(row=3, column=2, columnspan=2)
    label_respuesta3.grid(row=4, column=2, columnspan=2)
    
    if respuestas_elegidas["r1"] == respuestas_correctas["r1"]:
        label_respuesta1.config(bg="green")
    else:
        label_respuesta1.config(bg="red")
    if respuestas_elegidas["r2"] == respuestas_correctas["r2"]:
        label_respuesta2.config(bg="green")
    else:
        label_respuesta2.config(bg="red")
    if respuestas_elegidas["r3"] == respuestas_correctas["r3"]:
        label_respuesta3.config(bg="green")
    else:
        label_respuesta3.config(bg="red")
    
def capturar_respuesta():
    if seleccion.get() == 1:
        respuestas_elegidas["r1"] = 1
    elif seleccion.get() == 2:
        respuestas_elegidas["r1"] = 2
    elif seleccion.get() == 3:
        respuestas_elegidas["r1"] = 3
    elif seleccion.get() == 4:
        respuestas_elegidas["r1"] = 4
    else:
        pass
        
def capturar_respuesta2():
    if seleccion2.get() == 1:
        respuestas_elegidas["r2"] = 1
    elif seleccion2.get() == 2:
        respuestas_elegidas["r2"] = 2
    elif seleccion2.get() == 3:
        respuestas_elegidas["r2"] = 3
    elif seleccion2.get() == 4:
         respuestas_elegidas["r1"] = 4
    else:
         pass

def capturar_respuesta3():
    if seleccion3.get() == 1:
        respuestas_elegidas["r3"] = 1
    elif seleccion3.get() == 2:
        respuestas_elegidas["r3"] = 2
    elif seleccion3.get() == 3:
        respuestas_elegidas["r3"] = 3
    elif seleccion3.get() == 4:
         respuestas_elegidas["r1"] = 4
    else:
         pass

def salir():
    root.destroy()    
    
#-----INTRO-----
frame_de_imagen = Frame(root)
frame_de_imagen.place(x=1, y=1)

imagen = PhotoImage(file="fondo3.png")
label_imagen = Label(frame_de_imagen,image=imagen)
label_imagen.pack()

label_bienvenido = Label(root, text = "Bienvenido!",bg="black", fg="yellow", font=("Monotype Corsiva", 24), borderwidth=5, relief="groove")
label_bienvenido.grid(row=1, column=2, columnspan=2)

label_nombre = Label(root, text = "Ingresa tu nombre:", bg="black", fg="yellow", font=("Monotype Corsiva", 16), borderwidth=5, relief="groove")
label_nombre.grid(row=3, column=2, columnspan=2)

entrada_nombre = Entry(root, font=("Monotype Corsiva", 16), justify=CENTER)
entrada_nombre.grid(row=4, column=2, columnspan=2)

boton_start = Button(root, text = "►", bg="black", fg="yellow", font=("Arial", 24), command=vaciar_root)
boton_start.grid(row=5, column=2, columnspan=2)

boton_salir = Button(root, text = "Salir", bg="green", fg="yellow", font=("Arial", 16), command=salir)
boton_salir.place(x=331, y=350)

#------1ra PANTALLA-----
label_explicacion = Label(root)
label_explicacion.place_forget()

boton2 = Button(root, text = "►", bg="black", fg="yellow", font=("Arial", 24), command=vaciar_2daP)
boton2.place_forget()

#------2da Pantalla / Primera Pregunta
seleccion = IntVar()

pregunta1 = Label(root, text= "Cuál es la capital de Marruecos?")
pregunta1.config(font=("Monotype Corsiva", 24), borderwidth=5, relief="groove", bg="black", fg="yellow")
pregunta1.place_forget()

respuesta1 = Radiobutton(root, text = "Nicosia", variable = seleccion, value = 1)
respuesta1.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta1.grid_forget()

respuesta2 = Radiobutton(root, text = "Zagreb", variable = seleccion, value = 2)
respuesta2.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta2.grid_forget()

respuesta3 = Radiobutton(root, text = "Rabat", variable = seleccion, value = 3)
respuesta3.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta3.grid_forget()

respuesta4 = Radiobutton(root, text = "Saint George", variable = seleccion, value = 4)
respuesta4.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta4.grid_forget()

boton3 = Button(root, text = "►", bg="black", fg="yellow", font=("Arial", 24), command=vaciar_3raP)
boton3.place_forget()

#-----3RA PANTALLA / 2DA PREGUNTA -----
seleccion2 = IntVar()

pregunta2 = Label(root, text= "Cuál es la capital de Indonesia?")
pregunta2.config(font=("Monotype Corsiva", 24), borderwidth=5, relief="groove", bg="black", fg="yellow")
pregunta2.place_forget()

respuesta5 = Radiobutton(root, text = "Yakarta", variable = seleccion2, value = 1)
respuesta5.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta5.grid_forget()

respuesta6 = Radiobutton(root, text = "Sri Lanka", variable = seleccion2, value = 2)
respuesta6.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta6.grid_forget()

respuesta7 = Radiobutton(root, text = "Kingston", variable = seleccion2, value = 3)
respuesta7.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta7.grid_forget()

respuesta8 = Radiobutton(root, text = "El Cairo", variable = seleccion2, value = 4)
respuesta8.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta8.grid_forget()

boton3 = Button(root, text = "►", bg="black", fg="yellow", font=("Arial", 24), command=vaciar_3raP)
boton3.place_forget()

#-----3RA PANTALLA / 2DA PREGUNTA -----
seleccion3 = IntVar()

pregunta3 = Label(root, text= "Cuál es la capital de Nepal?")
pregunta3.config(font=("Monotype Corsiva", 24), borderwidth=5, relief="groove", bg="black", fg="yellow")
pregunta3.place_forget()

respuesta9 = Radiobutton(root, text = "Praga", variable = seleccion3, value = 1)
respuesta9.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta9.grid_forget()

respuesta10 = Radiobutton(root, text = "Lisboa", variable = seleccion3, value = 2)
respuesta10.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta10.grid_forget()

respuesta11 = Radiobutton(root, text = "Belgrado", variable = seleccion3, value = 3)
respuesta11.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta11.grid_forget()

respuesta12 = Radiobutton(root, text = "Katmandú", variable = seleccion3, value = 4)
respuesta12.config(font=("Monotype Corsiva", 18),bg="#D8D8D8")
respuesta12.grid_forget()

boton4 = Button(root, text = "►", bg="black", fg="yellow", font=("Arial", 24), command=vaciar_4taP)
boton4.place_forget()

#-----PANTALLA FINAL----

boton_resultados = Button(root, text = "Ver resultados", bg="black", fg="yellow", font=("Arial", 16), command=ver_resultados)
boton4.place_forget()

label_resultado = Label(root, text= "Resultados:")
label_resultado.config(font=("Monotype Corsiva", 24), borderwidth=5, relief="groove", bg="black", fg="yellow")
label_resultado.place_forget()

def suma_resultados():
    aciertos = 0
    if respuestas_elegidas["r1"] == respuestas_correctas["r1"]:
        aciertos += 1
    if respuestas_elegidas["r2"] == respuestas_correctas["r2"]:
        aciertos += 1
    if respuestas_elegidas["r3"] == respuestas_correctas["r3"]:
        aciertos += 1
    return aciertos

label_resultado2 = Label(root, text= "")
label_resultado2.config(font=("Monotype Corsiva", 24), borderwidth=5, relief="groove", bg="black", fg="yellow")

label_respuesta1 = Label(root, text="Marruecos: Rabat")
label_respuesta1.config(font=("Monotype Corsiva", 16), borderwidth=5, relief="groove", bg="black", fg="yellow", width=20)
label_respuesta1.grid_forget()

label_respuesta2 = Label(root, text="Indonesia: Yakarta")
label_respuesta2.config(font=("Monotype Corsiva", 16), borderwidth=5, relief="groove", bg="black", fg="yellow", width=20)
label_respuesta2.grid_forget()

label_respuesta3 = Label(root, text="Nepal: Katmandú")
label_respuesta3.config(font=("Monotype Corsiva", 16), borderwidth=5, relief="groove", bg="black", fg="yellow", width=20)
label_respuesta3.grid_forget()

root.mainloop()







