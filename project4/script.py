# %% [markdown]
# # Project 4 -- Dwijen Chawra

# %% [markdown]
# ## Question 1

# %%
import time
import uuid
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

firefox_options = Options()
firefox_options.add_argument("--window-size=1920,1080")
# Headless mode means no GUI
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")
firefox_options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")

driver = webdriver.Firefox(options=firefox_options)
driver.quit()


# %%
def get_zpid(search_term: str, page: int = 1):

    def _load_all_cards(driver):
        cards = driver.find_elements("xpath", "//article[starts-with(@id, 'zpid')]")
        while True:
            try:
                num_cards = len(cards)
                driver.execute_script('arguments[0].scrollIntoView();', cards[num_cards-1])
                time.sleep(5)
                cards = driver.find_elements("xpath", "//article[starts-with(@id, 'zpid')]")
                if num_cards == len(cards):
                    break
                num_cards = len(cards)
            except StaleElementReferenceException:
                # every once in a while we will get a StaleElementReferenceException
                # because we are trying to access or scroll to an element that has changed.
                # this probably means we can skip it because the data has already loaded.
                continue
        
        return cards

    driver = webdriver.Firefox(options=firefox_options)
    driver.get(f"https://www.zillow.com/homes/for_sale/{search_term}/{page}_p/")
    time.sleep(61.13)
    # print("current loaded site: ", driver.current_url)


    if "captcha" in driver.current_url:
        print("captcha")
        driver.quit()
        return []

    cards = _load_all_cards(driver)
    
    results = []
    for card in cards:
        zpid = card.get_attribute("id")
        results.append(zpid)

    driver.quit()

    return results

zpids = []
zpids.extend(get_zpid("32617", 1))
for i in range(2, 2):
    # print("nextpage")
    time.sleep(61.13)
    zpids.extend(get_zpid("32617", i + 1))   

zpids





# %% [markdown]
# ## Question 2

# %%
def get_zpids(search_term: str):

    def _load_all_cards(driver):
        cards = driver.find_elements("xpath", "//article[starts-with(@id, 'zpid')]")
        while True:
            try:
                num_cards = len(cards)
                driver.execute_script('arguments[0].scrollIntoView();', cards[num_cards-1])
                time.sleep(5)
                cards = driver.find_elements("xpath", "//article[starts-with(@id, 'zpid')]")
                if num_cards == len(cards):
                    break
                num_cards = len(cards)
            except StaleElementReferenceException:
                # every once in a while we will get a StaleElementReferenceException
                # because we are trying to access or scroll to an element that has changed.
                # this probably means we can skip it because the data has already loaded.
                continue
        
        return cards

    results = []
    pagecounter = 1

    while True:
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(f"https://www.zillow.com/homes/for_sale/{search_term}_rb/{pagecounter}_p/")

        if "captcha" in driver.current_url:
            print("captcha")
            driver.quit()
            return []
        
        time.sleep(61.13)
        print("current loaded site: ", driver.current_url)

        cards = _load_all_cards(driver)

        for card in cards:
            zpid = card.get_attribute("id")
            results.append(zpid)
        
        # driver.find_element_by_xpath("//a[@disabled='disabled']")
        nextpagebutton = driver.find_elements("xpath", "//a[@title='Next page']")

        if nextpagebutton.get_attribute("disabled") == "true":
            break
            
        pagecounter += 1

        driver.quit()

    return results

get_zpids("32607")

# %% [markdown]
# Markdown notes and sentences and analysis written here.

# %% [markdown]
# ## Question 3

# %% [markdown]
# Markdown notes and sentences and analysis written here.

# %% [markdown]
# ## Question 4

# %% [markdown]
# Markdown notes and sentences and analysis written here.

# %% [markdown]
# ## Pledge
# 
# By submitting this work I hereby pledge that this is my own, personal work. I've acknowledged in the designated place at the top of this file all sources that I used to complete said work, including but not limited to: online resources, books, and electronic communications. I've noted all collaboration with fellow students and/or TA's. I did not copy or plagiarize another's work.
# 
# > As a Boilermaker pursuing academic excellence, I pledge to be honest and true in all that I do. Accountable together – We are Purdue.


