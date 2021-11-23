from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
# chrome_options.add_extension("Adblock.crx")
# chrome_options.add_argument("--headless")
pref = {
'download.default_directory' : '/0'
}
chrome_options.add_experimental_option('prefs',pref)
driver = webdriver.Chrome('chromedriver', options=chrome_options)

#TODO: change the list to get the category you want
with open("after_cleaning.txt") as f:
    lines = f.readlines()

movies_not_found = open("movies_not_found.txt","w")
i = 0
not_found = []

#TODO: Before adding the number of the files add Adblock to the web browser + chose the download folder
files_to_download = 25000

input()
while(i < int(files_to_download)):
    try:
        # if(driver.find_element_by_xpath('//button[text()="close"]')):
        #     driver.find_element_by_xpath('//button[text()="close"]').click()
        print(i)
        print(lines[i])
        driver.get(f"https://yts-subs.com/movie-imdb/{lines[i]}")
        en = driver.find_element_by_xpath('//span[text()="English"]')
        find_download = en.find_element_by_xpath('.//ancestor::tr')
        find_download.click()
        download_sub = driver.find_element_by_xpath('//span[text()="DOWNLOAD SUBTITLE"]')

        download_sub.click()
        i = i+1
    except Exception as e:
        not_found.append(lines[i])
        movies_not_found.write(lines[i])
        print(e)
        i= i+1

