from selenium import webdriver
from pages.home_page import HomePage
from pages.Opinion_page import OpinionPage
from pages.article_page import ArticlePage
from selenium.webdriver.chrome.options import Options
from Utils.translator_utils import translate_titles, find_repeated_words
import time
import asyncio

options = Options()
options.add_argument('--headless')
options.add_argument("window-size=1920,1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# Set up
driver = webdriver.Chrome(options=options)
try:
    home = HomePage(driver)
    opinion = OpinionPage(driver)
    article = ArticlePage(driver)
    home.open("https://elpais.com")
    home.agree_condition()
    home.go_to_opinion()
    articles_info = opinion.get_first_articles()
    print(articles_info)
    contents = []
    titles = []

    for art in articles_info:
        driver.set_page_load_timeout(180)
        try:
            driver.get(art['url'])
        except Exception as e:
            print(f"Skipping article {art['url']} due to timeout: {e}")
            continue
        time.sleep(3)
        content = article.get_content()
        contents.append(content)
        article.download_article_image(art['title'])
        titles.append(art['title'])
    print("Original Titles (Spanish):")
    for t in titles:
        print(t)

    translated = translate_titles(titles)
    print("\nTranslated Titles (English):")
    for t in translated:
        print(t)

    repeated = find_repeated_words(translated)
    print("\nRepeated Words (>2 times):")
    for word, count in repeated.items():
        print(f"{word}: {count}")
finally:
    driver.quit()