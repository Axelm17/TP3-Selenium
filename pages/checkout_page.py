from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object Model pour les pages de checkout (étape 1 et récapitulatif)."""

    SELECTOR_PRENOM   = "[data-test='firstName']"
    SELECTOR_NOM      = "[data-test='lastName']"
    SELECTOR_POSTAL   = "[data-test='postalCode']"
    SELECTOR_CONTINUE = "[data-test='continue']"
    SELECTOR_FINISH   = "[data-test='finish']"

    # Récapitulatif
    SELECTOR_ITEMS      = ".cart_item"
    SELECTOR_NOM_ITEM   = ".inventory_item_name"
    SELECTOR_PRIX_ITEM  = ".inventory_item_price"
    SELECTOR_SOUS_TOTAL = ".summary_subtotal_label"
    SELECTOR_TAXE       = ".summary_tax_label"
    SELECTOR_TOTAL      = ".summary_total_label"

    def saisir_informations(self, prenom, nom, postal):
        self.attendre_visible(By.CSS_SELECTOR, self.SELECTOR_PRENOM).send_keys(prenom)
        self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_NOM).send_keys(nom)
        self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_POSTAL).send_keys(postal)
        self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_CONTINUE).click()
        self.logger.info(f"Informations saisies : {prenom} {nom} — {postal}")

    def verifier_recapitulatif(self, nom_produit, prix_attendu):
        items = self.driver.find_elements(By.CSS_SELECTOR, self.SELECTOR_ITEMS)
        trouve = False
        for item in items:
            nom  = item.find_element(By.CSS_SELECTOR, self.SELECTOR_NOM_ITEM).text
            prix = item.find_element(By.CSS_SELECTOR, self.SELECTOR_PRIX_ITEM).text
            if nom == nom_produit:
                assert prix == prix_attendu, f"Prix inattendu : '{prix}'"
                trouve = True
                self.logger.info(f"Recapitulatif : {nom} — {prix}")
        assert trouve, f"Produit '{nom_produit}' absent du recapitulatif !"

    def lire_totaux(self):
        sous_total = self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_SOUS_TOTAL).text
        taxe       = self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_TAXE).text
        total      = self.driver.find_element(By.CSS_SELECTOR, self.SELECTOR_TOTAL).text
        self.logger.info(f"Totaux — {sous_total} | {taxe} | {total}")
        return sous_total, taxe, total

    def valider_commande(self):
        self.attendre_cliquable(By.CSS_SELECTOR, self.SELECTOR_FINISH).click()
        self.logger.info("Commande validee")
