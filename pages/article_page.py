from selenium.webdriver.common.by import By
import requests
import os

from pages.base_page import BasePage

class ArticlePage(BasePage):
    PARAGRAPHS = (By.ID, "main-content")
    IMAGE = (By.XPATH, "//img[contains(@src, 'elpais.com/resizer')]")
    def get_content(self):
        paragraphs = self.find_elements(self.PARAGRAPHS)
        return "\n".join([p.text for p in paragraphs])

    def download_article_image(self, title):
        # Call base class method
        return self.download_image(self.IMAGE, title)

