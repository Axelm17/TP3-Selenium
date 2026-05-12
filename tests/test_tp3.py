import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage

LIGNE      = "=" * 60
PRODUIT    = "Sauce Labs Backpack"
UTILISATEUR = "standard_user"
MOT_DE_PASSE = "secret_sauce"


def test_scenario1_connexion_reussie(driver):
    logger = logging.getLogger("scenario1")
    print(f"\n{LIGNE}\nSCENARIO 1 — Connexion reussie\n{LIGNE}")

    login     = LoginPage(driver)
    inventaire = InventoryPage(driver)

    login.charger()
    login.se_connecter(UTILISATEUR, MOT_DE_PASSE)
    inventaire.verifier_chargement()

    logger.info("Scenario 1 reussi")
    print("Connexion reussie — page catalogue accessible")


def test_scenario2_connexion_refusee(driver):
    logger = logging.getLogger("scenario2")
    print(f"\n{LIGNE}\nSCENARIO 2 — Connexion refusee\n{LIGNE}")

    login = LoginPage(driver)

    login.charger()
    login.se_connecter("locked_out_user", MOT_DE_PASSE)

    erreur = login.lire_message_erreur()
    assert "locked out" in erreur.lower(), f"Message d'erreur inattendu : '{erreur}'"
    login.verifier_sur_page_login()

    logger.info(f"Scenario 2 reussi — message : {erreur}")
    print(f"Connexion refusee — message d'erreur verifie : '{erreur}'")


def test_scenario3_ajout_panier(driver):
    logger = logging.getLogger("scenario3")
    print(f"\n{LIGNE}\nSCENARIO 3 — Ajout au panier\n{LIGNE}")

    login      = LoginPage(driver)
    inventaire = InventoryPage(driver)
    panier     = CartPage(driver)

    login.charger()
    login.se_connecter(UTILISATEUR, MOT_DE_PASSE)
    inventaire.verifier_chargement()

    prix = inventaire.ajouter_au_panier(PRODUIT)
    print(f"Produit ajoute : {PRODUIT} — {prix}")

    inventaire.verifier_bouton_remove(PRODUIT)
    print("Bouton 'Remove' confirme")

    badge = inventaire.lire_badge_panier()
    assert badge == "1", f"Badge panier inattendu : '{badge}'"
    print(f"Badge panier : {badge}")

    inventaire.capturer("scenario3_apres_ajout")

    inventaire.ouvrir_panier()
    prix_panier = panier.verifier_produit(PRODUIT, prix)
    print(f"Produit present dans le panier — prix : {prix_panier}")

    logger.info("Scenario 3 reussi")


def test_scenario4_achat_complet(driver):
    logger = logging.getLogger("scenario4")
    print(f"\n{LIGNE}\nSCENARIO 4 — Parcours d'achat complet\n{LIGNE}")

    login      = LoginPage(driver)
    inventaire = InventoryPage(driver)
    panier     = CartPage(driver)
    checkout   = CheckoutPage(driver)
    confirmation = CheckoutCompletePage(driver)

    # 1. Connexion
    login.charger()
    login.se_connecter(UTILISATEUR, MOT_DE_PASSE)
    inventaire.verifier_chargement()
    print("Connexion effectuee")

    # 2. Ajout produit
    prix = inventaire.ajouter_au_panier(PRODUIT)
    print(f"Produit ajoute : {PRODUIT} — {prix}")

    # 3. Panier
    inventaire.ouvrir_panier()
    panier.verifier_produit(PRODUIT, prix)
    print("Produit verifie dans le panier")

    # 4. Checkout — étape 1
    panier.demarrer_checkout()
    checkout.saisir_informations("John", "Doe", "59000")
    print("Informations client saisies")

    # 5. Recapitulatif
    checkout.verifier_recapitulatif(PRODUIT, prix)
    sous_total, taxe, total = checkout.lire_totaux()
    print(f"Recapitulatif — {sous_total} | {taxe} | {total}")

    assert sous_total != "", "Sous-total absent !"
    assert taxe      != "", "Taxe absente !"
    assert total     != "", "Total absent !"

    # 6. Validation
    checkout.valider_commande()
    confirmation.verifier_confirmation()
    confirmation.capturer("scenario4_confirmation")
    print("Commande validee — message de confirmation recu")

    logger.info("Scenario 4 reussi")


def test_scenario5_deconnexion(driver):
    logger = logging.getLogger("scenario5")
    print(f"\n{LIGNE}\nSCENARIO 5 — Deconnexion\n{LIGNE}")

    login      = LoginPage(driver)
    inventaire = InventoryPage(driver)

    login.charger()
    login.se_connecter(UTILISATEUR, MOT_DE_PASSE)
    inventaire.verifier_chargement()

    inventaire.se_deconnecter()
    login.verifier_sur_page_login()

    logger.info("Scenario 5 reussi")
    print("Deconnexion reussie — retour sur la page de login")
