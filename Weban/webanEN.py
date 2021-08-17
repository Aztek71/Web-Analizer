import time
import os

print('''

 __          __  _                            _ _               
 \ \        / / | |         /\               | (_)              
  \ \  /\  / /__| |__      /  \   _ __   __ _| |_ _______ _ __  
   \ \/  \/ / _ \ '_ \    / /\ \ | '_ \ / _` | | |_  / _ \ '__| 
    \  /\  /  __/ |_) |  / ____ \| | | | (_| | | |/ /  __/ |    
     \/  \/ \___|_.__/  /_/    \_\_| |_|\__,_|_|_/___\___|_|    
                                                                
                                                                
''')

url = input("Enter URL : ")

if "https" and "http" not in url:
    print("Ok I scan : " + url)
    time.sleep(1)
    os.system("ping " + url)
else:
    print("Please do not specify the protocol as well as the '/'.")
