"""Test personalized destination responses"""
from src.chatbot import TunisiaChatbot
from pathlib import Path

# Initialize
data_path = Path('data/tunisia_tourism_data.json')
bot = TunisiaChatbot(str(data_path))

# Test personalized destinations
print("=" * 70)
print("TEST 1: Personalized Djerba Response")
print("=" * 70)
print(bot.chat("Parlez-moi de Djerba"))

print("\n" + "=" * 70)
print("TEST 2: Personalized Kairouan Response")
print("=" * 70)
print(bot.chat("Qu'est-ce qu'il y a à Kairouan?"))

print("\n" + "=" * 70)
print("TEST 3: Personalized Tozeur Response")
print("=" * 70)
print(bot.chat("Informations sur Tozeur"))

print("\n" + "=" * 70)
print("TEST 4: Multiple destinations")
print("=" * 70)
print(bot.chat("Parlez-moi de Tunis et Sousse"))
