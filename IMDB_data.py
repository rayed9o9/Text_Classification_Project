from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver', options=chrome_options)
movies_text_file = open("family_ids_for_subtitle.txt", "w")

start = 1
all_movies_lest= []
movies_to_download = 30000



while start < movies_to_download:
    #horror list from IMDB
    #driver.get(f"https://www.imdb.com/search/title/?genres=horror&sort=num_votes,desc&start={start}&explore=title_type,genres&ref_=adv_nxt")
    #family list from IDMB
    driver.get(f"https://www.imdb.com/search/title/?title_type=feature&genres=family&sort=num_votes,desc&start={start}&explore=genres&ref_=adv_nxt")

    titles = driver.find_elements_by_class_name('lister-item-header')

    movies_id_in_page = []
    for i in titles:
        # print (i.find_elements_by_tag_name('a'))
        movies_id_in_page.append(i.find_elements_by_tag_name('a'))



    # print(movies_id_in_page[2][0].get_attribute("href")[27:36])


    for i in movies_id_in_page:
        all_movies_lest.append(i[0].get_attribute("href")[27:36])
        print(start)
        movies_text_file.write(i[0].get_attribute("href")[27:36]+'\n')

    start = start + 50


print(all_movies_lest[299])