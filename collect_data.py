from urllib import request, parse
from config import REDDIT_URL
import json
from console import print_c
from colorama import Fore, Back, Style
from tabulate import tabulate


def collect_posts_from_subreddit(subreddit):
    url = REDDIT_URL + "/r/{}".format(subreddit)
    json_url = url + ".json"

    response = request.urlopen(json_url)
    content = response.read()
    json_data = json.loads(content.decode("utf-8"))["data"]

    posts = json_data["children"]
    posts_filtered = [post for post in posts if len(post["data"]) <= 104 and not post["data"]["over_18"]]

    return posts_filtered


class IndexErrorSmall(Exception):
    def __init__(self, text): super().__init__(text)


def prompt_usr_choice(posts):
    try:
        choice = int(input(
            f"{Style.RESET_ALL}{Fore.RED}Please choose a topic based on title [{Style.BRIGHT}{Fore.GREEN}1{Style.NORMAL}"
            f"{Fore.LIGHTBLACK_EX}-{Style.BRIGHT}{Fore.GREEN}{len(posts)}"
            + f"{Style.NORMAL}{Fore.RED}]> "))
        choice -= 1
        if choice < 0: raise IndexErrorSmall("")
        print_c(f"{Fore.BLUE}You chose: {Style.BRIGHT}{posts[choice]['data']['title']}{Style.RESET_ALL}")

        data = posts[choice]['data']
        return data["url"]
    except ValueError:
        print_c(f"{Fore.RED}{Style.BRIGHT}Cannot preform action with value!{Fore.WHITE}")
        prompt_usr_choice(posts)
    except IndexError:
        print_c(f"{Fore.RED}{Style.BRIGHT}Cannot preform action with value, because it is too big!{Fore.WHITE}")
        prompt_usr_choice(posts)
    except IndexErrorSmall:
        print_c(f"{Fore.RED}{Style.BRIGHT}Cannot preform action with value, because it is too small!{Fore.WHITE}")
        prompt_usr_choice(posts)


def collect_whole_post_from_subreddit(subreddit):
    print_c(f"{Fore.RED}Collecting posts from {Style.BRIGHT}{Fore.YELLOW}{subreddit}{Style.NORMAL}{Fore.RED}!")
    posts = collect_posts_from_subreddit(subreddit)
    print_c(f"{Fore.GREEN}{Style.BRIGHT}{len(posts)}{Style.NORMAL} found!")

    for post in posts: print(Fore.WHITE + post["data"]["title"])
    return prompt_usr_choice(posts)