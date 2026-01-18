# 📊 Guide de Présentation - Mini-Projet TALN

## Structure de l'Exposé (15 minutes total)

### PARTIE A: ARTICLE SCIENTIFIQUE (8 minutes)

#### Slide 1: Couverture Article
- **Titre de l'article** [À COMPLÉTER]
- **Auteurs** [À COMPLÉTER]
- **Année** [À COMPLÉTER]
- **Journal/Conférence** [À COMPLÉTER]

#### Slide 2: Contexte & Motivation (1 min)
**Points clés:**
- Pourquoi ce domaine? (IA générative, dialogue, NLP)
- Importance du problème
- Gap dans la littérature

#### Slide 3: Objectif de Recherche (1 min)
**Expliciter:**
- Question de recherche principale
- Hypothèses de base
- Objectifs spécifiques

#### Slide 4: Méthodologie (2 min)
**Sections:**
- Architecture du système
- Données d'entraînement (taille, source)
- Approche technique (modèle, algorithme)
- Hyperparamètres principaux

**Suggestion visuelle:** Diagramme d'architecture

#### Slide 5: Résultats (2 min)
**Afficher:**
- Tableau comparatif des résultats
- Graphiques de performance
- Métriques principales (BLEU, ROUGE, accuracy, etc.)
- Comparaison avec baselines

**Suggestion visuelle:** Graphiques/tableaux

#### Slide 6: Limites & Critique (1 min)
**Analyser:**
- Limitations méthodologiques
- Points forts de l'approche
- Points faibles/améliorations possibles
- Reproductibilité

#### Slide 7: Conclusion Article (1 min)
- Contribution principale
- Implication pour le domaine
- Questions ouvertes

---

### PARTIE B: VOTRE CHATBOT (7 minutes)

#### Slide 8: Introduction Projet
**Contenu:**
- 🇹🇳 Domaine: Tourisme en Tunisie
- Motivation du choix
- Vue globale du projet

#### Slide 9: Cas d'Usage & Définition (1 min)
**Définir:**
- Destinataires (touristes français, européens)
- Problème à résoudre (assistance touristique)
- Avantages d'un chatbot
- Cas d'usage types

#### Slide 10: Méthodologie Technique (1.5 min)
**Couvrir:**

**Architecture:**
```
Input → Preprocessing → Intention Detection 
→ Strategy Selection → Response Generation → Output
```

**Techniques NLP:**
- TF-IDF Vectorization (FAQ matching)
- Pattern Matching (destinations, activités)
- Entity Extraction (noms, types)

**Corpus:**
- 7 destinations touristiques
- 6 questions FAQ
- 5 catégories d'activités
- 4+ hôtels recommandés

#### Slide 11: Données & Base de Connaissance (1 min)
**Montrer:**
```json
{
  "destinations": 7,
  "attractions": 20+,
  "hotels": 4+,
  "activities": 5,
  "faq": 6
}
```

**Structure JSON:**
- Destinations (nom, région, attractions)
- Activités (type, locations)
- Hôtels (nom, stars, prix)
- FAQ (question, réponse)

**Visualisation:** Capture d'écran du JSON

#### Slide 12: Réalisation & Implémentation (1.5 min)
**Détails techniques:**
- **Langage:** Python 3.8+
- **Librairies:** scikit-learn, numpy
- **Architecture modulaire:**
  - `chatbot.py`: Moteur principal (350+ lignes)
  - `tunisia_tourism_data.json`: Base de données
  - Tests unitaires (25+ tests)

**Code snippet exemple:**
```python
# TF-IDF Matching
similarities = cosine_similarity(user_vector, faq_matrix)
best_idx = np.argmax(similarities)
answer = faq_database[best_idx][1]
```

#### Slide 13: Démonstration Live (1.5 min)
**Préparer à l'avance:**

**Dialogue 1: Destination**
```
Utilisateur: "Parlez-moi de Djerba"
Réponse: [Info détaillée + attractions]
```

**Dialogue 2: Activité**
```
Utilisateur: "Je veux faire un safari"
Réponse: [Recommandation activité + locations]
```

**Dialogue 3: FAQ**
```
Utilisateur: "Ai-je besoin d'un visa?"
Réponse: [Réponse FAQ détaillée]
```

**Dialogue 4: Hôtel**
```
Utilisateur: "Hôtels à Hammamet?"
Réponse: [Liste hôtels filtrés]
```

#### Slide 14: Résultats & Performance (0.5 min)
**Métriques:**
- Destinations couvertes: 7/7 (100%)
- Questions FAQ: 6/6 (100%)
- Activités: 5/5 (100%)
- Temps réponse: < 100ms
- Tests passés: 25/25 ✅

#### Slide 15: Limitations & Améliorations (1 min)
**Limitations actuelles:**
- Pas de mémoire contextuelle avancée
- Réponses basées sur templates
- Base de données statique
- Sensibilité orthographique

**Améliorations possibles:**
- Embedding models (Word2Vec, FastText)
- Modèles seq2seq
- Gestion du contexte
- API externes (booking, météo)
- Support multilingue

#### Slide 16: Conclusion & Impact (0.5 min)
**Points clés:**
- ✅ Chatbot fonctionnel et testable
- ✅ Approche NLP pertinente
- ✅ Cas d'usage réaliste
- ✅ Base pour améliorations futures

**Merci!**

---

## 🎯 Conseils de Présentation

### Timing
```
Slide 1-7:   Article (8 min)
- 1 min/slide pour contextualisation
- 2 min pour résultats et critique

Slide 8-16:  Chatbot (7 min)
- 1 min architecture/technique
- 1-2 min démo live
- 0.5 min améliorations
```

### Pratiques Recommandées

**Avant la présentation:**
- ✅ Tester toutes les démos
- ✅ Avoir le chatbot en mode interactif
- ✅ Préparer 3-4 exemples de dialogue
- ✅ Vérifier les connexions/écran partagé

**Pendant la présentation:**
- 🎤 Parler clairement et lentement
- 👁️ Maintenir contact avec audience
- 📊 Montrer des graphiques/diagrammes
- 🎬 Faire la démo en live si possible

**Organisation:**
- Utiliser PDF ou PowerPoint pour slides
- Avoir une copie du code à proximité
- Lire les slides ne suffit pas: ajouter commentaires

### Contenu des Slides

**Pour chaque slide:**
- ✅ Titre clair et descriptif
- ✅ Points à puces (pas de paragraphes)
- ✅ Visuel: graphiques, diagrammes, images
- ✅ Font lisible (min 28pt pour texte)
- ✅ Peu de texte (8-10 lignes max)

**Couleurs suggérées:**
- 🇹🇳 Bleu/blanc/rouge (couleurs Tunisie)
- Fond clair avec texte sombre
- Surligner points clés

---

## 📝 Script de Présentation (Notes)

### Partie A: Article (8 min)

**Slide 1 (30s):** "Nous présentons aujourd'hui [article]... Ce travail s'inscrit dans le contexte..."

**Slide 2-3 (1.5 min):** "Le problème adressé est... L'article propose..."

**Slide 4 (2 min):** "La méthodologie combine... Ils utilisent un modèle [description]... Le corpus contient..."

**Slide 5 (2 min):** "Les résultats montrent... Comparer aux baselines... Performance: [métrique]..."

**Slide 6 (1 min):** "Notre critique: les forces incluent... Les limitations incluent..."

**Slide 7 (1 min):** "En conclusion, cet article contribue en montrant..."

### Partie B: Chatbot (7 min)

**Slide 8 (1 min):** "Pour notre projet, nous avons choisi le tourisme en Tunisie... Motivation..."

**Slide 9-10 (1.5 min):** "Notre chatbot aide les touristes à... Il utilise TF-IDF pour faire correspondre les FAQ... et pattern matching pour..."

**Slide 11 (1 min):** "Notre base de données contient... Voici la structure..."

**Slide 12 (1 min):** "Techniquement, nous utilisons Python, scikit-learn... Le code est modulaire..."

**Slide 13 (1.5 min):** [Démo live] "Voyons comment ça marche en pratique..."

**Slide 14-15 (1 min):** "Les résultats montrent 100% de couverture... Les améliorations futures pourraient inclure..."

**Slide 16 (0.5 min):** "Merci for your attention. Questions?"

---

## 🎬 Démo Live - Checklist

**Avant de commencer:**
- [ ] Chatbot démarré et testé
- [ ] Terminal/interface propre
- [ ] Exemples préparés et testés
- [ ] Taille police lisible (30+)
- [ ] Connection internet (si nécessaire)

**Exemples à préparer:**
- [ ] 1. Accueil: "Bonjour"
- [ ] 2. Destination: "Djerba" ou "Sousse"
- [ ] 3. Activité: "Plage" ou "Désert"
- [ ] 4. FAQ: "Visa?" ou "Meilleure époque?"
- [ ] 5. Hôtels: "Hôtels à Hammamet"

**Gestion des erreurs:**
- Si ça crash: avoir une capture d'écran de backup
- Si ça ralentit: rester calme, montrer output pré-enregistré
- Si question compliquée: "Bonne question, on peut l'explorer après"

---

## 📚 Ressources

### Pour les slides:
- Google Slides / PowerPoint / LibreOffice Impress
- Thème avec couleurs Tunisie
- Polices: sans-serif (Arial, Helvetica, Roboto)

### Visuals utiles:
- 🗺️ Carte Tunisie avec destinations
- 🏖️ Photos des destinations
- 📊 Graphiques des résultats
- 🤖 Diagramme du chatbot

### Timing
```
Article (8 min)       = 7 slides × ~1.1 min/slide
Chatbot (7 min)       = 8 slides + démo
Buffer                = ~30s pour transitions
Total                 = 15 min
```

---

## ✅ Checklist Finale

**Contenu:**
- [ ] Article scientifique sélectionné et analysé
- [ ] Chatbot complètement fonctionnel
- [ ] Démos préparées et testées
- [ ] Toutes les 15+ slides préparées
- [ ] Notes de présentation écrites

**Technique:**
- [ ] Code téléchargé et exécutable
- [ ] Démo opérationnelle
- [ ] Slides prêtes (PDF ou PPTX)
- [ ] Rapport 3-5 pages (si requis)

**Équipe:**
- [ ] Rôles définis (qui parle quelle partie)
- [ ] Entraînement/répétitions
- [ ] Accord sur le style de présentation
- [ ] Timing pratiqué

---

**Bonne chance pour votre présentation! 🇹🇳✨**
