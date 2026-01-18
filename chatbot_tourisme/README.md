# 🇹🇳 Chatbot Touristique Tunisie - Mini-Projet TALN

## Vue d'ensemble

Chatbot spécialisé pour l'assistance touristique en Tunisie, utilisant NLP avec TF-IDF et correspondance de patterns pour fournir des recommandations de destinations, d'activités et d'hébergements.

### Domaine
**Tourisme en Tunisie** - Assistance pour planification de voyage, recommandations de destinations et informations pratiques

---

## 📋 Fonctionnalités

### 1. **FAQ Interactif**
- Réponses aux questions courantes (visa, monnaie, langue, transport, sécurité, meilleure période)
- Utilise TF-IDF pour correspondance sémantique
- Seuil de confiance pour filtrer les mauvaises correspondances

### 2. **Recommandations de Destinations**
- 7 destinations principales en Tunisie (Djerba, Tunis, Hammamet, Sousse, Tataouine, Carthage, Tozeur)
- Informations détaillées: attractions, meilleure période, hébergements
- Extraction automatique de destinations mentionnées

### 3. **Recommandations d'Activités**
- Plages, safaris désertiques, oasis, histoire/culture, sports nautiques
- Recommandations basées sur le type d'activité

### 4. **Recommandations d'Hôtels**
- Base de données avec hôtels par destination
- Informations: catégorie (étoiles), gamme de prix, description

### 5. **Informations Pratiques**
- Électricité, urgences, santé, douanes

---

## 🔧 Technologie

### Approche NLP
- **TF-IDF Vectorization**: Correspondance sémantique pour FAQ
- **Pattern Matching**: Extraction de destinations et d'activités
- **Keyword-based Routing**: Détection d'intentions utilisateur

### Dépendances
```
scikit-learn >= 1.0.0 (optionnel, pour TF-IDF amélioré)
numpy >= 1.20.0 (optionnel)
```

> **Note**: Le chatbot fonctionne sans sklearn avec un fallback sur la correspondance par mots-clés

---

## 📁 Structure du Projet

```
chatbot_tourisme/
├── src/
│   └── chatbot.py              # Moteur principal du chatbot
├── data/
│   └── tunisia_tourism_data.json # Base de données touristique
├── demo.py                      # Script de démonstration
├── test_chatbot.py             # Tests unitaires
├── requirements.txt            # Dépendances Python
└── README.md                   # Ce fichier
```

---

## 🚀 Installation et Exécution

### 1. Installation des dépendances

```bash
# Installation minimale (fonctionnement garanti)
pip install numpy

# Installation complète (avec TF-IDF optimisé)
pip install -r requirements.txt
```

### 2. Exécution du Chatbot

**Mode interactif:**
```bash
python src/chatbot.py
```

**Démonstration automatique:**
```bash
python demo.py
```

**Tests:**
```bash
python test_chatbot.py
```

---

## 💬 Exemples d'Interactions

### Exemple 1: Demande de destination
```
Utilisateur: Parlez-moi de Djerba
Chatbot: 🏖️ Djerba (Sud-Est)
Description: Île méditerranéenne célèbre pour ses plages...
Attractions: Musée du Linge Traditionnel, Île de Flamingo, Synagogue de la Ghriba
Meilleure période: Avril à Octobre
Hébergement: Hôtels 3-5 étoiles, Resorts
```

### Exemple 2: Demande d'activités
```
Utilisateur: Je veux faire un safari dans le désert
Chatbot: Exploration du Sahara avec chameaux ou 4x4
Lieux recommandés: Tataouine, Tozeur
```

### Exemple 3: Question FAQ
```
Utilisateur: Ai-je besoin d'un visa?
Chatbot: Les ressortissants de l'UE, Suisse, Norvège ne nécessitent 
pas de visa pour 90 jours...
```

### Exemple 4: Demande d'hôtel
```
Utilisateur: Hôtels à Hammamet
Chatbot: Hôtels recommandés à Hammamet:
- Sheraton Tunisie (5⭐)
  Luxury resort avec plage privée, restaurants gastronomiques
  Gamme de prix: Élevée
```

---

## 🎯 Méthodologie

### Architecture
1. **Chargement des données** → JSON avec destinations, FAQ, hôtels, activités
2. **Prétraitement** → TF-IDF vectorization et construction de la base de connaissances
3. **Traitement d'entrée** → Détection d'intention et extraction d'entités
4. **Sélection de réponse** → Pattern matching hiérarchisé + similarité TF-IDF
5. **Génération de réponse** → Formattage et enrichissement d'informations

### Flux de Décision
```
Entrée utilisateur
    ↓
[Salutation?] → Réponse accueil
    ↓
[Destination mentionnée?] → Info détaillée
    ↓
[Activité demandée?] → Recommandation activité
    ↓
[Question FAQ?] → Recherche TF-IDF
    ↓
[Aide demandée?] → Afficher guide
    ↓
[Défaut] → Suggestion de reformulation
```

---

## 📊 Base de Données

### Destinations (7)
- **Nord**: Tunis, Carthage, Hammamet
- **Est**: Sousse
- **Sud-Est**: Djerba
- **Sud**: Tataouine, Tozeur

### FAQ (6 questions)
- Visa et documents
- Monnaie et paiements
- Langue
- Transport
- Meilleure période
- Sécurité

### Activités (5 types)
- Plages
- Safari désertique
- Histoire et culture
- Oasis
- Sports nautiques

---

## 🔍 Détails Techniques

### TF-IDF Configuration
- **n-grams**: (1, 2) - unigrammes et bigrammes
- **Stop words**: Mots français courants
- **Max features**: 100
- **Seuil de confiance**: 0.15

### Pattern Matching
- Expressions régulières pour entités
- Extraction par mots-clés
- Correspondance insensible à la casse

---

## 📈 Améliorations Possibles

1. **NLP Avancé**
   - Modèles d'embedding (Word2Vec, FastText)
   - Modèles seq2seq pour génération de réponses
   - Analyse de sentiment

2. **Dialogue Plus Naturel**
   - Gestion du contexte conversationnel multi-tours
   - Anaphore et résolution de références
   - Questions de clarification

3. **Données Enrichies**
   - Base de restaurants/cafés
   - Informations météorologiques
   - Calendrier d'événements
   - Intégration avec APIs (booking, musées, etc.)

4. **Fonctionnalités Avancées**
   - Réservation d'hôtels
   - Génération d'itinéraires personnalisés
   - Multi-modal (images, cartes)
   - Support multilingue (arabe, anglais)

5. **Apprentissage**
   - Collecte de feedback utilisateur
   - Fine-tuning de modèles
   - Détection de questions non traitées

---

## 🧪 Tests

Le fichier `test_chatbot.py` contient des tests pour:
- Chargement des données
- Correspondance TF-IDF
- Extraction d'entités
- Réponses pour chaque catégorie

Exécutez:
```bash
python test_chatbot.py
```

---

## 📝 Limitations et Considérations

### Limitations Actuelles
- Pas de mémoire conversationnelle avancée (context window limité)
- Réponses basées sur templates (pas de génération)
- Dépendance à la base de données statique
- Sensibilité aux variations orthographiques

### Opportunités d'Amélioration
- Intégration avec APIs externes (météo, réservations)
- Apprentissage actif et correction active
- Support des images et des cartes interactives
- Chatbot multilingue avec arabe/anglais

---

## 👥 Auteurs

**Mini-Projet TALN - Trinôme**
- Tourisme en Tunisie
- Année académique 2024-2025

---

## 📚 Références

### Données
- Informations touristiques vérifiées de la Tunisie
- Attractions et destinations principales

### Technologies
- scikit-learn: TF-IDF Vectorization
- NLP: Pattern Matching, Entity Extraction
- Python 3.8+

---

## 📄 Licence

Projet académique - Usage éducatif uniquement

---

## 📞 Support

Pour des questions ou des rapports de bugs, veuillez consulter la structure de test et la documentation du code.

---

**Bon voyage en Tunisie! 🇹🇳✈️**
