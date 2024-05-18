
# cores

cor1 = "#3b3b3b"  # preta
cor2 = "#feffff"   # branca
cor3 = "#38576b"   # Azul escuro
cor4 = "#ECEFF1"   # Cinza
cor5 = "#FFAB40"   # Laranja
cor6 = "#3a403f"
janela = Tk()
janela.title("Calculadora")
janela.geometry("320x427")
janela.config(bg=cor1)


# Frames

frame_tela = Frame(janela, width=320, height=71, bg=cor6)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=320, height=355, bg=cor4)
frame_corpo.grid(row=1, column=0)


# Variavel valores
todos_valores = ''

# Label de resultado
valor_texto = StringVar()

# def de calculo

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #resultado printado na calculadora
    valor_texto.set(todos_valores)


# Função de Calculo

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""
    

# Função para limpar Tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 16'), bg=cor6, fg=cor2)
app_label.place(x=105, y= 10)


# Botoes
# Linha 1
b_1 = Button(frame_corpo, command = lambda: limpar_tela(), text="C", width=15, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=160, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=240, y=0)

# Linha 2
b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=71)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=80, y=71)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=71)
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="*", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=240, y=71)

# Linha 3 
b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=143)
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=80, y=143)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=160, y=143)
b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=240, y=143)

# Linha 4
b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=214)
b_13 = Button(frame_corpo,  command = lambda: entrar_valores('2'),text="2", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=80, y=214)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=160, y=214)
b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'),text="+", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=240, y=214)

# Linha 4
b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=15, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=285)
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=7, height=3, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=160, y=285)
b_18 = Button(frame_corpo, command = lambda: calcular(), text="=", width=7, height=3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=240, y=285)



janela.mainloop()
