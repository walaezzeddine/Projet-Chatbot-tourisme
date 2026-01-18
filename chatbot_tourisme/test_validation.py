#!/usr/bin/env python3
"""
Script de validation du chatbot avec tests automatisés
Teste différentes questions et vérifie les réponses
"""

from pathlib import Path
from src.chatbot import TunisiaChatbot
import json


class ChatbotValidator:
    """Valide les réponses du chatbot avec des cas de test."""
    
    def __init__(self):
        data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
        self.chatbot = TunisiaChatbot(str(data_path))
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_results = []
    
    def test_question(self, question: str, expected_keywords: list, description: str):
        """
        Teste une question et vérifie si la réponse contient les mots-clés attendus.
        
        Args:
            question: La question à poser
            expected_keywords: Liste de mots-clés qui doivent apparaître dans la réponse
            description: Description du test
        """
        print(f"\n{'='*80}")
        print(f"TEST: {description}")
        print(f"Question: {question}")
        print(f"Mots-clés attendus: {', '.join(expected_keywords)}")
        print('-'*80)
        
        response = self.chatbot.chat(question)
        print(f"Réponse: {response[:200]}..." if len(response) > 200 else f"Réponse: {response}")
        
        # Vérifier si tous les mots-clés sont présents
        response_lower = response.lower()
        found_keywords = [kw for kw in expected_keywords if kw.lower() in response_lower]
        missing_keywords = [kw for kw in expected_keywords if kw.lower() not in response_lower]
        
        success = len(missing_keywords) == 0
        
        if success:
            print(f"✅ SUCCÈS - Tous les mots-clés trouvés")
            self.passed_tests += 1
        else:
            print(f"❌ ÉCHEC - Mots-clés manquants: {', '.join(missing_keywords)}")
            self.failed_tests += 1
        
        self.test_results.append({
            'description': description,
            'question': question,
            'response': response,
            'expected_keywords': expected_keywords,
            'found_keywords': found_keywords,
            'missing_keywords': missing_keywords,
            'success': success
        })
        
        return success
    
    def run_all_tests(self):
        """Exécute tous les tests de validation."""
        
        print("\n" + "="*80)
        print("🧪 VALIDATION DU CHATBOT TOURISTIQUE TUNISIE")
        print("="*80)
        
        # Test 1: Salutations
        self.test_question(
            "Bonjour",
            ["bienvenue", "tunisie", "assistant"],
            "Salutation basique"
        )
        
        # Test 2: Information sur une destination
        self.test_question(
            "Parle-moi de Djerba",
            ["djerba", "île", "plage"],
            "Information sur destination - Djerba"
        )
        
        # Test 3: Information sur Tunis
        self.test_question(
            "Qu'est-ce que je peux visiter à Tunis?",
            ["tunis", "médina", "bardo"],
            "Attractions à Tunis"
        )
        
        # Test 4: Activités plage
        self.test_question(
            "Où trouver les meilleures plages?",
            ["plage", "djerba", "hammamet"],
            "Recommandations de plages"
        )
        
        # Test 5: Hôtels à Hammamet
        self.test_question(
            "Quels sont les hôtels recommandés à Hammamet?",
            ["hammamet", "hôtel", "étoile"],
            "Recommandations d'hôtels à Hammamet"
        )
        
        # Test 6: Désert et Sahara
        self.test_question(
            "Je veux visiter le désert du Sahara",
            ["sahara", "désert", "douz"],
            "Activités désert"
        )
        
        # Test 7: Question visa
        self.test_question(
            "Ai-je besoin d'un visa pour la Tunisie?",
            ["visa", "pas besoin", "90 jours"],
            "Information visa"
        )
        
        # Test 8: Monnaie
        self.test_question(
            "Quelle est la monnaie en Tunisie?",
            ["dinar", "tnd", "monnaie"],
            "Information monnaie"
        )
        
        # Test 9: Meilleure période
        self.test_question(
            "Quel est le meilleur moment pour visiter la Tunisie?",
            ["avril", "mai", "octobre"],
            "Meilleure période de visite"
        )
        
        # Test 10: Transport
        self.test_question(
            "Comment se déplacer en Tunisie?",
            ["taxi", "louage", "bus"],
            "Moyens de transport"
        )
        
        # Test 11: Sécurité
        self.test_question(
            "La Tunisie est-elle sûre pour les touristes?",
            ["sûr", "sécurit", "touriste"],
            "Question sécurité"
        )
        
        # Test 12: Langue
        self.test_question(
            "Quelle langue parle-t-on en Tunisie?",
            ["arabe", "français", "langue"],
            "Langues parlées"
        )
        
        # Test 13: Carthage
        self.test_question(
            "Que visiter à Carthage?",
            ["carthage", "ruine", "romain"],
            "Sites à Carthage"
        )
        
        # Test 14: Kairouan
        self.test_question(
            "Raconte-moi sur Kairouan",
            ["kairouan", "mosquée", "islam"],
            "Information sur Kairouan"
        )
        
        # Test 15: Plongée
        self.test_question(
            "Où puis-je faire de la plongée sous-marine?",
            ["plongée", "tabarka", "djerba"],
            "Spots de plongée"
        )
        
        self.print_summary()
    
    def print_summary(self):
        """Affiche le résumé des tests."""
        total_tests = self.passed_tests + self.failed_tests
        success_rate = (self.passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print("\n" + "="*80)
        print("📊 RÉSUMÉ DES TESTS")
        print("="*80)
        print(f"Tests réussis: {self.passed_tests}/{total_tests}")
        print(f"Tests échoués: {self.failed_tests}/{total_tests}")
        print(f"Taux de réussite: {success_rate:.1f}%")
        
        if self.failed_tests > 0:
            print("\n❌ Tests échoués:")
            for result in self.test_results:
                if not result['success']:
                    print(f"\n  - {result['description']}")
                    print(f"    Question: {result['question']}")
                    print(f"    Mots-clés manquants: {', '.join(result['missing_keywords'])}")
        
        print("\n" + "="*80)
        
        if success_rate >= 80:
            print("✅ VALIDATION RÉUSSIE - Le chatbot fonctionne bien!")
        elif success_rate >= 60:
            print("⚠️  VALIDATION PARTIELLE - Quelques améliorations nécessaires")
        else:
            print("❌ VALIDATION ÉCHOUÉE - Corrections importantes requises")
        
        print("="*80)
    
    def save_results(self, filename: str = "test_results.json"):
        """Sauvegarde les résultats des tests dans un fichier JSON."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                'passed_tests': self.passed_tests,
                'failed_tests': self.failed_tests,
                'total_tests': self.passed_tests + self.failed_tests,
                'success_rate': (self.passed_tests / (self.passed_tests + self.failed_tests) * 100) if (self.passed_tests + self.failed_tests) > 0 else 0,
                'test_results': self.test_results
            }, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Résultats sauvegardés dans {filename}")


def main():
    """Point d'entrée principal."""
    validator = ChatbotValidator()
    validator.run_all_tests()
    validator.save_results()


if __name__ == "__main__":
    main()
