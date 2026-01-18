"""Simple test for repetitive answers"""
from src.chatbot import TunisiaChatbot
from pathlib import Path

data_path = Path('data/tunisia_tourism_data.json')
bot = TunisiaChatbot(str(data_path))

print("TEST: Beaches (should give activity recommendation)\n")
ans1 = bot.chat("Quelles sont les plages?")
print("Answer 1:")
print(ans1)

bot2 = TunisiaChatbot(str(data_path))
print("\n" + "="*70)
print("TEST: Different beach question\n")
ans2 = bot2.chat("Où puis-je me baigner?")
print("Answer 2:")
print(ans2)

print("\n" + "="*70)
print("COMPARISON:")
print(f"Answer 1 == Answer 2: {ans1 == ans2}")
print(f"Answer 1 length: {len(ans1)}")
print(f"Answer 2 length: {len(ans2)}")
