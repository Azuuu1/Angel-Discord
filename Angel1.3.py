
from dhooks import Webhook
import colorama
from colorama import Fore
import time
import pystyle
from pystyle import Center
text = ('''
   █████╗ ███╗   ██╗ ██████╗ ███████╗██╗     
  ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║     
  ███████║██╔██╗ ██║██║  ███╗█████╗  ██║     
  ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     
  ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗ 1.3 BETA
              
''')
from pystyle import Colors, Colorate

print(Colorate.Diagonal(Colors.blue_to_cyan, text, 1))
print(Colorate.Horizontal(Colors.red_to_blue, "Made By Azuu",1))
print(f"{Fore.RED}This Tool Is In Beta Versions[!]")
webhookurl = Webhook(input(f"{Fore.CYAN}Webhook:"))
if webhookurl == "":
    print("Webhook Is Not Found Closing...")
message = input("Message: ")
delay = int(input("Delay: "))
delay = int(delay)
while True == True:
    time.sleep(delay)
    webhookurl.send(message)
    print(f"{Fore.GREEN}Succes[+]")
