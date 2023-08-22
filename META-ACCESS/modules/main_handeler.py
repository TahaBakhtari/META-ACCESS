def meta_access(): 
    from colorama import Fore , Style
    import time , os , sys , platform 
    from modules import banners , webcam , mice , location

    def clear():
        if "Windows" in platform.uname():
            os.system("cls")
        else:
            os.system("clear")
    clear()

    banners.main_page()
    banners.sec_page()
    select = input(Fore.LIGHTWHITE_EX + f"    Select > "+Fore.LIGHTRED_EX)

    if select == "1":
        time.sleep(0.3)
        clear()
        location.location()
    elif select == "2":
        time.sleep(0.3)
        clear()
        webcam.webcam()
    elif select == "3":
        time.sleep(0.3)
        clear()
        mice.mice()
    elif select == "0":
        time.sleep(0.3)
        clear()
        print(Fore.LIGHTCYAN_EX + """

Good Bye. . . 

        """)
        sys.exit()