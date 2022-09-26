import os
import subprocess
import time
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import tkinter.font as font
import json


with open("test.json", encoding='utf-8') as meu_json:
    app = json.load(meu_json)

aplicativos = (list(app["PROGRAMA"]))


def enviar():
    endereco = ip.get()
    programa = combo.get()
    
    s = subprocess.Popen(["ping.exe", "-n","1",endereco],stdout = subprocess.PIPE,shell =True).communicate()[0]

    if b'Verifique o nome' in s:
        ipativo.config(text =".", font=("Times New Roman", 50), foreground="red")


    elif b'Esgotado o tempo limite do pedido' in s:
        ipativo.config(text =".", font=("Times New Roman", 50), foreground="red")


    elif b'Falha geral' in s:
        ipativo.config(text =".", font=("Times New Roman", 50), foreground="red")


    else:
        ipativo.config(text =".", font=("Times New Roman", 50), foreground="#28F82B")

        #Puxar a tabela
        aplicativos = (dict(app["PROGRAMA"]))
        infor = (dict(aplicativos[programa]))
        #Pegar informações necessarias
        aplic = (infor["endereco"])
        aplic = aplic.replace("/", "\\")
        #enviar Programa
        enviar = ('start Xcopy "%s" "\\\%s\C$\Windows\Temp\" /Y' %(aplic, endereco))
        os.system(enviar)
        data = datetime.now()
        textf.insert(END, '''Time.: %s \nComando.: "%s" \n''' %(data, enviar))

def executa():
    endereco = ip.get()
    programa = combo.get()
    
    aplicativos = (dict(app["PROGRAMA"]))
    infor = (dict(aplicativos[programa]))
    #executar Programa
    exe = (infor["executa"])
    exe = exe.replace("/", "\\")
    executar = ('start Psexec.exe \\\%s "c:\Windows\Temp\%s" ' %(endereco, exe))
    os.system(executar)
    data = datetime.now()
    textf.insert(END,'''Time.: %s \nComando.: "%s" \n''' %(data, executar))

def info():
    programa = combo.get()
    #Puxar a tabela
    aplicativos = (dict(app["PROGRAMA"]))
    infor = (dict(aplicativos[programa]))
    #Pegar informações necessarias
    ser = (infor["serviço"])
    inf = (infor["informacao"])
    #executar Pesquisa
    conhecimento = ('start %s' %(inf))
    os.system(conhecimento)
    data = datetime.now()
    textf.insert(END, '''Time.: %s \nComando.: "%s" \n''' %(data, conhecimento))
    

    

root = Tk()
root.title('AUTO INSTALADOR')
root.minsize(350,400)
root.maxsize(350,400)
root.configure(background="#71a6ff")

myFont = font.Font(family='Arial', size=10, weight='bold')

#######################################################
label1 = Label(root,text = "IP / NOMENCLATURA.:", font=(myFont), bg="#71a6ff").place(x=40, y=45)
ip = Entry(root, bg="white", font=(myFont))
ip.pack()
ip.place(x=40, y=75, width=250,height=20)

ipativo = Label(root, bg="#71a6ff")
ipativo.pack()
ipativo.place(x=295, y=25)

label2 = Label(root,text = "PROGRAMA.:", font=(myFont), bg="#71a6ff").place(x=40, y=110)
combo = Combobox(root, font=(myFont))
combo['values']=(aplicativos)
combo.current(1)
combo.pack()
combo.place(x=40, y=140, width=250,height=20)

buton1 = Button(root, text=" ENVIAR  ", font=(myFont), command= enviar)
buton1.pack()
buton1.place(x=60, y=180)

buton2 = Button(root, text="EXECUTAR", font=(myFont), command= executa)
buton2.pack()
buton2.place(x=200, y=180)

buton3 = Button(root, text="BASE DE CONHECIMENTO", font=(myFont), command= info)
buton3.pack()
buton3.place(x=80, y=250)

textf = Text(root, height=5, width=47, font=(("Arial"),10))
textf.pack()
textf.place(x=9, y=310)

root.mainloop()

