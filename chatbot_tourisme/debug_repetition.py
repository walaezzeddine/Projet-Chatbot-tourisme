"""Debug the FAQ keyword issue"""
from src.chatbot import TunisiaChatbot
from pathlib import Path

data_path = Path('data/tunisia_tourism_data.json')
bot = TunisiaChatbot(str(data_path))

# Check the FAQ keywords dictionary
print("FAQ KEYWORDS IN CODE:")
print("-" * 70)

faq_keywords = {
    'déplacer': 'transport',
    'transport': 'transport',
    'se déplacer': 'transport',
    'comment aller': 'transport',
    'comment se': 'transport',
    'taxi': 'transport',
    'bus': 'transport',
    'train': 'transport',
    'louage': 'transport',
    'avion': 'transport',
    'visa': 'visa',
    'monnaie': 'currency',
    'devise': 'currency',
    'langue': 'language',
    'meilleur moment': 'best_time',
    'quand visiter': 'best_time',
    'sûr': 'safety',
    'sécurité': 'safety',
    'plage': 'beaches',
    'manger': 'food',
    'hôtel': 'hotels',
    'activité': 'activities'
}

print(f"Total keywords: {len(faq_keywords)}")
print(f"Keywords: {list(faq_keywords.keys())}")

print("\n" + "=" * 70)
print("ISSUE: 'plage' is in faq_keywords!")
print("=" * 70)

print("\nWhen user asks: 'Quelles sont les plages?'")
print("1. Pattern 2 finds 'plage' keyword")
print("2. Calls _find_best_faq_match()")
print("3. Returns FAQ answer about beaches")
print("4. SKIPS Pattern 4 (Activity check)")
print("\nResult: ✓ Correct! (happens to work)")

print("\n" + "=" * 70)
print("PROBLEM: Multiple keywords in same question!")
print("=" * 70)

print("\nWhen user asks: 'Comment puis-je visiter les plages à Djerba?'")
print("Keywords found in order:")

test_input = "Comment puis-je visiter les plages à Djerba?"
test_lower = test_input.lower()

for keyword in faq_keywords.keys():
    if keyword in test_lower:
        print(f"  - '{keyword}' found → matches FAQ '{faq_keywords[keyword]}'")

print("\nResult: First matching keyword triggers FAQ!")
print("This may not be what user wanted...")

print("\n" + "=" * 70)
print("ROOT CAUSE OF REPETITION:")
print("=" * 70)
print("""
1. FAQ keyword matching runs BEFORE destination matching
2. If ANY FAQ keyword is found, it returns FAQ answer
3. This prevents showing personalized destination info
4. Multiple questions with same keyword → same answer

Example:
- "Quelles plages à Djerba?" → Returns FAQ (not destination details)
- "Où se baigner?" → Might match 'sûr' (safety) or fail → Default answer
- "Plages Hammamet?" → Returns FAQ (not destination details)
""")

print("\nSOLUTION:")
print("Need to check if question is about a DESTINATION + keyword")
print("If destination + activity keyword → Show destination with that activity")
print("If ONLY keyword (no destination) → Show FAQ answer")
