from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random

# ---------- SETTINGS ----------
search_query = "politics"
tweet_limit = 3000
output_file = "tweets_selenium.csv"
min_scroll = 2
max_scroll = 6
# -------------------------------

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-webgl")
chrome_options.add_argument("--disable-accelerated-2d-canvas")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--headless=new")  # more stable headless

# Initialize driver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

try:
    # Login
    driver.get("https://twitter.com/login")
    time.sleep(3)
    driver.find_element(By.NAME, "text").send_keys("ChetanaM79086")
    driver.find_element(By.XPATH, '//span[text()="Next"]').click()
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Chetana@2302")
    driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
    time.sleep(5)

    # Search page
    url = f"https://twitter.com/search?q={search_query}&f=live"
    driver.get(url)
    time.sleep(3)

    tweets = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    while len(tweets) < tweet_limit:
        try:
            wait.until(EC.presence_of_all_elements_located((By.XPATH, '//article[contains(@data-testid,"tweet")]')))
            tweet_elements = driver.find_elements(By.XPATH, '//article[contains(@data-testid,"tweet")]')

            for elem in tweet_elements:
                try:
                    text = " ".join([span.text for span in elem.find_elements(By.XPATH, './/div[@lang]')])
                    timestamp_elem = elem.find_element(By.TAG_NAME, 'time')
                    timestamp = timestamp_elem.get_attribute('datetime')
                    tweet_data = {"text": text, "created_at": timestamp}
                    if tweet_data not in tweets:
                        tweets.append(tweet_data)
                except:
                    continue

            # Scroll
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(min_scroll, max_scroll))

            # Stop if no more content
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        except Exception as e:
            print("⚠️ Warning:", e)
            break

    # Save CSV
    tweets = tweets[:tweet_limit]
    df = pd.DataFrame(tweets)
    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"✅ Scraped {len(df)} tweets and saved to {output_file}")

finally:
    driver.quit()
