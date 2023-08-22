from colorama import Fore , Style
from time import sleep
import random

def main_page():
    banner = Fore.LIGHTRED_EX + f"""

    ███╗░░░███╗███████╗████████╗░█████╗░  ░█████╗░░█████╗░░█████╗░███████╗░██████╗░██████╗
    ████╗░████║██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ██╔████╔██║█████╗░░░░░██║░░░███████║  ███████║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░
    ██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║  ██╔══██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██║░╚═╝░██║███████╗░░░██║░░░██║░░██║  ██║░░██║╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝
    ╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░
    {Fore.LIGHTYELLOW_EX}Made By Taha Security                                                               v1"""

    for line in banner.center(25).split(sep="\n"):
        print(line)
        sleep(0.1)


def sec_page():
    print("\033[1m"+Fore.LIGHTWHITE_EX+"\n    ["+Fore.LIGHTGREEN_EX+"1"+Fore.LIGHTWHITE_EX+"]"+"  Track Location With Link")
    sleep(0.1)
    print("\033[1m"+Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"2"+Fore.LIGHTWHITE_EX+"]"+"  Hack Webcam With Link")
    sleep(0.1)
    print("\033[1m"+Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"3"+Fore.LIGHTWHITE_EX+"]"+"  Hack Microphone With Link")
    sleep(0.1)
    print("\033[1m"+Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"0"+Fore.LIGHTWHITE_EX+"]"+"  Exit\n" + "\033[0m")
    sleep(0.1)

def webcam_banner():
    banner = Fore.LIGHTBLUE_EX + f"""
    █░█░█ █▀▀ █▄▄ █▀▀ ▄▀█ █▀▄▀█   ▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀
    ▀▄▀▄▀ ██▄ █▄█ █▄▄ █▀█ █░▀░█   █▀█ ░█░ ░█░ █▀█ █▄▄ █░█
    """
    for line in banner.split("\n"):
        print(line)
        sleep(0.1)

def mice_banner():
    banner = Fore.LIGHTBLUE_EX + f"""
    █▀▄▀█ █ █▀▀ █▀█ █▀█ █▀█ █░█ █▀█ █▄░█ █▀▀   ▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀
    █░▀░█ █ █▄▄ █▀▄ █▄█ █▀▀ █▀█ █▄█ █░▀█ ██▄   █▀█ ░█░ ░█░ █▀█ █▄▄ █░█
    """
    for line in banner.split("\n"):
        print(line)
        sleep(0.1)

def webcam_menu():
    print("\033[1m"+Fore.LIGHTWHITE_EX+"\n    ["+Fore.LIGHTGREEN_EX+"1"+Fore.LIGHTWHITE_EX+"]"+"  Default Page")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"2"+Fore.LIGHTWHITE_EX+"]"+"  Your Page ( customize )")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"0"+Fore.LIGHTWHITE_EX+"]"+"  Back to main Page\n"+"\033[0m")
    sleep(0.1)  

def mice_menu():
    print("\033[1m"+Fore.LIGHTWHITE_EX+"\n    ["+Fore.LIGHTGREEN_EX+"1"+Fore.LIGHTWHITE_EX+"]"+"  Default Page")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"2"+Fore.LIGHTWHITE_EX+"]"+"  Your Page ( customize )")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"0"+Fore.LIGHTWHITE_EX+"]"+"  Back to main Page\n"+"\033[0m")
    sleep(0.1) 

def hacking():
    banner = Fore.GREEN + """
    ▒█░▒█ ░█▀▀█ ▒█▀▀█ ▒█░▄▀ ▀█▀ ▒█▄░▒█ ▒█▀▀█ ░ ░ ░ 
    ▒█▀▀█ ▒█▄▄█ ▒█░░░ ▒█▀▄░ ▒█░ ▒█▒█▒█ ▒█░▄▄ ▄ ▄ ▄ 
    ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▄█▄ ▒█░░▀█ ▒█▄▄█ █ █ █ """  
    for line in banner.split("\n"):
        print(line)
        sleep(0.1)

def hacking_():
    banner = Fore.GREEN + """
    ▒█░▒█ ░█▀▀█ ▒█▀▀█ ▒█░▄▀ ▀█▀ ▒█▄░▒█ ▒█▀▀█ ░ ░ ░ 
    ▒█▀▀█ ▒█▄▄█ ▒█░░░ ▒█▀▄░ ▒█░ ▒█▒█▒█ ▒█░▄▄ ▄ ▄ ▄ 
    ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▄█▄ ▒█░░▀█ ▒█▄▄█ █ █ █ """  
    print(banner)

def hacking_menu():
    print("\033[1m"+Fore.LIGHTWHITE_EX+"\n    ["+Fore.LIGHTGREEN_EX+"1"+Fore.LIGHTWHITE_EX+"]"+"  Run on Localhost")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"2"+Fore.LIGHTWHITE_EX+"]"+"  Port Forwarding ( With Ngrok )\n"+"\033[0m")
    sleep(0.1)  

def hacking_menu2():
    sleep(0.1)
    print("\033[1m"+ Fore.LIGHTGREEN_EX + "\n    Page Is Ready !\n")
    sleep(0.1)
    print("\033[1m"+Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"1"+Fore.LIGHTWHITE_EX+"]"+"  Run on Localhost")
    sleep(0.1)
    print("\033[1m"+Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"2"+Fore.LIGHTWHITE_EX+"]"+"  Port Forwarding ( With Ngrok )\n"+"\033[0m")
    sleep(0.1) 

def loc_banner():
    banner = Fore.LIGHTBLUE_EX + f"""
    ▀█▀ █▀█ ▄▀█ █▀▀ █▄▀   █░░ █▀█ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█
    ░█░ █▀▄ █▀█ █▄▄ █░█   █▄▄ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█"""
    for line in banner.split("\n"):
        print(line)
        sleep(0.1)

def loc_menu():
    print("\033[1m"+Fore.LIGHTWHITE_EX+"\n    ["+Fore.LIGHTGREEN_EX+"1"+Fore.LIGHTWHITE_EX+"]"+"  Default Page")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"2"+Fore.LIGHTWHITE_EX+"]"+"  Your Page ( customize )")
    sleep(0.1)
    print(Fore.LIGHTWHITE_EX+"    ["+Fore.LIGHTGREEN_EX+"0"+Fore.LIGHTWHITE_EX+"]"+"  Back to main Page\n"+"\033[0m")
    sleep(0.1) 