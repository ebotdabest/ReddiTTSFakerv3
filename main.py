from collect_data import collect_whole_post_from_subreddit
from colorama import Fore
from mugshots import get_mugshot_of_post
from console import print_c
from config import *
from makevideo import make_post_video

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Setting up environment...")

if not os.path.exists(SCREENSHOT_PATH): os.mkdir(SCREENSHOT_PATH)
if not os.path.exists(TRANSCRIPT_PATH): os.mkdir(TRANSCRIPT_PATH)


clear_console()


print("""██████╗░███████╗██████╗░██████╗░██╗████████╗████████╗░██████╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝█████╗░░██║░░██║██║░░██║██║░░░██║░░░░░░██║░░░╚█████╗░█████╗░░███████║█████═╝░█████╗░░██████╔╝ 
██╔══██╗██╔══╝░░██║░░██║██║░░██║██║░░░██║░░░░░░██║░░░░╚═══██╗██╔══╝░░██╔══██║██╔═██╗░██╔══╝░░██╔══██╗▀█─█▀ █▀▀█ 
██║░░██║███████╗██████╔╝██████╔╝██║░░░██║░░░░░░██║░░░██████╔╝██║░░░░░██║░░██║██║░╚██╗███████╗██║░░██║ █▄█    ▀▄ 
╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ▀   █▄▄█""")

sr = input(f"{Fore.CYAN}Give me a subreddit>{Fore.LIGHTRED_EX} ")
# amount = int(input(f"{Fore.CYAN}Amount of comments> "))
url = collect_whole_post_from_subreddit(sr)
id = get_mugshot_of_post(url)
make_post_video(id)