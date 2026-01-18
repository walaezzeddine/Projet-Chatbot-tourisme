"""Debug Test 4 issue"""
from src.chatbot import TunisiaChatbot
from pathlib import Path

data_path = Path('data/tunisia_tourism_data.json')
bot = TunisiaChatbot(str(data_path))

q = "Comment se déplacer en Tunisie?"
print(f"Question: {q}\n")

# Check what it detects
print("Checking destinations:")
destinations = bot._extract_destination_request(q)
print(f"  Destinations found: {destinations}")

print("\nChecking for 'déplacer' keyword:")
print(f"  'déplacer' in question? {'déplacer' in q.lower()}")

print("\nExpected: Show transport FAQ")
print("\nActual answer:")
answer = bot.chat(q)
print(answer[:300])
