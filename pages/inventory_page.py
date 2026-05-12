from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class InventoryPage(BasePage):
    """Page Object Model pour la page catalogue."""

    SELECTOR_TITRE       = ".title"
    SELECTOR_MENU        = "#react-burger-menu-btn"
    SELECTOR_LOGOUT      = "#logout_sidebar_link"
    SELECTOR_BADGE_PANIER = ".shopping_cart_badge"
    SELECTOR_PANIER      = ".shopping_cart_link"

    def verifier_chargement(self):
        titre = self.attendre_visible(By.CSS_SELECTOR, self.SELECTOR_TITRE)
        assert "Products" in titre.text, f"Titre inattendu : '{titre.text}'"
        self.logger.info("Page inventaire chargee et verifiee")

    def ajouter_au_panier(self, nom_produit):
        """Ajoute un produit au panier par son nom."""
        # Trouve le bouton Add to cart correspondant au produit
        produits = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for produit in produits:
            nom = produit.find_element(By.CLASS_NAME, "inventory_item_name").text
            if nom == nom_produit:
                prix = produit.find_element(By.CLASS_NAME, "inventory_item_price").text
                bouton = produit.find_element(By.TAG_NAME, "button")
                bouton.click()
                self.logger.info(f"Produit ajoute : {nom} — {prix}")
                return prix
        raise AssertionError(f"Produit introuvable : '{nom_produit}'")

    def verifier_bouton_remove(self, nom_produit):
        produits = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for produit in produits:
            nom = produit.find_element(By.CLASS_NAME, "inventory_item_name").text
            if nom == nom_produit:
                bouton = produit.find_element(By.TAG_NAME, "button")
                assert bouton.text == "Remove", f"Bouton inattendu : '{bouton.text}'"
                return
        raise AssertionError(f"Produit introuvable : '{nom_produit}'")

    def lire_badge_panier(self):
        badge = self.attendre_visible(By.CSS_SELECTOR, self.SELECTOR_BADGE_PANIER)
        return badge.text

    def ouvrir_panier(self):
        self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_PANIER).click()
        time.sleep(1)  # laisser le panier se charger
        self.logger.info("Panier ouvert")

    def se_deconnecter(self):
        self.attendre_cliquable(By.CSS_SELECTOR, self.SELECTOR_MENU).click()
        time.sleep(0.5)  # laisser le menu s'ouvrir
        self.attendre_cliquable(By.CSS_SELECTOR, self.SELECTOR_LOGOUT).click()
        time.sleep(1)    # laisser la redirection se faire
        self.logger.info("Deconnexion effectuee")
