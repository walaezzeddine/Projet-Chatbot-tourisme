#!/usr/bin/env python3
"""
Quick Start Guide - Tunisia Tourism Chatbot
Run this file to launch the interactive chatbot
"""

import sys
from pathlib import Path

def main():
    """Main entry point for the chatbot."""
    print("\n" + "="*70)
    print("🇹🇳 CHATBOT TOURISTIQUE TUNISIE - MINI-PROJET TALN")
    print("="*70)
    print()
    print("Options:")
    print("  1. Mode interactif (chat en temps réel)")
    print("  2. Exécuter démo automatique")
    print("  3. Exécuter tests unitaires")
    print("  4. Afficher aide")
    print("  5. Quitter")
    print()
    
    while True:
        choice = input("Choisissez une option (1-5): ").strip()
        
        if choice == "1":
            run_interactive()
            break
        elif choice == "2":
            run_demo()
            break
        elif choice == "3":
            run_tests()
            break
        elif choice == "4":
            show_help()
            break
        elif choice == "5":
            print("Au revoir!")
            sys.exit(0)
        else:
            print("Option invalide. Veuillez entrer 1-5.")


def run_interactive():
    """Run the chatbot in interactive mode."""
    print("\nDémarrage du chatbot interactif...")
    from src.chatbot import TunisiaChatbot
    
    data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
    chatbot = TunisiaChatbot(str(data_path))
    
    print("\n" + "="*70)
    print("Tapez 'aide' pour voir les commandes, 'quitter' pour terminer")
    print("="*70 + "\n")
    
    # Run the interactive chat
    import src.chatbot as chatbot_module
    sys.modules['__main__'].__dict__.update(chatbot_module.__dict__)
    
    while True:
        try:
            user_input = input("Vous: ").strip()
            if not user_input:
                continue
            
            response = chatbot.chat(user_input)
            print(f"\nChatbot: {response}\n")
            
            if user_input.lower() in ['quitter', 'exit', 'au revoir', 'bye']:
                break
                
        except KeyboardInterrupt:
            print("\n\nAu revoir!")
            break


def run_demo():
    """Run the automatic demo."""
    print("\nExécution de la démonstration...")
    import subprocess
    result = subprocess.run([sys.executable, 'demo.py'], cwd=Path(__file__).parent)
    sys.exit(result.returncode)


def run_tests():
    """Run the unit tests."""
    print("\nExécution des tests unitaires...")
    import subprocess
    result = subprocess.run([sys.executable, 'test_chatbot.py'], cwd=Path(__file__).parent)
    sys.exit(result.returncode)


def show_help():
    """Show help information."""
    help_text = """
╔════════════════════════════════════════════════════════════════════╗
║         CHATBOT TOURISTIQUE TUNISIE - GUIDE RAPIDE               ║
╚════════════════════════════════════════════════════════════════════╝

📁 STRUCTURE DU PROJET:
  src/chatbot.py                    → Moteur du chatbot
  data/tunisia_tourism_data.json    → Base de données
  demo.py                           → Démo automatique
  test_chatbot.py                   → Tests unitaires
  README.md                         → Documentation complète

🚀 DÉMARRAGE RAPIDE:

1. Mode Interactif:
   python src/chatbot.py
   ou
   python main.py  (option 1)

2. Démo Automatique:
   python demo.py
   ou
   python main.py  (option 2)

3. Tests Unitaires:
   python test_chatbot.py
   ou
   python main.py  (option 3)

💡 EXEMPLES DE QUESTIONS:

• Destinations:
  "Parlez-moi de Djerba"
  "Qu'est-ce qu'il y a à Sousse?"
  "Je veux visiter Tozeur"

• Activités:
  "Je veux aller à la plage"
  "Safaris dans le désert"
  "Que peut-on faire à Tunis?"

• FAQ:
  "Ai-je besoin d'un visa?"
  "Quelle est la meilleure période?"
  "Quelle langue?"

• Hébergement:
  "Hôtels à Hammamet"
  "Où dormir à Sousse?"

• Aide:
  "Aide"
  "Quoi faire?"

🎯 CAPACITÉS DU CHATBOT:

✅ 7 destinations touristiques
✅ 6 questions FAQ complètes
✅ 5 catégories d'activités
✅ Recommandations d'hôtels
✅ Informations pratiques
✅ Historique de conversation
✅ NLP avec TF-IDF

📊 STATISTIQUES:

Tests passants:    24/24 ✅
Destinations:      7/7   (100%)
FAQ traitées:      6/6   (100%)
Activités:         5/5   (100%)
Temps réponse:     <100ms
Taille données:    ~5KB

📚 DOCUMENTATION:

README.md                          → Guide complet
docs/RAPPORT_TEMPLATE.md           → Template de rapport
docs/EXEMPLES_DIALOGUES.md         → 20+ dialogues
presentation/GUIDE_PRESENTATION.md → Guide d'exposé
INDEX.md                           → Index complet

🎓 POUR LA PRÉSENTATION:

1. Lire: presentation/GUIDE_PRESENTATION.md
2. Préparer: 5-6 dialogues clés
3. Tester: python demo.py
4. Pratiquer: timing de 15 minutes
5. Démo: python src/chatbot.py

❓ SUPPORT:

Consultez les fichiers documentation ou les commentaires du code.

═══════════════════════════════════════════════════════════════════════
Bonne chance! 🇹🇳✨
═══════════════════════════════════════════════════════════════════════
"""
    print(help_text)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        print("\nVérifiez que vous êtes dans le bon répertoire et que les")
        print("dépendances sont installées:")
        print("  pip install scikit-learn numpy")
        sys.exit(1)
