from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class HomePage(BasePage):
    OPINION_LINK = (By.XPATH, "//nav[contains(@class,'cs_m')]//child::a[text()='Opinión']")
    AgreeButton = (By.ID, "didomi-notice-agree-button")
    def agree_condition(self):
        try:
            self.click(self.AgreeButton)
        except TimeoutException:
            print("Agree button not found, skipping...")
    def go_to_opinion(self):
        self.click(self.OPINION_LINK)