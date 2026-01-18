"""Test the improved non-repetitive chatbot"""
from src.chatbot import TunisiaChatbot
from pathlib import Path

data_path = Path('data/tunisia_tourism_data.json')

print("=" * 70)
print("TEST 1: Destination + Activity (COMBINED)")
print("=" * 70)

bot = TunisiaChatbot(str(data_path))
q1 = "Quelles plages à Djerba?"
print(f"\nQ: {q1}")
a1 = bot.chat(q1)
print(f"A: {a1[:200]}...\n")

print("=" * 70)
print("TEST 2: Pure Activity (no destination)")
print("=" * 70)

bot = TunisiaChatbot(str(data_path))
q2 = "Quelles sont les plages?"
print(f"\nQ: {q2}")
a2 = bot.chat(q2)
print(f"A: {a2[:200]}...\n")

print("=" * 70)
print("TEST 3: Destination + Hotel")
print("=" * 70)

bot = TunisiaChatbot(str(data_path))
q3 = "Hôtels à Hammamet?"
print(f"\nQ: {q3}")
a3 = bot.chat(q3)
print(f"A: {a3[:200]}...\n")

print("=" * 70)
print("TEST 4: Pure Transport FAQ (no destination)")
print("=" * 70)

bot = TunisiaChatbot(str(data_path))
q4 = "Comment se déplacer en Tunisie?"
print(f"\nQ: {q4}")
a4 = bot.chat(q4)
print(f"A: {a4[:200]}...\n")

print("=" * 70)
print("TEST 5: Destination only")
print("=" * 70)

bot = TunisiaChatbot(str(data_path))
q5 = "Parlez-moi de Kairouan"
print(f"\nQ: {q5}")
a5 = bot.chat(q5)
print(f"A: {a5[:250]}...\n")

print("=" * 70)
print("TEST 6: Different Destination + Activity")
print("=" * 70)

bot = TunisiaChatbot(str(data_path))
q6 = "Désert à Tozeur"
print(f"\nQ: {q6}")
a6 = bot.chat(q6)
print(f"A: {a6[:200]}...\n")

print("=" * 70)
print("RESULT: Are answers different?")
print("=" * 70)
print(f"Test 1 == Test 2: {a1 == a2} (Should be False)")
print(f"Test 3 == Test 4: {a3 == a4} (Should be False)")
print(f"Test 1 == Test 5: {a1 == a5} (Should be False)")
