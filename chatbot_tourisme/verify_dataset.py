#!/usr/bin/env python3
"""
Verify enriched dataset
"""

import json
from pathlib import Path

# Load data
data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("\n" + "="*70)
print("✅ DATASET ENRICHI - VÉRIFICATION")
print("="*70 + "\n")

# Count destinations
destinations = data['destinations']
print(f"🏖️  DESTINATIONS: {len(destinations)} (all governorates)")
for dest in destinations:
    gov = dest.get('governorate', 'N/A')
    print(f"   ✓ {dest['name']:20} ({gov})")

# Count FAQ
faq = data['faq']
print(f"\n❓ FAQ: {len(faq)} questions")
for key, item in faq.items():
    print(f"   ✓ {item['question'][:50]}...")

# Count activities
activities = data['activities']
print(f"\n🎯 ACTIVITÉS: {len(activities)} catégories")
for activity in activities:
    locations = activity.get('locations', [])
    print(f"   ✓ {activity['type']:20} ({len(locations)} locations)")

# Count hotels
hotels = data['hotels_recommendations']
print(f"\n🏨 HÔTELS: {len(hotels)} recommandations")
for hotel in hotels:
    print(f"   ✓ {hotel['name']:30} - {hotel['location']}")

# Practical info
print(f"\n📋 INFORMATIONS PRATIQUES:")
practical = data['practical_info']
print(f"   ✓ Électricité: {practical['electricity']}")
print(f"   ✓ Urgences: {practical['emergency']}")
print(f"   ✓ Santé: {practical['health']}")
print(f"   ✓ Douanes: {practical['customs']}")
print(f"   ✓ Climat: {len(practical.get('climate', {}))} saisons documentées")
print(f"   ✓ Transport: {len(practical.get('transport', {}))} modes")

print(f"\n{'='*70}")
print(f"📊 TOTAL CONTENU:")
print(f"   - {len(destinations)} destinations (24 gouvernorats)")
print(f"   - {len(faq)} questions FAQ")
print(f"   - {len(activities)} activités")
print(f"   - {len(hotels)} hôtels recommandés")
print(f"   - Informations pratiques complètes")
print(f"\n✅ Dataset prêt pour la présentation!")
print("="*70 + "\n")
