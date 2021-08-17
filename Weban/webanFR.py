import time
import os

print('''

 __           __  _                            _ _               
 \ \        / / | |         /\               | (_)              
  \ \  /\  / /__| |__      /  \   _ __   __ _| |_ _______ _ __  
   \ \/  \/ / _ \ '_ \    / /\ \ | '_ \ / _` | | |_  / _ \ '__| 
    \  /\  /  __/ |_) |  / ____ \| | | | (_| | | |/ /  __/ |    
     \/  \/ \___|_.__/  /_/    \_\_| |_|\__,_|_|_/___\___|_|    
                                                                
                                                                
''')

url = input("Entrez l'URL : ")

if "https" and "http" not in url:
    print("D'accord je scan : " + url)
    time.sleep(1)
    os.system("ping " + url)
else:
    print("Merci de ne pas préciser le protocole ainsi que les '/'. ")