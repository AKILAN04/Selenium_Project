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
        try:
            # Try clicking close buttons if they exist
            self.close_if_exists((By.CLASS_NAME, "pmConsentWall-button"))
            self.close_if_exists((By.CSS_SELECTOR, ".pmConsentWall-main-inner a.pmConsentWall-button"))
            self.close_if_exists((By.XPATH, "//a[contains(@onclick,'acceptConsentWall')]"))

            # Optionally remove overlay div as fallback
            self.driver.execute_script("""
                let el = document.querySelector('.pmConsentWall-main-inner');
                if (el) { el.remove(); }
            """)
            print("Extra consent wall removed if present.")

        except Exception as e:
            print("Error while closing extra overlay:", e)
        self.click(self.OPINION_LINK)