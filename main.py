import os
import requests
from bs4 import BeautifulSoup

ServerPath = "E:\OHDS\HarshDoorstop"

if os.name == 'nt':
    serverOs = "WindowsServer"
else:
    serverOs = "LinuxServer"

def CheckPath():
    if not os.path.isdir(ServerPath):
        print("Server folder not found!")
        exit()

    if not os.path.exists(ServerPath + f"/Saved/Config/{serverOs}/Bans.cfg"):
        os.makedirs(ServerPath+f"/Saved/Config/{serverOs}", exist_ok=True)


def bannedPlayers():
    response = requests.get(url="https://raw.githubusercontent.com/PERPGamer/OHD-Communtiy-Ban-List/main/Bans.cfg")
    return (response.content).decode("utf-8").split("\n")

CheckPath()

f = open(ServerPath + f"/Saved/Config/{serverOs}/Bans.cfg", "w")
for player in bannedPlayers():
    f.write(player + "\n")  
f.close()

print("File Bans.cfg updated succesfully!")
