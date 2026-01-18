"""Test to diagnose why answers are repetitive"""
from src.chatbot import TunisiaChatbot
from pathlib import Path

# Initialize
data_path = Path('data/tunisia_tourism_data.json')
bot = TunisiaChatbot(str(data_path))

# Test multiple similar questions
print("=" * 70)
print("TEST 1: Different ways to ask about beaches")
print("=" * 70)

q1 = "Quelles sont les plages?"
print(f"\nQ1: {q1}")
print(f"A1: {bot.chat(q1)}\n")

q2 = "Où puis-je me baigner?"
print(f"\nQ2: {q2}")
print(f"A2: {bot.chat(q2)}\n")

q3 = "Parlez-moi des plages en Tunisie"
print(f"\nQ3: {q3}")
print(f"A3: {bot.chat(q3)}\n")

print("=" * 70)
print("TEST 2: Different ways to ask about visa")
print("=" * 70)

q4 = "Ai-je besoin d'un visa?"
print(f"\nQ4: {q4}")
print(f"A4: {bot.chat(q4)}\n")

q5 = "Visa requirements"
print(f"\nQ5: {q5}")
print(f"A5: {bot.chat(q5)}\n")

q6 = "Comment obtenir un visa?"
print(f"\nQ6: {q6}")
print(f"A6: {bot.chat(q6)}\n")

print("=" * 70)
print("TEST 3: Greetings (should vary)")
print("=" * 70)

for i in range(3):
    greeting = ["Bonjour", "Hello", "Salut"][i]
    print(f"\n{i+1}. {greeting}")
    print(f"Response: {bot.chat(greeting)}\n")

print("=" * 70)
print("TEST 4: Check FAQ database")
print("=" * 70)

print(f"\nTotal FAQ questions: {len(bot.faq_database)}")
for i, (q, a) in enumerate(bot.faq_database, 1):
    print(f"{i}. Q: {q[:50]}...")
