import shutil
import os
import getpass
import time
def menu():
    print("1. Instalar Mod")
    print("2. Restaurar partida guardada")
    print("3. Respaldar partida guardada")
    print("4. Salir")
menu()
option = input("Seleccione una opción: ")
if option == "1":
    os.system("cls")
    # TODO: hacer que la carpeta de www_vanilla se renombre a www para evitar errores, ahora mismo lo haria pero me da pereza...
    game_dir = input("Por favor indique el directorio de su juego: (Por ejemplo: C:/juegos/SMC 1.x.x.x x64/x64/): ")
    mod_dir = input("Por favor indique el directorio de su mod: ")
    print("Instalando mod...")
    os.chdir(game_dir)
    os.rename("www", "www_vanilla")
    time.sleep(2) # sinceramente esto es lo unico que se me ocurrio para arreglarlo
    shutil.copytree(mod_dir, "www")
    print("Mod instalado correctamente.")
elif option == "2":
    os.system("cls")
    # TODO: lo mismo que en lo de instalar mods
    print("Restaurando partida guardada...")
    shutil.copytree(os.getcwd() + "/backup/IndexedDB", "C:/Users/" + getpass.getuser() + "/AppData/Local/Super Momos Crushers/EBWebView/Default/IndexedDB")
    print("Partida guardada restaurada correctamente.")
elif option == "3":
    os.system("cls")
    print("Respaldando partida guardada...")
    # TODO: lo mismo que en los 2 comentarios de arriba
    shutil.copytree("C:/Users/" + getpass.getuser() + "/AppData/Local/Super Momos Crushers/EBWebView/Default/IndexedDB", os.getcwd() + "/backup/IndexedDB")
    print("Partida guardada respaldada correctamente.")
elif option == "4":
    exit()    