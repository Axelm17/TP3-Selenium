from selenium import webdriver
from utils.logger import configurer_logger
from selenium.webdriver.chrome.options import Options
from tests.test_tp3 import (
    test_scenario1_connexion_reussie,
    test_scenario2_connexion_refusee,
    test_scenario3_ajout_panier,
    test_scenario4_achat_complet,
    test_scenario5_deconnexion,
)

LIGNE = "=" * 60


def creer_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Désactiver le popup "mot de passe compromis" parce que cet enfoiré faisait tout foirer
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    return webdriver.Chrome(options=options)


def main():
    logger = configurer_logger()

    print(LIGNE)
    print("TP3 — Automatisation de tests fonctionnels Sauce Demo")
    print(LIGNE)

    scenarios = [
        ("Scenario 1 — Connexion reussie",    test_scenario1_connexion_reussie),
        ("Scenario 2 — Connexion refusee",    test_scenario2_connexion_refusee),
        ("Scenario 3 — Ajout au panier",      test_scenario3_ajout_panier),
        ("Scenario 4 — Parcours achat complet", test_scenario4_achat_complet),
        ("Scenario 5 — Deconnexion",          test_scenario5_deconnexion),
    ]

    resultats = []

    for nom, scenario in scenarios:
        driver = creer_driver()
        try:
            scenario(driver)
            resultats.append((nom, "REUSSI", None))
            logger.info(f"{nom} : REUSSI")
        except Exception as e:
            import traceback
            traceback.print_exc()
        finally:
            driver.quit()

    # Rapport final
    print(f"\n{LIGNE}")
    print("RAPPORT FINAL")
    print(LIGNE)
    for nom, statut, erreur in resultats:
        symbole = "OK" if statut == "REUSSI" else "KO"
        print(f"  [{symbole}] {nom}")
        if erreur:
            print(f"       Erreur : {erreur}")

    reussis = sum(1 for _, s, _ in resultats if s == "REUSSI")
    print(f"\n{reussis}/{len(resultats)} scenarios reussis")
    print(LIGNE)


if __name__ == "__main__":
    main()
