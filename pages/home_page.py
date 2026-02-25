from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    download_extend = (By.XPATH, "//span[text()='Extend']")
    themes_option = (By.XPATH, "//a/span[contains(text(),'Themes')]")

    # Launch URL
    def open_url(self):
        self.driver.get("https://wordpress.org/")

    # Mouse Hover + Click Themes
    def mouse_over_and_click_themes(self):
        actions = ActionChains(self.driver)
        download = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.download_extend)
        )
        actions.move_to_element(download).perform()
        download.click()

        themes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.themes_option)
        )
        themes.click()