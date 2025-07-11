import requests
import os
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, by_locator, skip_if_not_found=False):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
        except TimeoutException:
            if skip_if_not_found:
                print(f"Element {by_locator} not found, skipping click.")
            else:
                raise

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def find_elements(self, by_locator):
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def download_image(self, img_locator, title):
        try:
            # Wait for image
            img = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(img_locator)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", img)

            img_url = img.get_attribute("src")
            print("Original src:", img_url)

            if not img_url or not img_url.startswith("http"):
                srcset = img.get_attribute("srcset")
                if srcset:
                    img_url = srcset.split(",")[-1].split()[0]
                    print("Using srcset:", img_url)
                else:
                    print(f"Image URL not valid for: {title}")
                    return None

            response = requests.get(img_url)
            if response.status_code != 200:
                print(f"Failed to download image from: {img_url}")
                return None

            img_data = response.content

            img_name = title.strip().replace(" ", "_")[:30] + ".jpg"

            img_name = re.sub(r'[<>:"/\\|?*]', '', img_name)
            if not os.path.exists("images"):
                os.makedirs("images")
            with open(os.path.join("images", img_name), 'wb') as f:
                f.write(img_data)

            print(f"Downloaded image for: {title}")
            return img_name

        except Exception as e:
            print(f"Image not downloaded for: {title}. Error: {e}")
            return None
