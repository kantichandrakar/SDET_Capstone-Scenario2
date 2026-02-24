import pytest
from pages.home_page import HomePage
from pages.themes_page import ThemesPage

@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("theme_name", ["hello", "Twenty"])
def test_search_theme(driver, theme_name):
    home = HomePage(driver)
    themes = ThemesPage(driver)

    # Step 1: Launch URL and verify title
    home.open_url()
    assert "WordPress" in driver.title, "WordPress homepage title mismatch"

    # Step 2: Mouse over "Download & Extend" and click "Themes"
    home.mouse_over_and_click_themes()

    # Step 3: Search for theme
    themes.search_theme(theme_name)

    # Step 4: Verify theme titles are displayed
    titles = themes.get_theme_titles()
    assert any(theme_name.lower() in t.lower() for t in titles), f"{theme_name} not found in themes"