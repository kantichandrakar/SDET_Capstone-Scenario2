from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ThemesPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators (kept as you requested)
    search_box = (By.XPATH, "//input[@placeholder='Search themes']")
    theme_titles = (By.XPATH, "//div/div/h2")

    # Search for a theme
    def search_theme(self, theme_name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_box)
        )
        search_input.clear()
        search_input.send_keys(theme_name)
        search_input.submit()

    # Get all theme titles
    def get_theme_titles(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.theme_titles)
        )
        return [e.text for e in self.driver.find_elements(*self.theme_titles)]