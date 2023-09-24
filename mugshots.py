from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
import os.path as p
from config import SCREENSHOT_PATH, TRANSCRIPT_PATH
from urllib import parse
import re
import selenium

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbat symbols
        "\U000024C2-\U0001F251"  
        "]+"
    )
    return emoji_pattern.sub(r'', text)

def get_mugshot_of_post(url):
    parsed = parse.urlparse(url)
    post_id = parsed.path.split("/")[4]

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1.5)
    if not p.exists(p.join(SCREENSHOT_PATH, post_id)): os.mkdir(p.join(SCREENSHOT_PATH, post_id))
    if not p.exists(p.join(TRANSCRIPT_PATH, post_id)): os.mkdir(p.join(TRANSCRIPT_PATH, post_id))
    title = driver.find_element(By.TAG_NAME, 'shreddit-post')
    try:
        bts = driver.find_element(By.XPATH, "//shreddit-post/div/button")
        if bts.text == "Read more": bts.click()
    # The only exception here can be an element not found
    # I rest my case
    except Exception:
        pass

    driver.set_window_size(1920, title.size["height"] + 1000)
    title.screenshot(p.join(SCREENSHOT_PATH, post_id, "title.png"))
    title_text = driver.find_element(By.XPATH, '//shreddit-post/h1')
    parts = driver.find_elements(By.XPATH, "//shreddit-post/div[@slot='text-body']/div/p")

    with open(p.join(TRANSCRIPT_PATH, post_id, 'title.txt'), "w") as f:
        f.write(title_text.text)

    ts = []
    i = 0
    for part in parts:
        part.screenshot(p.join(SCREENSHOT_PATH, post_id, f"{i}.png"))
        i += 1
        ts.append(part.text)

    with open(p.join(TRANSCRIPT_PATH, post_id, "ts.txt"), "w") as f:
        f.write("\n".join(ts))



    return post_id
