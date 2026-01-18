"""
Demo script for Tunisia Tourism Chatbot
Demonstrates various chatbot capabilities
"""

from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.chatbot import TunisiaChatbot


def print_separator(title=""):
    """Print a formatted separator."""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    else:
        print("-" * 60)


def run_demo():
    """Run demonstration conversations."""
    
    # Initialize chatbot
    data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
    chatbot = TunisiaChatbot(str(data_path))
    
    # Demo conversations
    demo_queries = [
        {
            "title": "1. GREETING & HELP",
            "queries": [
                "Bonjour",
                "Aide"
            ]
        },
        {
            "title": "2. DESTINATION INFORMATION",
            "queries": [
                "Parlez-moi de Djerba",
                "Qu'est-ce qu'il y a à Sousse?",
                "Je veux visiter Tozeur"
            ]
        },
        {
            "title": "3. ACTIVITY RECOMMENDATIONS",
            "queries": [
                "Quelles plages me recommandez-vous?",
                "Je veux faire un safari dans le désert",
                "Que puis-je faire à Tunis?"
            ]
        },
        {
            "title": "4. ACCOMMODATION REQUESTS",
            "queries": [
                "Hôtels à Hammamet",
                "Où dormir à Sousse?",
                "Hébergements à Djerba"
            ]
        },
        {
            "title": "5. FAQ & PRACTICAL INFORMATION",
            "queries": [
                "Ai-je besoin d'un visa?",
                "Quelle est la meilleure période pour visiter?",
                "Quelle langue parle-t-on en Tunisie?",
                "Comment se déplacer?",
                "Comment est la devise?"
            ]
        }
    ]
    
    # Run demos
    for demo_section in demo_queries:
        print_separator(demo_section["title"])
        
        for query in demo_section["queries"]:
            print(f"👤 Utilisateur: {query}")
            response = chatbot.chat(query)
            print(f"🤖 Chatbot: {response}")
            print_separator()
    
    # Summary
    print_separator("CONVERSATION SUMMARY")
    history = chatbot.get_conversation_history()
    print(f"Total exchanges: {len(history)}")
    print(f"\nDemo completed successfully!")


if __name__ == "__main__":
    try:
        run_demo()
    except Exception as e:
        print(f"Demo error: {e}")
        import traceback
        traceback.print_exc()
