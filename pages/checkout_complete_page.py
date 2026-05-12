from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """Page Object Model pour la page de confirmation de commande."""

    SELECTOR_TITRE   = ".complete-header"
    SELECTOR_MESSAGE = ".complete-text"

    MESSAGE_ATTENDU = "Thank you for your order!"

    def verifier_confirmation(self):
        titre = self.attendre_visible(By.CSS_SELECTOR, self.SELECTOR_TITRE)
        assert self.MESSAGE_ATTENDU in titre.text, \
            f"Message de confirmation inattendu : '{titre.text}'"
        self.logger.info(f"Confirmation recue : '{titre.text}'")
