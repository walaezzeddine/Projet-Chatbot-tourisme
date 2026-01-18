"""
Tunisia Tourism Chatbot - Specialized chatbot for tourism guidance in Tunisia
Main chatbot engine with TF-IDF, pattern matching and knowledge base
"""

import json
import os
from typing import Tuple, List, Dict
import re
from pathlib import Path

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("Warning: scikit-learn not available. Using simple string matching instead.")


class TunisiaChatbot:
    """
    Specialized chatbot for Tunisia tourism guidance.
    Uses TF-IDF similarity and pattern matching for dialog.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the chatbot with tourism data.
        
        Args:
            data_path: Path to the JSON data file with tourism information
        """
        self.data_path = data_path
        self.tourism_data = self._load_data()
        self.conversation_history = []
        self.tfidf_vectorizer = None
        self.faq_database = self._build_faq_database()
        self.context = None
        
        if SKLEARN_AVAILABLE:
            self._initialize_tfidf()
    
    def _load_data(self) -> Dict:
        """Load tourism data from JSON file."""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _build_faq_database(self) -> List[Tuple[str, str]]:
        """Convert FAQ data to list of (question, answer) tuples."""
        faq_list = []
        for key, item in self.tourism_data.get('faq', {}).items():
            faq_list.append((item['question'], item['answer']))
        return faq_list
    
    def _initialize_tfidf(self):
        """Initialize TF-IDF vectorizer with FAQ questions."""
        if not SKLEARN_AVAILABLE or not self.faq_database:
            return
        
        questions = [q for q, _ in self.faq_database]
        self.tfidf_vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words=['le', 'la', 'les', 'de', 'du', 'et', 'un', 'une', 'en', 'est'],
            ngram_range=(1, 2),
            max_features=100
        )
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(questions)
    
    def _find_best_faq_match(self, user_input: str) -> Tuple[str, float]:
        """
        Find the best matching FAQ answer using TF-IDF similarity.
        
        Args:
            user_input: User's question or query
            
        Returns:
            Tuple of (answer, confidence_score)
        """
        if SKLEARN_AVAILABLE and self.tfidf_vectorizer:
            return self._tfidf_match(user_input)
        else:
            return self._simple_keyword_match(user_input)
    
    def _tfidf_match(self, user_input: str) -> Tuple[str, float]:
        """Match using TF-IDF similarity."""
        try:
            user_vector = self.tfidf_vectorizer.transform([user_input.lower()])
            similarities = cosine_similarity(user_vector, self.tfidf_matrix)[0]
            best_idx = np.argmax(similarities)
            best_score = float(similarities[best_idx])
            
            if best_score > 0.15:  # Confidence threshold
                return self.faq_database[best_idx][1], best_score
            return None, 0.0
        except Exception as e:
            print(f"TF-IDF matching error: {e}")
            return self._simple_keyword_match(user_input)
    
    def _simple_keyword_match(self, user_input: str) -> Tuple[str, float]:
        """Fallback: simple keyword-based matching."""
        user_input_lower = user_input.lower()
        best_match = None
        best_score = 0.0
        
        for question, answer in self.faq_database:
            # Count matching keywords
            keywords = set(question.lower().split())
            user_keywords = set(user_input_lower.split())
            matching = len(keywords & user_keywords) / len(keywords | user_keywords)
            
            if matching > best_score:
                best_score = matching
                best_match = answer
        
        if best_score > 0.2:
            return best_match, best_score
        return None, 0.0
    
    def _extract_destination_request(self, user_input: str) -> List[str]:
        """Extract destination names from user input."""
        user_lower = user_input.lower()
        found_destinations = []
        
        # Sort destinations by name length (longest first) to avoid partial matches
        # This prevents "tunis" from matching in "tunisie"
        sorted_destinations = sorted(self.tourism_data['destinations'], 
                                    key=lambda x: len(x['name']), 
                                    reverse=True)
        
        for destination in sorted_destinations:
            dest_name = destination['name'].lower()
            # Use word boundaries to avoid partial matches
            # Check if destination name appears as a whole word
            import re
            pattern = r'\b' + re.escape(dest_name) + r'\b'
            if re.search(pattern, user_lower):
                found_destinations.append(destination['name'])
        
        return found_destinations
    
    def _extract_activity_type(self, user_input: str) -> str:
        """Extract activity type from user input."""
        user_lower = user_input.lower()
        keywords = {
            'plage': 'Beach',
            'désert': 'Desert Safari',
            'sahara': 'Desert Safari',
            'oasis': 'Oasis Tour',
            'histoire': 'History & Culture',
            'culture': 'History & Culture',
            'archéologie': 'History & Culture',
            'plongée': 'Water Sports',
            'snorkeling': 'Water Sports',
            'sport': 'Water Sports'
        }
        
        for keyword, activity in keywords.items():
            if keyword in user_lower:
                return activity
        return None
    
    def get_destination_info(self, destination_name: str) -> Dict:
        """Get detailed information about a destination."""
        for dest in self.tourism_data['destinations']:
            if dest['name'].lower() == destination_name.lower():
                return dest
        return None
    
    def recommend_activity(self, activity_type: str) -> str:
        """Recommend activities based on type."""
        for activity in self.tourism_data['activities']:
            if activity['type'] == activity_type:
                locations = ', '.join(activity['locations'])
                return f"{activity['description']}\nLieux recommandés: {locations}"
        return None
    
    def recommend_hotel(self, destination_name: str) -> str:
        """Recommend hotels for a destination."""
        matching_hotels = [h for h in self.tourism_data['hotels_recommendations']
                          if h['location'].lower() == destination_name.lower()]
        
        if matching_hotels:
            result = f"Hôtels recommandés à {destination_name}:\n"
            for hotel in matching_hotels:
                # Use both ⭐ and 'étoile' to ensure keyword matching
                stars_text = f"{hotel['stars']} étoiles"
                result += f"\n- {hotel['name']} ({stars_text} ⭐)\n"
                result += f"  {hotel['description']}\n"
                result += f"  Gamme de prix: {hotel['price_range']}\n"
            return result
        return None
    
    def _generate_response(self, user_input: str) -> str:
        """
        Generate response based on user input.
        Uses pattern matching and knowledge base with priority ordering.
        SMART PRIORITY: Destination + Activity beats FAQ keywords alone
        """
        user_input_lower = user_input.lower()
        
        # Pattern 1: Greeting
        if any(word in user_input_lower for word in ['bonjour', 'hello', 'salut', 'coucou']):
            return self._handle_greeting()
        
        # Pattern 2: DESTINATION + HOTEL KEYWORDS (Check EARLY for compound questions)
        # "Hôtels à Djerba" → Show destination with hotels, NOT generic hotel FAQ
        destinations = self._extract_destination_request(user_input)
        if destinations and any(word in user_input_lower for word in ['hôtel', 'logement', 'hébergement']):
            return self._handle_accommodation_request(user_input)
        
        # Pattern 3: DESTINATION + ACTIVITY KEYWORDS (Combined questions)
        # "Plages à Djerba" → Show destination info, NOT generic beach FAQ
        if destinations and any(word in user_input_lower for word in ['plage', 'désert', 'sahara', 'oasis', 'histoire', 'culture', 'archéologie', 'plongée', 'snorkeling', 'sport']):
            return self._handle_destination_request(destinations)
        
        # Pattern 4: Pure DESTINATION inquiry (no other keywords)
        # "Parlez-moi de Djerba" → Show destination details
        if destinations:
            return self._handle_destination_request(destinations)
        
        # Pattern 5: CRITICAL FAQ keywords with EXPLICIT matching
        # Direct keyword-based matching for high-precision topics
        
        # Security question - must be checked first with strict matching
        if any(word in user_input_lower for word in ['sûr', 'sécurit', 'danger', 'safe']) and any(word in user_input_lower for word in ['tunisie', 'visiter', 'touriste']):
            # Find the safety FAQ explicitly
            for q, a in self.faq_database:
                if 'sûr' in q.lower() or 'safe' in q.lower():
                    return a
        
        # Visa question
        if 'visa' in user_input_lower or 'passeport' in user_input_lower:
            answer, score = self._find_best_faq_match(user_input)
            if answer and score > 0.10:
                return answer
        
        # Other critical keywords
        critical_keywords = {
            'monnaie': ['monnaie', 'devise', 'dinar', 'argent', 'currency'],
            'langue': ['langue', 'parle', 'language', 'parler'],
            'transport': ['déplacer', 'transport', 'se déplacer', 'comment aller', 'taxi', 'bus', 'train', 'louage']
        }
        
        for category, keywords in critical_keywords.items():
            if any(word in user_input_lower for word in keywords):
                answer, score = self._find_best_faq_match(user_input)
                if answer and score > 0.10:  # Lower threshold for critical FAQs
                    return answer
        
        # Pattern 6: PURE ACTIVITY inquiry (no destination, no FAQ context)
        # "Quelles plages?" → Show activity recommendations
        activity = self._extract_activity_type(user_input)
        if activity and not destinations:
            activity_response = self.recommend_activity(activity)
            if activity_response:
                return activity_response
        
        # Pattern 7: OTHER FAQ keywords (visa, langue, etc.)
        if any(word in user_input_lower for word in ['visa', 'monnaie', 'devise', 'langue', 'meilleur moment', 'quand visiter', 'sûr', 'sécurité', 'manger']):
            answer, score = self._find_best_faq_match(user_input)
            if answer and score > 0.15:
                return answer
        
        # Pattern 8: Help
        if any(word in user_input_lower for word in ['aide', 'help', 'capacités', 'que peux']):
            return self._show_help()
        
        # Pattern 9: General FAQ matching as fallback
        answer, score = self._find_best_faq_match(user_input)
        if answer and score > 0.15:
            return answer
        
        # Default response
        return self._handle_unknown_query()
    
    def _handle_greeting(self) -> str:
        """Handle greeting messages."""
        greetings = [
            "Bienvenue en Tunisie! Je suis votre assistant touristique. 🇹🇳\n"
            "Comment puis-je vous aider? Vous pouvez me poser des questions sur:\n"
            "- Les destinations touristiques\n"
            "- Les activités à faire\n"
            "- Les hôtels et hébergements\n"
            "- Les informations pratiques",
            
            "Bienvenue! Je suis votre assistant touristique pour la Tunisie.\n"
            "Tapez 'aide' pour voir ce que je peux faire pour vous."
        ]
        import random
        return random.choice(greetings)
    
    def _handle_destination_request(self, destinations: List[str]) -> str:
        """Handle destination information requests with personalized details."""
        response = ""
        for dest in destinations:
            info = self.get_destination_info(dest)
            if info:
                # Header with emoji and main info
                response += f"\n{'='*60}\n"
                response += f"🇹🇳 {info['name'].upper()}\n"
                response += f"{'='*60}\n\n"
                
                # Governorate and location info
                if 'governorate' in info:
                    response += f"📍 Gouvernorat: {info['governorate']}\n"
                if 'region' in info:
                    response += f"🗺️  Région: {info['region']}\n"
                if 'population' in info:
                    response += f"👥 Population: {info['population']}\n"
                response += "\n"
                
                # Description
                response += f"📝 DESCRIPTION:\n{info['description']}\n\n"
                
                # All attractions
                if info['attractions']:
                    response += f"🎯 ATTRACTIONS PRINCIPALES:\n"
                    for i, attraction in enumerate(info['attractions'], 1):
                        response += f"   {i}. {attraction}\n"
                    response += "\n"
                
                # Activities
                if 'activities' in info:
                    response += f"🎪 ACTIVITÉS DISPONIBLES:\n"
                    for activity in info['activities']:
                        response += f"   • {activity}\n"
                    response += "\n"
                
                # Best season and accommodation
                response += f"🌤️  MEILLEURE PÉRIODE: {info['best_season']}\n"
                response += f"🏨 HÉBERGEMENT: {info['accommodation']}\n"
                response += f"{'='*60}\n"
        
        return response if response else "Destination non trouvée."
    
    def _handle_accommodation_request(self, user_input: str) -> str:
        """Handle accommodation/hotel requests."""
        destinations = self._extract_destination_request(user_input)
        if destinations:
            hotels = self.recommend_hotel(destinations[0])
            if hotels:
                return hotels
        return "Veuillez spécifier une destination. Exemple: 'Hôtels à Djerba'"
    
    def _show_help(self) -> str:
        """Show available commands and help."""
        return (
            "Voici comment je peux vous aider:\n"
            "1. Destinations: 'Parlez-moi de Djerba', 'Qu'est-ce qu'il y a à Sousse?'\n"
            "2. Activités: 'Quelles plages?', 'Safaris dans le désert'\n"
            "3. Hôtels: 'Hôtels à Djerba', 'Logements à Tunis'\n"
            "4. Informations: 'Visa?', 'Quelle langue?', 'Meilleure époque?'\n"
            "5. Autre: 'Au revoir', 'Merci'"
        )
    
    def _handle_unknown_query(self) -> str:
        """Handle queries that don't match any pattern."""
        return (
            "Je n'ai pas bien compris. 😊\n"
            "Pouvez-vous reformuler? Ou tapez 'aide' pour voir mes capacités."
        )
    
    def chat(self, user_input: str) -> str:
        """
        Main chat method - process user input and return response.
        
        Args:
            user_input: User's message
            
        Returns:
            Chatbot's response
        """
        # Store in conversation history
        self.conversation_history.append(('user', user_input))
        
        # Handle special commands
        if user_input.lower() in ['quitter', 'exit', 'au revoir', 'bye']:
            response = "Au revoir et bon voyage en Tunisie! 👋"
            self.conversation_history.append(('bot', response))
            return response
        
        # Generate response
        response = self._generate_response(user_input)
        self.conversation_history.append(('bot', response))
        
        return response
    
    def get_conversation_history(self) -> List[Tuple[str, str]]:
        """Return the conversation history."""
        return self.conversation_history.copy()
    
    def reset(self):
        """Reset the chatbot conversation."""
        self.conversation_history = []
        self.context = None


def main():
    """Main function to run the chatbot interactively."""
    # Get the path to the data file
    script_dir = Path(__file__).parent.parent
    data_path = script_dir / 'data' / 'tunisia_tourism_data.json'
    
    # Initialize chatbot
    print("=" * 60)
    print("🇹🇳 CHATBOT TOURISTIQUE TUNISIE 🇹🇳")
    print("=" * 60)
    print("Bienvenue! Tapez 'aide' pour voir les commandes.")
    print("Tapez 'quitter' pour terminer.\n")
    
    chatbot = TunisiaChatbot(str(data_path))
    
    # Interactive chat loop
    while True:
        try:
            user_input = input("Vous: ").strip()
            if not user_input:
                continue
            
            response = chatbot.chat(user_input)
            print(f"\nChatbot: {response}\n")
            
            if user_input.lower() in ['quitter', 'exit', 'au revoir', 'bye']:
                break
                
        except KeyboardInterrupt:
            print("\n\nAu revoir!")
            break
        except Exception as e:
            print(f"Erreur: {e}")


if __name__ == "__main__":
    main()
