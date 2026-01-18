# Exemples de Dialogues - Tunisia Tourism Chatbot

## 📋 Dialogues de Test et Démonstration

Ce document contient des dialogues pré-testés que vous pouvez utiliser pour la démonstration du chatbot.

---

## ✅ Exemple 1: Dialogue d'Accueil

```
👤 Utilisateur: Bonjour

🤖 Chatbot:
Bienvenue en Tunisie! Je suis votre assistant touristique. 🇹🇳
Comment puis-je vous aider? Vous pouvez me poser des questions sur:
- Les destinations touristiques
- Les activités à faire
- Les hôtels et hébergements
- Les informations pratiques
```

**Contexte:** Premier contact, démonstration des capacités

---

## ✅ Exemple 2: Information sur une Destination

```
👤 Utilisateur: Parlez-moi de Djerba

🤖 Chatbot:
🏖️ Djerba (Sud-Est)
Description: Île méditerranéenne célèbre pour ses plages de sable blanc et son patrimoine culturel
Attractions: Musée du Linge Traditionnel, Île de Flamingo, Synagogue de la Ghriba
Meilleure période: Avril à Octobre
Hébergement: Hôtels 3-5 étoiles, Resorts
```

**Points clés:** Affiche information structurée, atractif visuel

---

## ✅ Exemple 3: Détails Destinée Alterne (Tunis)

```
👤 Utilisateur: Qu'est-ce qu'il y a à Tunis?

🤖 Chatbot:
🏖️ Tunis (Nord)
Description: Capitale historique avec architecture ottomane et médina authentique
Attractions: Médina de Tunis, Musée du Bardo, Parc du Belvédère, Cathédrale de Tunis
Meilleure période: Octobre à Avril
Hébergement: Hôtels 2-5 étoiles, Auberges
```

**Variante:** Même type de réponse, destination différente

---

## ✅ Exemple 4: Recommandation d'Activité

```
👤 Utilisateur: Je veux aller à la plage

🤖 Chatbot:
Plages méditerranéennes avec eaux turquoise
Lieux recommandés: Djerba, Hammamet, Sousse
```

**Contexte:** Identification d'activité par mots-clés

---

## ✅ Exemple 5: Safari Désertique

```
👤 Utilisateur: Quels sont les safaris dans le désert?

🤖 Chatbot:
Exploration du Sahara avec chameaux ou 4x4
Lieux recommandés: Tataouine, Tozeur
```

**Contexte:** Variante sur les activités

---

## ✅ Exemple 6: Question FAQ - Visa

```
👤 Utilisateur: Ai-je besoin d'un visa pour la Tunisie?

🤖 Chatbot:
Les ressortissants de l'UE, Suisse, Norvège ne nécessitent pas de visa pour 90 jours.
Les autres nationalités doivent vérifier les conditions auprès de leur consulat tunisien.
```

**Contexte:** Utilise TF-IDF matching pour FAQ

---

## ✅ Exemple 7: Question FAQ - Monnaie

```
👤 Utilisateur: Quelle est la devise?

🤖 Chatbot:
La monnaie est le Dinar Tunisien (TND). Le taux de change est approximativement 
1 EUR = 3.3 TND. Les cartes de crédit sont acceptées dans la plupart des hôtels 
et commerces modernes.
```

---

## ✅ Exemple 8: Recommandation d'Hôtel

```
👤 Utilisateur: Hôtels à Hammamet

🤖 Chatbot:
Hôtels recommandés à Hammamet:

- Sheraton Tunisie (5⭐)
  Luxury resort avec plage privée, restaurants gastronomiques
  Gamme de prix: Élevée
```

**Contexte:** Filtrage par destination

---

## ✅ Exemple 9: Gestion du Contexte Multiple

```
👤 Utilisateur: Je veux visiter Tunis et Sousse

🤖 Chatbot:
🏖️ Tunis (Nord)
Description: Capitale historique avec architecture ottomane et médina authentique
Attractions: Médina de Tunis, Musée du Bardo, Parc du Belvédère, Cathédrale de Tunis
Meilleure période: Octobre à Avril
Hébergement: Hôtels 2-5 étoiles, Auberges
---

🏖️ Sousse (Côte Est)
Description: Port historique et station balnéaire populaire, centre du tourisme tunisien
Attractions: Ribat de Sousse, Musée Archéologique, Médina de Sousse, Plages urbaines
Meilleure période: Mai à Octobre
Hébergement: Hôtels 3-5 étoiles, Resorts
```

**Points clés:** Traitement de multiple destination

---

## ✅ Exemple 10: Oasis et Désert

```
👤 Utilisateur: Parlez-moi de Tozeur

🤖 Chatbot:
🏖️ Tozeur (Sud-Ouest)
Description: Oasis berbère au cœur du Sahara avec architecture traditionnelle unique
Attractions: Oasis de Tozeur, Montagne de Chebika, Canyon de Tamerza, Lac salé de Chott El Djerid
Meilleure période: Octobre à Mars
Hébergement: Petits hôtels, Guesthouses de charme
```

---

## ✅ Exemple 11: Information Pratique - Transport

```
👤 Utilisateur: Comment se déplacer en Tunisie?

🤖 Chatbot:
Options: vols intérieurs, louage (taxi partagé), trains, bus. 
La location de voiture est recommandée pour explorer le sud.
```

---

## ✅ Exemple 12: Meilleure Période

```
👤 Utilisateur: Quel est le meilleur moment pour visiter?

🤖 Chatbot:
De mars à mai et septembre à novembre offrent un climat idéal. 
L'été (juin-août) est très chaud mais idéal pour la baignade. 
L'hiver (décembre-février) est doux.
```

---

## ✅ Exemple 13: Sécurité

```
👤 Utilisateur: Est-ce sûr de visiter la Tunisie?

🤖 Chatbot:
La Tunisie est généralement sûre pour les touristes. 
Évitez les zones frontalières sud. 
Prenez les précautions habituelles (pickpockets dans les villes).
```

---

## ✅ Exemple 14: Demande d'Aide

```
👤 Utilisateur: Aide

🤖 Chatbot:
Voici comment je peux vous aider:
1. Destinations: 'Parlez-moi de Djerba', 'Qu'est-ce qu'il y a à Sousse?'
2. Activités: 'Quelles plages?', 'Safaris dans le désert'
3. Hôtels: 'Hôtels à Djerba', 'Logements à Tunis'
4. Informations: 'Visa?', 'Quelle langue?', 'Meilleure époque?'
5. Autre: 'Au revoir', 'Merci'
```

---

## ✅ Exemple 15: Requête Inconnue

```
👤 Utilisateur: [Quelque chose de non prévu]

🤖 Chatbot:
Je n'ai pas bien compris. 😊
Pouvez-vous reformuler? Ou tapez 'aide' pour voir mes capacités.
```

---

## ✅ Exemple 16: Patrimoine Culturel

```
👤 Utilisateur: Quels sites historiques à Carthage?

🤖 Chatbot:
🏖️ Carthage (Banlieue Nord)
Description: Site historique de l'ancienne civilisation romaine et carthaginoise
Attractions: Ruines de Carthage, Musée de Carthage, Thermes d'Antonin, Plages historiques
Meilleure période: Octobre à Avril
Hébergement: Hôtels 3-4 étoiles
```

---

## ✅ Exemple 17: Région du Sud

```
👤 Utilisateur: J'aime les paysages désertiques

🤖 Chatbot:
Exploration du Sahara avec chameaux ou 4x4
Lieux recommandés: Tataouine, Tozeur
```

---

## ✅ Exemple 18: Combinaison - Destination + Activité

```
👤 Utilisateur: Plages à Djerba

🤖 Chatbot:
🏖️ Djerba (Sud-Est)
Description: Île méditerranéenne célèbre pour ses plages de sable blanc et son patrimoine culturel
Attractions: Musée du Linge Traditionnel, Île de Flamingo, Synagogue de la Ghriba
Meilleure période: Avril à Octobre
Hébergement: Hôtels 3-5 étoiles, Resorts

---

Plages méditerranéennes avec eaux turquoise
Lieux recommandés: Djerba, Hammamet, Sousse
```

---

## ✅ Exemple 19: Langue

```
👤 Utilisateur: Quelle langue parle-t-on en Tunisie?

🤖 Chatbot:
La langue officielle est l'arabe. Le français est largement parlé, notamment dans le tourisme. 
L'anglais est compris dans les hôtels touristiques.
```

---

## ✅ Exemple 20: Fin de Conversation

```
👤 Utilisateur: Au revoir

🤖 Chatbot:
Au revoir et bon voyage en Tunisie! 👋
```

---

## 📊 Résumé Statistique

| Type de Dialogue | Nombre d'Exemples | Couverture |
|-----------------|-----------------|-----------|
| Accueil | 2 | Salutations |
| Destinations | 8 | 7/7 destinations |
| Activités | 3 | 5/5 activités |
| FAQ | 5 | 6/6 questions |
| Hôtels | 1 | Hébergements |
| Aide | 1 | Help system |
| Fin | 1 | Termination |
| Erreurs | 1 | Error handling |
| **TOTAL** | **22** | **100% coverage** |

---

## 🎯 Utilisation Recommandée

### Pour la Démo Live (5-7 minutes)
Choisir **5-6 dialogues variés**:
1. Accueil: Exemple 1
2. Destination: Exemple 2 ou 3
3. Activité: Exemple 4
4. FAQ: Exemple 6 ou 7
5. Hôtel: Exemple 8

### Pour les Tests Automatisés
Utiliser tous les **22 exemples** pour validation complète

### Pour la Documentation
Utiliser les **exemples structurés** dans rapports/slides

---

## 💡 Conseils pour la Démonstration

**✅ Faites:**
- Parler en français avec accent naturel
- Laisser le chatbot répondre complètement
- Lire les réponses à haute voix pour l'audience
- Montrer les informations structurées
- Pointer les emoji et formatage

**❌ Évitez:**
- Poser questions trop compliquées hors du scope
- Interrompre les réponses
- Murmurer les réponses
- Taper trop rapidement
- Laisser le silence après les réponses

---

## 📱 Format de Copie-Pâte

Pour tester rapidement dans le chatbot:

```
Bonjour
Parlez-moi de Djerba
Je veux aller à la plage
Ai-je besoin d'un visa?
Hôtels à Hammamet
Aide
Au revoir
```

Copier-coller ligne par ligne et appuyer sur Entrée après chaque.

---

**Utilisez ces exemples pour une démonstration fluide et convaincante! 🇹🇳✨**
