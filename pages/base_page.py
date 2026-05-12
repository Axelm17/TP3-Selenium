from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import os


class BasePage:
    """Classe de base partagée par toutes les pages."""

    SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots")

    def __init__(self, driver, timeout=15):
        self.driver  = driver
        self.wait    = WebDriverWait(driver, timeout)
        self.logger  = logging.getLogger(self.__class__.__name__)

    def attendre_visible(self, by, selector):
        return self.wait.until(EC.visibility_of_element_located((by, selector)))

    def attendre_invisible(self, by, selector):
        return self.wait.until(EC.invisibility_of_element_located((by, selector)))

    def attendre_cliquable(self, by, selector):
        return self.wait.until(EC.element_to_be_clickable((by, selector)))

    def capturer(self, nom):
        os.makedirs(self.SCREENSHOTS_DIR, exist_ok=True)
        chemin = os.path.join(self.SCREENSHOTS_DIR, f"{nom}.png")
        self.driver.save_screenshot(chemin)
        self.logger.info(f"Screenshot : {chemin}")
        return chemin
