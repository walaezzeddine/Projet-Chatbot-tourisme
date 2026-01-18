# 🇹🇳 TUNISIA CHATBOT - COMPLETE PIPELINE

## 1️⃣ INPUT LAYER - User Message Arrives

```
User Input (Text)
        ↓
    "Parlez-moi de Djerba"
```

---

## 2️⃣ PREPROCESSING LAYER

```
User Input
    ↓
Convert to lowercase
    ↓
"parlez-moi de djerba"
    ↓
Store in conversation_history
```

**Code Location:** `chat()` method, line 348

---

## 3️⃣ PATTERN MATCHING LAYER (Priority Order)

This is the **CORE** of the chatbot - it checks patterns in this exact order:

### Pattern 1: GREETING CHECK
```
Is input like: "bonjour", "hello", "salut", "coucou"?
    ↓ YES
    └─→ _handle_greeting() 
            └─→ Return random welcome message
            
    ↓ NO
    └─→ Continue to Pattern 2
```

**Code:** Line 210

---

### Pattern 2: FAQ KEYWORDS CHECK (PRIORITY!)
```
Does input contain FAQ keywords?
Examples: 'déplacer', 'transport', 'visa', 'monnaie', 'langue', etc.

    ↓ YES (Keyword found)
    └─→ Run TF-IDF matching
            └─→ Compare with FAQ database
            └─→ If score > 0.15
                    └─→ Return FAQ answer
    
    ↓ NO (No FAQ keyword)
    └─→ Continue to Pattern 3
```

**Code:** Lines 219-251

**FAQ Keywords Dictionary:**
```python
{
    'déplacer': transport
    'transport': transport
    'visa': visa
    'monnaie': currency
    'langue': language
    'meilleur moment': best_time
    'plage': beaches (but NOT if part of destination)
    ...etc
}
```

---

### Pattern 3: DESTINATION CHECK
```
Does input mention a destination name?
Examples: "Djerba", "Tunis", "Kairouan", "Tozeur"

    ↓ YES (Destination found)
    └─→ _extract_destination_request()
            └─→ Loop through 27 destinations
            └─→ Check if name is in user input
            └─→ Return matching destinations
    
    ↓ Destination found
    └─→ _handle_destination_request()
            ├─→ Get destination info from JSON
            ├─→ Format with governorate, region, population
            ├─→ Add all attractions
            ├─→ Add activities
            ├─→ Add best season & accommodation
            └─→ Return formatted response
    
    ↓ NO destination
    └─→ Continue to Pattern 4
```

**Code:** Lines 253-256

**Example Output:**
```
============================================================
🇹🇳 DJERBA
============================================================

📍 Gouvernorat: Médenine
🗺️  Région: Sud-Est

📝 DESCRIPTION:
Île méditerranéenne célèbre pour ses plages de sable blanc...

🎯 ATTRACTIONS PRINCIPALES:
   1. Musée du Linge Traditionnel
   2. Île de Flamingo
   ... (all 6 attractions)

🎪 ACTIVITÉS DISPONIBLES:
   • Plages
   • Culture
   • Détente

🌤️  MEILLEURE PÉRIODE: Avril à Octobre
🏨 HÉBERGEMENT: Hôtels 3-5 étoiles, Resorts
============================================================
```

---

### Pattern 4: ACTIVITY CHECK
```
Does input mention an activity type?
Examples: 'plage', 'désert', 'oasis', 'histoire', 'plongée'

Activity Keywords:
{
    'plage': Beach,
    'désert': Desert Safari,
    'sahara': Desert Safari,
    'oasis': Oasis Tour,
    'histoire': History & Culture,
    'culture': History & Culture,
    'archéologie': History & Culture,
    'plongée': Water Sports,
    'snorkeling': Water Sports,
    'sport': Water Sports
}

    ↓ YES (Activity found)
    └─→ recommend_activity(activity_type)
            └─→ Find activity in database
            └─→ Get all locations for that activity
            └─→ Return description + locations
    
    ↓ NO activity
    └─→ Continue to Pattern 5
```

**Code:** Lines 258-261

**Example:**
```
Input: "Quelles plages?"
↓
Activity found: "Beach"
↓
Output: "Plages méditerranéennes avec eaux turquoise
Lieux recommandés: Djerba, Hammamet, Sousse, Mahdia, Monastir, Îles Kerkennah"
```

---

### Pattern 5: HOTEL/ACCOMMODATION CHECK
```
Does input contain hotel keywords?
Examples: 'hôtel', 'logement', 'hébergement', 'accommodation'

    ↓ YES
    └─→ _handle_accommodation_request()
            ├─→ Extract destination from input
            ├─→ Find hotels for that destination
            └─→ Return formatted hotel info
    
    ↓ NO
    └─→ Continue to Pattern 6
```

**Code:** Lines 263-265

**Example:**
```
Input: "Hôtels à Djerba"
↓
Hotels found: 
- Djerba Plaza Hotel & Spa (4⭐)
  Resort moderne avec vue mer, spa et piscine
  Gamme de prix: Moyenne
  Amenities: Plage privée, Spa, Restaurant, Piscine
```

---

### Pattern 6: HELP CHECK
```
Does input contain help keywords?
Examples: 'aide', 'help', 'capacités', 'que peux'

    ↓ YES
    └─→ _show_help()
            └─→ Return list of available commands
    
    ↓ NO
    └─→ Continue to Pattern 7
```

**Code:** Lines 267-269

---

### Pattern 7: GENERAL FAQ FALLBACK
```
No specific pattern matched?
Try general TF-IDF matching against ALL FAQ questions

    ↓
    └─→ _find_best_faq_match(user_input)
            ├─→ Vectorize user input with TF-IDF
            ├─→ Compare with all FAQ question vectors
            ├─→ Get highest similarity score
            └─→ If score > 0.15
                    └─→ Return matching FAQ answer
    
    ↓ Score too low (<0.15)
    └─→ Continue to Pattern 8
```

**Code:** Lines 271-275

---

### Pattern 8: DEFAULT/UNKNOWN
```
No pattern matched at all!

    ↓
    └─→ _handle_unknown_query()
            └─→ Return friendly "I didn't understand" message
```

**Code:** Lines 277-279

---

## 4️⃣ TF-IDF NLP MATCHING (INSIDE FAQ CHECK)

When FAQ match is needed, here's what happens:

```
User Input: "Ai-je besoin d'un visa?"
    ↓
Step 1: Vectorization (TF-IDF)
    └─→ Convert question to numerical vector
    └─→ Remove stop words (le, la, de, etc.)
    └─→ Use n-grams (1-2 word combinations)
    
    ↓
Step 2: Similarity Calculation
    └─→ Compare with 10 FAQ questions in database
    └─→ Calculate cosine similarity for each
    └─→ Find highest similarity
    
    ↓
Step 3: Confidence Check
    └─→ If similarity_score > 0.15 (threshold)
            └─→ MATCH FOUND ✓
            └─→ Return FAQ answer
    └─→ Else
            └─→ Try keyword fallback
    
    ↓
FAQ Answer: "Les ressortissants de l'UE, Suisse, Norvège..."
```

**Code:** Lines 89-106

---

## 5️⃣ DATA FLOW ARCHITECTURE

```
                    INCOMING USER TEXT
                            ↓
                    ┌─────────────────────────┐
                    │  CHATBOT.PY PIPELINE    │
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  1. Greeting Check      │
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  2. FAQ Keywords Check  │ ← TF-IDF Vectorizer
                    │     (PRIORITY!)         │
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  3. Destination Check   │ ← 27 Destinations
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  4. Activity Check      │ ← 10 Activities
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  5. Hotel Check         │ ← 8 Hotels
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  6. Help Check          │
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  7. General FAQ Match   │ ← TF-IDF
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │  8. Unknown Query       │
                    └─────────────────────────┘
                            ↓
                    ┌─────────────────────────┐
                    │   FORMAT & RETURN       │
                    │   RESPONSE TO USER      │
                    └─────────────────────────┘
                            ↓
                    OUTGOING RESPONSE TEXT
```

---

## 6️⃣ DATA SOURCES

```
TUNISIA_TOURISM_DATA.JSON (15KB local database)
    ├─→ destinations: 27 entries
    │   └─→ Tunis, Carthage, Hammamet, Nabeul, Sousse, Monastir,
    │       Sfax, Djerba, Médenine, Tataouine, Tozeur, Nefta,
    │       Gafsa, Sidi Bouzid, Kairouan, Mahdia, Îles Kerkennah,
    │       Kébili, Kasserine, Le Kef, Béja, Jendouba, Siliana,
    │       Manouba, Ariana, Ben Arous, Zaghouan
    │
    ├─→ faq: 10 Q&A pairs
    │   └─→ visa, currency, language, transport, best_time,
    │       safety, beaches, food, hotels, activities
    │
    ├─→ activities: 10 categories
    │   └─→ Beach, Desert Safari, History & Culture, Oasis Tour,
    │       Water Sports, Mountain Trekking, Local Markets,
    │       Religious Sites, Thermal Springs, Winery Tours
    │
    ├─→ hotels_recommendations: 8 hotels
    │   └─→ With amenities, prices, descriptions
    │
    └─→ practical_info: Transportation, electricity, 
                        climate, banking, etc.
```

---

## 7️⃣ CONVERSATION FLOW EXAMPLE

```
USER: "Parlez-moi de Djerba"
    ↓
CHATBOT PIPELINE:
1. Greeting? NO
2. FAQ keyword? NO (no 'transport', 'visa', etc.)
3. Destination? YES! ("Djerba" found)
    └─→ Extract destination: "Djerba"
    └─→ Get info from JSON
    └─→ Format response with all details
    └─→ Return personalized answer
    ↓
OUTPUT:
============================================================
🇹🇳 DJERBA
============================================================
📍 Gouvernorat: Médenine
🗺️  Région: Sud-Est
📝 DESCRIPTION: Île méditerranéenne célèbre...
🎯 ATTRACTIONS PRINCIPALES: (6 items)
🎪 ACTIVITÉS DISPONIBLES: Plages, Culture, Détente
🌤️  MEILLEURE PÉRIODE: Avril à Octobre
🏨 HÉBERGEMENT: Hôtels 3-5 étoiles, Resorts
============================================================

STORED IN HISTORY:
conversation_history = [
    ('user', 'Parlez-moi de Djerba'),
    ('bot', '============================================================...')
]
```

---

## 8️⃣ KEY ALGORITHMS

### TF-IDF MATCHING
```
Question: "Ai-je besoin d'un visa?"
    ↓
TF-IDF Vectorizer:
- Lowercase: "ai-je besoin d'un visa?"
- Remove stops: "besoin", "visa"
- Create vector with weights
- Compare to 10 FAQ vectors
- Find highest cosine similarity
- Return answer if score > 0.15

Result: Match with FAQ #1 (visa question) ✓
```

### KEYWORD FALLBACK
```
If scikit-learn not available or score too low:
    ├─→ Split question into keywords
    ├─→ Calculate Jaccard similarity
    ├─→ Find best matching FAQ
    ├─→ Return if similarity > 0.2
```

---

## 9️⃣ RESPONSE FORMATTING

```
For Destinations:
├─→ Header with emoji and name
├─→ Governorate + Region + Population
├─→ Full description
├─→ ALL attractions (numbered)
├─→ Activities list (bullet points)
├─→ Best season & accommodation
└─→ Formatted with emojis & separators

For FAQ:
├─→ Direct answer text
└─→ Usually 1-3 sentences

For Activities:
├─→ Description
└─→ Recommended locations (comma-separated)

For Hotels:
├─→ Hotel name + star rating
├─→ Description
├─→ Price range
└─→ List of amenities
```

---

## 🔟 PERFORMANCE METRICS

```
Processing Speed: <50ms per query
TF-IDF Score Range: 0.0 - 1.0
Confidence Threshold: > 0.15
Fallback Threshold: > 0.2
Database Size: 27 destinations + 10 FAQ + 10 activities + 8 hotels
Conversation History: Unlimited (stored in memory)
```

---

## SUMMARY

The chatbot works like a **smart decision tree**:

1. **Check greetings** (simple pattern)
2. **Check FAQ keywords FIRST** (prevent false positives)
3. **Check destinations** (exact name matching)
4. **Check activities** (keyword matching)
5. **Check hotels** (keyword + destination matching)
6. **Check help** (simple pattern)
7. **Try TF-IDF FAQ matching** (NLP algorithm)
8. **Default response** (unknown query)

Each step returns immediately if a match is found, so the response is **fast and contextually correct**! ⚡
