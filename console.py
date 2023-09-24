from colorama import Fore, Style
import sys
from sys import stdout

def print_c(text):
    stdout.write(text + f"\n")

def exit_code():
    sys.exit()