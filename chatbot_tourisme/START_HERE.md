# DÉMARRAGE RAPIDE - Tunisia Tourism Chatbot

## 🇹🇳 Bienvenue!

Ce document vous guide pour utiliser immédiatement le chatbot.

---

## ⚡ 30 SECONDES POUR DÉMARRER

### Option 1: Mode Interactif (Recommandé pour test)
```bash
python src/chatbot.py
```
Puis tapez: `Bonjour` → `Djerba` → `Aide` → `Au revoir`

### Option 2: Démo Automatique (20+ dialogues)
```bash
python demo.py
```

### Option 3: Interface Graphique Menu
```bash
python main.py
```
Choisissez l'option 1, 2 ou 3

---

## 📋 PRÉ-REQUIS

```bash
# Installation dépendances (une seule fois)
pip install scikit-learn numpy

# Vérifier installation
python demo.py
```

**Attention:** Pour Windows PowerShell, utiliser `python.exe` au lieu de `python`

---

## 🎯 5 QUESTIONS CLÉS POUR TESTER

Essayez ces questions dans le chatbot interactif:

```
1️⃣  Bonjour
    → Réponse d'accueil avec capacités

2️⃣  Parlez-moi de Djerba
    → Information détaillée sur la destination

3️⃣  Quelles plages?
    → Recommandation d'activité

4️⃣  Ai-je besoin d'un visa?
    → Réponse FAQ

5️⃣  Au revoir
    → Message de fermeture
```

---

## 📁 FICHIERS IMPORTANTS

| Fichier | Rôle |
|---------|------|
| `src/chatbot.py` | 💎 Moteur du chatbot |
| `demo.py` | 🎬 Démonstration automatique |
| `test_chatbot.py` | ✅ Tests (24/24 passants) |
| `data/tunisia_tourism_data.json` | 📊 Base de données |
| `README.md` | 📖 Guide complet |
| `main.py` | 🎛️ Interface menu |

---

## 🎓 POUR LA PRÉSENTATION

### 1. Préparer l'Exposé
```
Lire: presentation/GUIDE_PRESENTATION.md
Durée: 15 minutes total (8 min article + 7 min chatbot)
```

### 2. Préparer les Dialogues
```
Utiliser: docs/EXEMPLES_DIALOGUES.md
Ou lancer: python demo.py
```

### 3. Tester la Démo
```
python demo.py
# Pratiquer 3-4 fois avant la présentation
```

---

## ✨ CAPACITÉS PRINCIPALES

🏖️ **7 Destinations** - Djerba, Tunis, Hammamet, Sousse, Tataouine, Carthage, Tozeur

❓ **6 Questions FAQ** - Visa, monnaie, langue, transport, meilleure époque, sécurité

🎯 **5 Activités** - Plages, désert, histoire, oasis, sports nautiques

🏨 **Hôtels** - Recommandations par destination

🤖 **NLP** - TF-IDF matching + pattern matching

---

## 🧪 VÉRIFIER L'INSTALLATION

```bash
# Vérifier les tests (doit afficher OK)
python test_chatbot.py

# Doit afficher: "Ran 24 tests in X.XXs OK"
```

---

## ❌ DÉPANNAGE

**Problème:** `No module named sklearn`
```bash
pip install scikit-learn numpy
```

**Problème:** Fichier JSON non trouvé
```bash
# Assurer d'être dans le répertoire du projet
cd chatbot_tourisme
python demo.py
```

**Problème:** Erreur "command not found"
```bash
# Windows PowerShell
python.exe demo.py

# Linux/Mac
python3 demo.py
```

---

## 📞 BESOIN D'AIDE?

| Question | Réponse |
|----------|---------|
| Comment utiliser le chatbot? | Lire `README.md` |
| Comment préparer l'exposé? | Lire `presentation/GUIDE_PRESENTATION.md` |
| Quels dialogues utiliser? | Voir `docs/EXEMPLES_DIALOGUES.md` |
| Architecture du projet? | Voir `INDEX.md` |
| Comment tester? | Lancer `python test_chatbot.py` |

---

## ✅ CHECKLIST AVANT PRÉSENTATION

- [ ] Python et dépendances installés (`pip install -r requirements.txt`)
- [ ] Démo testée (`python demo.py`)
- [ ] Tests vérifiés (`python test_chatbot.py`)
- [ ] 5-6 dialogues préparés et pratiqués
- [ ] Article scientifique sélectionné et analysé
- [ ] Slides PowerPoint préparées
- [ ] Timing pratiqué (15 minutes exactement)

---

## 🎉 C'EST PRÊT!

Vous avez tout ce qu'il faut pour:
✅ Exécuter le chatbot
✅ Faire une démo live
✅ Passer les tests
✅ Présenter un projet complet

**Bonne chance! 🇹🇳**

---

## 📊 RÉSUMÉ PROJET

```
Domaine:          Tourisme en Tunisie
Technique NLP:    TF-IDF + Pattern Matching
Lignes de code:   350+
Tests:            24/24 passants ✅
Documentation:    15+ pages
Démo:             20+ dialogues
État:             PRÊT POUR PRÉSENTATION ✨
```

---

**Pour commencer maintenant:**
```bash
python demo.py
```

ou

```bash
python src/chatbot.py
```

Tapez votre première question! 💬
