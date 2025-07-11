from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OpinionPage(BasePage):
    ARTICLE_LINKS = (By.XPATH, "//section[contains(@class,'_g _g-md _g-o b b-d')]//descendant::h2[contains(@class,'c_t')]//child::a")

    def get_first_articles(self, count=5):
        elements = self.find_elements(self.ARTICLE_LINKS)[:count]
        articles = []
        for e in elements:
            articles.append({
                "title": e.text,
                "url": e.get_attribute('href')
            })
        return articles
