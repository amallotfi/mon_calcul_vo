# 💼 ComptaSmart: Calculateur de VO & TVA

**ComptaSmart** est une application web moderne et épurée développée en Python avec **Streamlit**. Elle permet aux comptables, entrepreneurs et gestionnaires de convertir instantanément un montant TTC (Toutes Taxes Comprises) en Valeur d'Origine HT (Hors Taxe) tout en calculant avec précision le montant exact de la TVA applicable.

---

## ✨ Fonctionnalités

- 📊 **Calcul Dynamique :** Conversion instantanée du montant TTC en HT.
- ⚙️ **Taux de TVA Personnalisable :** Possibilité de spécifier n'importe quel taux de TVA (ex: 20%, 14%, 10%, 7%).
- 🛡️ **Sécurité du Code :** Gestion rigoureuse des entrées utilisateurs pour éviter les erreurs de division par zéro (`taux_tva > 0`).
- 🎨 **Interface Professionnelle :** Affichage clair et structuré des résultats à l'aide de composants visuels colorés (Success/Info boxes).

---

## 🛠️ Technologies Utilisées

* **Python** (Logique métier et calculs)
* **Streamlit** (Framework d'interface utilisateur web)

---

## 💻 Installation et Lancement en Local

Pour exécuter ce projet sur votre machine locale, suivez ces étapes simples :

1. **Installer Streamlit (si ce n'est pas déjà fait) :**
   ```bash
   pip install streamlit
