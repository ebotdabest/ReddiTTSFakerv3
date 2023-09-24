import urllib.error
from moviepy import editor

from collect_data import collect_whole_post_from_subreddit
from colorama import Fore, Style
from mugshots import get_mugshot_of_post
from console import print_c, exit_code
from config import *
from makevideo import make_post_video
from tts import say_and_save

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Setting up environment...")

if not os.path.exists(SCREENSHOT_PATH): os.mkdir(SCREENSHOT_PATH)
if not os.path.exists(TRANSCRIPT_PATH): os.mkdir(TRANSCRIPT_PATH)
if not os.path.exists(VOICE_PATH): os.mkdir(VOICE_PATH)


clear_console()


print("""██████╗░███████╗██████╗░██████╗░██╗████████╗████████╗░██████╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝█████╗░░██║░░██║██║░░██║██║░░░██║░░░░░░██║░░░╚█████╗░█████╗░░███████║█████═╝░█████╗░░██████╔╝ 
██╔══██╗██╔══╝░░██║░░██║██║░░██║██║░░░██║░░░░░░██║░░░░╚═══██╗██╔══╝░░██╔══██║██╔═██╗░██╔══╝░░██╔══██╗▀█─█▀ █▀▀█ 
██║░░██║███████╗██████╔╝██████╔╝██║░░░██║░░░░░░██║░░░██████╔╝██║░░░░░██║░░██║██║░╚██╗███████╗██║░░██║ █▄█    ▀▄ 
╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ▀   █▄▄█""")

sr = input(f"{Fore.CYAN}Give me a subreddit>{Fore.LIGHTRED_EX} ")
# amount = int(input(f"{Fore.CYAN}Amount of comments> "))
try:
    url = collect_whole_post_from_subreddit(sr)
except urllib.error.HTTPError:
    print_c("Too many requests please try again later")
    exit_code()

id = get_mugshot_of_post(url)

if not os.path.exists(os.path.join(VOICE_PATH, id)): os.mkdir(os.path.join(VOICE_PATH, id))
durations, i = [], 0

with open(os.path.join(TRANSCRIPT_PATH, id, "ts.txt")) as f:
    lines = f.readlines()


for line in lines:
    print_c(f"{Fore.CYAN}Saying:{Fore.GREEN}{Style.BRIGHT}{line}{Style.NORMAL}{Fore.WHITE}")
    say_and_save(line, os.path.join(VOICE_PATH, id, str(i) + ".mp3"))
    durations.append(editor.AudioFileClip(os.path.join(VOICE_PATH, id, str(i) + ".mp3")).duration)
    i += 1


with open(os.path.join(TRANSCRIPT_PATH, id, "title.txt")) as f:
    ttl = f.read()


say_and_save(ttl, os.path.join(VOICE_PATH, id, "title.mp3"))
durations.append(editor.AudioFileClip(os.path.join(VOICE_PATH, id, "title.mp3")).duration)

make_post_video(id, durations)
