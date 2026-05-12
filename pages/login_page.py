from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object Model pour la page de connexion de Sauce Demo."""

    URL = "https://www.saucedemo.com/"

    SELECTOR_USERNAME = "#user-name"
    SELECTOR_PASSWORD = "#password"
    SELECTOR_BOUTON   = "#login-button"
    SELECTOR_ERREUR   = "[data-test='error']"

    def charger(self):
        self.driver.get(self.URL)
        self.attendre_visible(By.CSS_SELECTOR, self.SELECTOR_USERNAME)
        self.logger.info("Page de login chargee")

    def se_connecter(self, username, password):
        self.logger.info(f"Tentative de connexion avec : {username}")
        self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_USERNAME).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_PASSWORD).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_BOUTON).click()

    def lire_message_erreur(self):
        el = self.attendre_visible(By.CSS_SELECTOR, self.SELECTOR_ERREUR)
        return el.text.strip()

    def verifier_sur_page_login(self):
        assert "saucedemo.com" in self.driver.current_url, \
            "L'utilisateur n'est pas sur la page de login !"
