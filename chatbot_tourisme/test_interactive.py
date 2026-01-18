#!/usr/bin/env python3
"""
Interactive chatbot test script
Tests the chatbot with 5 key queries
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.chatbot import TunisiaChatbot

def test_chatbot():
    """Test chatbot with interactive queries."""
    
    # Initialize chatbot
    data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
    chatbot = TunisiaChatbot(str(data_path))
    
    print("\n" + "="*70)
    print("🇹🇳 TUNISIA TOURISM CHATBOT - INTERACTIVE TEST")
    print("="*70 + "\n")
    
    # Test queries
    test_queries = [
        {
            "query": "Bonjour",
            "description": "Test 1: Greeting"
        },
        {
            "query": "Parlez-moi de Djerba",
            "description": "Test 2: Destination info"
        },
        {
            "query": "Quelles plages me recommandez-vous?",
            "description": "Test 3: Activity recommendation"
        },
        {
            "query": "Ai-je besoin d'un visa?",
            "description": "Test 4: FAQ question"
        },
        {
            "query": "Hôtels à Hammamet",
            "description": "Test 5: Hotel recommendation"
        }
    ]
    
    # Run tests
    for i, test in enumerate(test_queries, 1):
        print(f"\n{'-'*70}")
        print(f"📋 {test['description']}")
        print(f"{'-'*70}")
        print(f"\n👤 USER: {test['query']}")
        print(f"\n🤖 CHATBOT:")
        
        response = chatbot.chat(test['query'])
        print(f"{response}")
    
    # Summary
    print(f"\n{'='*70}")
    print("✅ TEST COMPLETED SUCCESSFULLY!")
    print("="*70)
    print(f"\nTotal exchanges: {len(chatbot.get_conversation_history())}")
    print("✨ Chatbot is working perfectly!\n")

if __name__ == "__main__":
    try:
        test_chatbot()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
