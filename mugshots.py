from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
import os.path as p
from config import SCREENSHOT_PATH, TRANSCRIPT_PATH
from urllib import parse


def get_mugshot_of_post(url):
    parsed = parse.urlparse(url)
    post_id = parsed.path.split("/")[4]

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1.5)
    if not p.exists(p.join(SCREENSHOT_PATH, post_id)): os.mkdir(p.join(SCREENSHOT_PATH, post_id))
    if not p.exists(p.join(TRANSCRIPT_PATH, post_id)): os.mkdir(p.join(TRANSCRIPT_PATH, post_id))
    title = driver.find_element(By.TAG_NAME, 'shreddit-post')
    title.screenshot(p.join(SCREENSHOT_PATH, post_id, "title.png"))
    parts = driver.find_elements(By.XPATH, "//shreddit-post/div[@slot='text-body']/div/p")
    ts = []
    for part in parts: ts.append(part.text)
    with open(p.join(TRANSCRIPT_PATH, post_id, "ts.txt"), "w") as f: f.write("\n".join(ts))

    return post_id