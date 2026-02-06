import platform
import serial
import subprocess
import pyautogui
import time
import webbrowser

def escribirTexto(texto = ""):
    time.sleep(0.5)  # tiempo para enfocar la ventana
    pyautogui.write(texto, interval=0.05) 

def correrPrograma(programa = ""):
    subprocess.Popen([programa])

def abrirPaginaWeb(pagina = ""):
    webbrowser.open(pagina)

os_name = platform.system()

if os_name == "Linux":
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    print("Linux")
else:
    raise RuntimeError("Unsupported OS")

dato = None

while dato != 255:
    dato = ser.read(1)  # convert byte to int
    print("Received:", dato)

ser.close()
print("Serial closed")


def correrMacros(macro = 0, modo = 0):
    if modo == 1:
        match macro:        
            #--------------------------------------------------------------#
            #General Macros                                                #
            #--------------------------------------------------------------#
            case "0":
                correrPrograma("firefox")                   #Navegador
            case "1":
                pyautogui.hotkey("win", "e")                #Files
            case "2":
                print("Calculadora")                        #Calculadora
            case "3":
                print("Musica")                             #Musica

            #---------------------------------------------------------------#
            #Dev Macros                                                     #
            #---------------------------------------------------------------#
            case "4":
                correrPrograma("code")                      #Vs Code
            case "5":
                pyautogui.hotkey("ctrl", "alt", "t")        #Terminal
            case "6":
                abrirPaginaWeb("chatgpt.com")               #ChatGPT
            case "7":
                abrirPaginaWeb("github.com")                #Github

            #---------------------------------------------------------------#
            #Web Macros                                                     #
            #---------------------------------------------------------------#       
            case "8":
                abrirPaginaWeb("google.com")                #Google
            case "9":
                abrirPaginaWeb("youtube.com")               #Youtube
            case "A":
                abrirPaginaWeb("amazon.com")                #Amazon
            case "B":
                abrirPaginaWeb("reddit.com")                #Reddit

            #---------------------------------------------------------------#
            #Sistema Macros                                                 #
            #---------------------------------------------------------------#       
            case "C":
                pyautogui.hotkey("printscreen")             #Captura de Pantalla
            case "D":
                pyautogui.hotkey("win",  "d")               #Mostrar esctritorio
            case "#":
                print("Modo Siguiente")
            case "*":
                print("Modo Anterior")
            case _:
                escribirTexto("Opcion Invalida - Revise la comunicacion serial")
    
    elif modo == 2:
        match macro:        
            #--------------------------------------------------------------#
            #General Macros                                                #
            #--------------------------------------------------------------#
            case "0":
                pyautogui.hotkey("ctrl", "c")
            case "1":
                pyautogui.hotkey("ctrl", "v")
            case "2":
                pyautogui.hotkey("ctrl", "x")
            case "3":
                pyautogui.hotkey("ctrl", "f")

            #---------------------------------------------------------------#
            #Dev Macros                                                     #
            #---------------------------------------------------------------#
            case "4":
                pyautogui.hotkey("ctrl", "r")
            case "5":
                print("En desarrollo")
            case "6":
                print("En desarrollo")
            case "7":
                print("En desarrollo")

            #---------------------------------------------------------------#
            #Web Macros                                                     #
            #---------------------------------------------------------------#       
            case "8":
                print("En desarrollo")
            case "9":
                print("En desarrollo")
            case "A":
                print("En desarrollo")
            case "B":
                print("En desarrollo")

            #---------------------------------------------------------------#
            #Sistema Macros                                                 #
            #---------------------------------------------------------------#       
            case "C":
                print("En desarrollo")
            case "D":
                print("En desarrollo")
            case "#":
                print("Modo Siguiente")
            case "*":
                print("Modo Anterior")
            case _:
                escribirTexto("Opcion Invalida - Revise la comunicacion serial")

