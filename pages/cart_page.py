from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object Model pour la page panier."""

    SELECTOR_ITEMS    = ".cart_item"
    SELECTOR_NOM  = "[data-test='inventory-item-name']"
    SELECTOR_PRIX = "[data-test='inventory-item-price']"
    SELECTOR_CHECKOUT = "[data-test='checkout']"

    def verifier_produit(self, nom_produit, prix_attendu=None):
        self.attendre_visible(By.CSS_SELECTOR, ".cart_item")
        items = self.driver.find_elements(By.CSS_SELECTOR, ".cart_item")
        time.sleep(1)  # laisser le panier se charger
        items = self.driver.find_elements(By.CSS_SELECTOR, ".cart_item")
        print(f"Nombre d'items trouves dans le panier : {len(items)}")
        for item in items:
            print(f"HTML item : {item.get_attribute('innerHTML')[:200]}")

    def demarrer_checkout(self):
        self.attendre_cliquable(By.CSS_SELECTOR, self.SELECTOR_CHECKOUT).click()
        self.logger.info("Checkout demarre")
        self.attendre_visible(By.CSS_SELECTOR, "[data-test='firstName']")
