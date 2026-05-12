# TP3 — Automatisation de tests fonctionnels avec Selenium Python

Projet d'automatisation QA sur le site de démonstration e-commerce [Sauce Demo](https://www.saucedemo.com/).  
Il couvre cinq scénarios utilisateur complets, structurés avec le pattern **Page Object Model (POM)**, un système de logs et des captures d'écran automatiques.

---

## Site testé

**URL** : [https://www.saucedemo.com/](https://www.saucedemo.com/)

| Compte           | Mot de passe   | Comportement               |
|------------------|----------------|----------------------------|
| standard_user    | secret_sauce   | Connexion normale           |
| locked_out_user  | secret_sauce   | Connexion refusée           |

---

## Structure du projet

```
tP_3/
├── main.py                      # Point d'entrée — orchestre les cinq scénarios
├── requirements.txt             # Dépendances Python
├── README.md                    # Documentation du projet
├── pages/
│   ├── base_page.py             # Classe de base (waits, logs, screenshots)
│   ├── login_page.py            # Page de connexion
│   ├── inventory_page.py        # Page catalogue produits
│   ├── cart_page.py             # Page panier
│   ├── checkout_page.py         # Pages checkout (formulaire + récapitulatif)
│   └── checkout_complete_page.py# Page de confirmation de commande
├── tests/
│   └── test_tp3.py              # Les cinq scénarios de test
├── utils/
│   └── logger.py                # Configuration du logger Python
├── logs/                        # Fichiers de log générés automatiquement
└── screenshots/                 # Captures d'écran générées automatiquement
```

---

## Prérequis

- Python 3.8 ou supérieur
- Google Chrome installé
- ChromeDriver compatible avec votre version de Chrome

---

## Installation

**1. Cloner le repository**

```bash
git clone https://github.com/votre-utilisateur/tp3.git
cd tp3
```

**2. Créer un environnement virtuel**

```bash
python -m venv .venv
```

Activer l'environnement :

- Windows : `.venv\Scripts\activate`
- macOS / Linux : `source .venv/bin/activate`

**3. Installer les dépendances**

```bash
pip install -r requirements.txt
```

---

## Exécution

Depuis le dossier `TP_3/`, exécuter :

```bash
python main.py
```

Chaque scénario est exécuté dans un navigateur indépendant. Le rapport final s'affiche en console à la fin de l'exécution.

---

## Scénarios couverts

### Scenario 1 — Connexion reussie
Connexion avec `standard_user` et vérification de l'accès au catalogue produits.

### Scenario 2 — Connexion refusee
Tentative de connexion avec `locked_out_user` et vérification du message d'erreur.

### Scenario 3 — Ajout au panier
Ajout du produit `Sauce Labs Backpack`, vérification du bouton `Remove`, du badge panier et du contenu du panier. Screenshot automatique après ajout.

### Scenario 4 — Parcours d'achat complet
Connexion, ajout produit, validation panier, saisie des informations client (John Doe, 59000), vérification du récapitulatif (prix, taxe, total) et confirmation de commande. Screenshot automatique de la page de confirmation.

### Scenario 5 — Deconnexion
Connexion puis déconnexion via le menu burger, vérification du retour sur la page de login.

---

## Logs et captures d'écran

Les logs sont enregistrés dans le dossier `logs/` avec horodatage :

```
logs/tp3_2025-01-15_14-32-00.log
```

Les captures d'écran sont sauvegardées dans `screenshots/` :

- `scenario3_apres_ajout.png` — après ajout au panier
- `scenario4_confirmation.png` — page de confirmation de commande
- `erreur_<nom_scenario>.png` — en cas d'échec d'un scénario

---
