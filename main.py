import os
import subprocess
import sys

try:

    def check_adb_exists():
        try:
            result = subprocess.run(['adb', 'version'], capture_output=True, text=True)
            return True
        except FileNotFoundError:
            return False

    if not check_adb_exists():
        print("ADB n'est pas installé ou n'est pas accessible.")
        input("Appuyez sur Entrer pour quitter...")
        sys.exit()

    def check_devices_connected():
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        output = result.stdout.strip().split('\n')[1:]
        devices = [line.split('\t')[0] for line in output if line.strip()]
        return bool(devices)

    if not check_devices_connected():
        print("Aucun appareil n'a été trouvé. Veuillez connecter un appareil et/ou accepter le débogage USB, et réessayer.")
        input("Appuyez sur Entrer pour quitter...")
        sys.exit()    

    while True:
        response = input("Voulez-vous désinstaller Service d'impression par défaut ? [O/n] ")
        if response == '' or response == 'o' or response == 'O':
            print("Désinstallation de Service d'impression par défaut...")
            os.system('adb shell pm uninstall -k --user 0 com.android.bips')
            break
        elif response == 'n' or response == 'N':
            print("Passons...")
            break
        else:
            print("Entrée invalide.")
            
    while True:
        response = input("Voulez-vous désinstaller Mi Music ? [O/n] ")
        if response == '' or response == 'o' or response == 'O':
            print("Désinstallation de Mi Music...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.player')
            break
        elif response == 'n' or response == 'N':
            print("Passons...")
            break
        else:
            print("Entrée invalide.")

    while True:
        response = input("Voulez-vous désinstaller Mi Video ? [O/n] ")
        if response == '' or response == 'o' or response == 'O':
            print("Déinstallation de Mi Video...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.videoplayer')
            break
        elif response == 'n' or response == 'N':
            print("Passons...")
            break
        else:
            print("Entrée invalide")

    while True:
        response = input("Voulez-vous désinstaller Mi File Manager ? [O/n]")
        if response == '' or response == 'o' or response == 'O':
            print("Désinstallation de Mi File Manager...")
            os.system('adb shell pm uninstall -k --user 0 com.mi.android.globalFileexplorer')
            break
        elif response == 'n' or response == 'N':
            print("Passons...")
            break
        else:
            print("Entrée invalide")
            
    while True:
        response = input("Voulez-vous désinstaller Mi Gallery ? [O/n]")
        if response == '' or response == 'o' or response == 'O':
            print("Désinstallation de Mi Gallery...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.gallery')
            break
        elif response == 'n' or response == 'N':
            print("Passons...")
            break
        else:
            print("Entrée invalide.")

    while True:
        response = input("Voulez-vous désinstaller Mi Calculator ? [O/n] ")
        if response == '' or response == 'o' or response == 'O':
            print("Désinstallation de Mi Calculator...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.calculator')
            break
        elif response == 'n' or response == 'N':
            print("Passons...")
            break
        else:
            print("Entrée invalide")


    while True:
        response = input("Voulez-vous désinstaller Xiaomi ShareMe ? [O/n] ")
        if response == '' or response == 'o' or response == 'O':
            print("Désinstallation de Xiaomi ShareMe...")
            os.system('adb shell pm uninstall -k --user 0 com.miui.mishare.connectivity ')
            break
        elif response == 'n' or response == 'N':
            print("Passons...")
            break
        else:
            print("Entrée invalide")


            
    input("Fini ! Pressez Entrer pour terminer !")
    sys.exit() 

except KeyboardInterrupt:
    sys.exit()
