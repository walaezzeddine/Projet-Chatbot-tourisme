"""Test transportation and FAQ responses"""
from src.chatbot import TunisiaChatbot
from pathlib import Path

# Initialize
data_path = Path('data/tunisia_tourism_data.json')
bot = TunisiaChatbot(str(data_path))

print("=" * 70)
print("TEST 1: Transportation question")
print("=" * 70)
print("Q: sur quoi je peux déplacer en tunisie")
print("\nA:")
print(bot.chat("sur quoi je peux déplacer en tunisie"))

print("\n" + "=" * 70)
print("TEST 2: Another transport question")
print("=" * 70)
print("Q: comment se déplacer?")
print("\nA:")
print(bot.chat("comment se déplacer?"))

print("\n" + "=" * 70)
print("TEST 3: Visa question (FAQ)")
print("=" * 70)
print("Q: ai-je besoin d'un visa?")
print("\nA:")
print(bot.chat("ai-je besoin d'un visa?"))

print("\n" + "=" * 70)
print("TEST 4: Destination (should still work)")
print("=" * 70)
print("Q: Parlez-moi de Djerba")
print("\nA:")
print(bot.chat("Parlez-moi de Djerba"))

print("\n" + "=" * 70)
print("TEST 5: Best time (FAQ)")
print("=" * 70)
print("Q: Quel est le meilleur moment pour visiter?")
print("\nA:")
print(bot.chat("Quel est le meilleur moment pour visiter?"))
