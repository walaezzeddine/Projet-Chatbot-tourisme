"""
Unit tests for Tunisia Tourism Chatbot
Tests the main functionality and NLP components
"""

import unittest
import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.chatbot import TunisiaChatbot


class TestTunisiaChatbot(unittest.TestCase):
    """Test cases for TunisiaChatbot class."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
        cls.chatbot = TunisiaChatbot(str(data_path))
    
    def test_data_loading(self):
        """Test that tourism data is loaded correctly."""
        self.assertIsNotNone(self.chatbot.tourism_data)
        self.assertIn('destinations', self.chatbot.tourism_data)
        self.assertIn('faq', self.chatbot.tourism_data)
        self.assertIn('activities', self.chatbot.tourism_data)
    
    def test_faq_database(self):
        """Test FAQ database construction."""
        self.assertGreater(len(self.chatbot.faq_database), 0)
        for question, answer in self.chatbot.faq_database:
            self.assertIsInstance(question, str)
            self.assertIsInstance(answer, str)
            self.assertGreater(len(question), 0)
            self.assertGreater(len(answer), 0)
    
    def test_destination_extraction(self):
        """Test destination name extraction from user input."""
        # Test single destination
        dests = self.chatbot._extract_destination_request("Djerba")
        self.assertIn("Djerba", dests)
        
        # Test multiple destinations
        dests = self.chatbot._extract_destination_request("Je veux visiter Tunis et Sousse")
        self.assertGreaterEqual(len(dests), 1)
        
        # Test case insensitivity
        dests = self.chatbot._extract_destination_request("djerba")
        self.assertIn("Djerba", dests)
    
    def test_destination_info(self):
        """Test destination information retrieval."""
        info = self.chatbot.get_destination_info("Djerba")
        self.assertIsNotNone(info)
        self.assertEqual(info['name'], 'Djerba')
        self.assertIn('description', info)
        self.assertIn('attractions', info)
        self.assertIn('best_season', info)
    
    def test_activity_extraction(self):
        """Test activity type extraction."""
        # Beach
        activity = self.chatbot._extract_activity_type("Je veux aller à la plage")
        self.assertEqual(activity, "Beach")
        
        # Desert Safari
        activity = self.chatbot._extract_activity_type("Safari dans le désert")
        self.assertEqual(activity, "Desert Safari")
        
        # History - keyword-based test
        activity = self.chatbot._extract_activity_type("Visite archéologie")
        self.assertIsNotNone(activity)
    
    def test_hotel_recommendation(self):
        """Test hotel recommendation retrieval."""
        hotels = self.chatbot.recommend_hotel("Hammamet")
        self.assertIsNotNone(hotels)
        self.assertIn("Hammamet", hotels)
    
    def test_activity_recommendation(self):
        """Test activity recommendation."""
        activity_rec = self.chatbot.recommend_activity("Beach")
        self.assertIsNotNone(activity_rec)
        self.assertIn("plage", activity_rec.lower())
    
    def test_faq_matching(self):
        """Test FAQ matching with TF-IDF or keyword matching."""
        # Test visa question
        answer, score = self.chatbot._find_best_faq_match("Ai-je besoin d'un visa?")
        self.assertIsNotNone(answer)
        self.assertGreater(score, 0)
        self.assertIn("visa", answer.lower())
        
        # Test currency question
        answer, score = self.chatbot._find_best_faq_match("Quelle est la monnaie?")
        self.assertIsNotNone(answer)
        self.assertGreater(score, 0)
    
    def test_greeting_response(self):
        """Test greeting response."""
        response = self.chatbot._handle_greeting()
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_help_response(self):
        """Test help message."""
        response = self.chatbot._show_help()
        self.assertIsNotNone(response)
        self.assertIn("Destinations", response)
    
    def test_chat_basic(self):
        """Test basic chat functionality."""
        response = self.chatbot.chat("Bonjour")
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_chat_destination(self):
        """Test chat with destination request."""
        response = self.chatbot.chat("Parlez-moi de Djerba")
        self.assertIsNotNone(response)
        self.assertIn("Djerba", response)
    
    def test_conversation_history(self):
        """Test conversation history tracking."""
        chatbot = TunisiaChatbot(str(Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'))
        initial_count = len(chatbot.get_conversation_history())
        
        chatbot.chat("Bonjour")
        chatbot.chat("Djerba")
        
        history = chatbot.get_conversation_history()
        self.assertEqual(len(history), initial_count + 4)  # 2 user + 2 bot
    
    def test_reset(self):
        """Test conversation reset."""
        self.chatbot.chat("Test message")
        self.chatbot.reset()
        history = self.chatbot.get_conversation_history()
        self.assertEqual(len(history), 0)
    
    def test_unknown_query_handling(self):
        """Test handling of unknown queries."""
        response = self.chatbot._handle_unknown_query()
        self.assertIsNotNone(response)
        self.assertIn("compris", response.lower())
    
    def test_multiple_destinations_in_query(self):
        """Test extraction of multiple destinations."""
        response = self.chatbot.chat("Que puis-je faire à Tunis et Sousse?")
        self.assertIsNotNone(response)
    
    def test_case_insensitivity(self):
        """Test case insensitive matching."""
        response1 = self.chatbot.chat("djerba")
        response2 = self.chatbot.chat("DJERBA")
        response3 = self.chatbot.chat("Djerba")
        
        self.assertIn("Djerba", response1)
        self.assertIn("Djerba", response2)
        self.assertIn("Djerba", response3)


class TestDataIntegrity(unittest.TestCase):
    """Test data integrity and completeness."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
        cls.chatbot = TunisiaChatbot(str(data_path))
    
    def test_all_destinations_have_info(self):
        """Test that all destinations have complete information."""
        for dest in self.chatbot.tourism_data['destinations']:
            self.assertIn('name', dest)
            self.assertIn('description', dest)
            self.assertIn('attractions', dest)
            self.assertIn('best_season', dest)
            self.assertGreater(len(dest['attractions']), 0)
    
    def test_all_activities_have_locations(self):
        """Test that activities have locations."""
        for activity in self.chatbot.tourism_data['activities']:
            self.assertIn('type', activity)
            self.assertIn('locations', activity)
            self.assertGreater(len(activity['locations']), 0)
    
    def test_hotels_valid(self):
        """Test hotel data integrity."""
        for hotel in self.chatbot.tourism_data['hotels_recommendations']:
            self.assertIn('name', hotel)
            self.assertIn('location', hotel)
            self.assertIn('stars', hotel)
    
    def test_faq_completeness(self):
        """Test FAQ entries are complete."""
        faq = self.chatbot.tourism_data['faq']
        for key, item in faq.items():
            self.assertIn('question', item)
            self.assertIn('answer', item)
            self.assertGreater(len(item['question']), 0)
            self.assertGreater(len(item['answer']), 0)


class TestNLPFunctionality(unittest.TestCase):
    """Test NLP-specific functionality."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures."""
        data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
        cls.chatbot = TunisiaChatbot(str(data_path))
    
    def test_tfidf_vectorizer_exists(self):
        """Test TF-IDF vectorizer is properly initialized if sklearn available."""
        if self.chatbot.tfidf_vectorizer is not None:
            self.assertIsNotNone(self.chatbot.tfidf_matrix)
    
    def test_keyword_matching_fallback(self):
        """Test keyword matching fallback works."""
        answer, score = self.chatbot._simple_keyword_match("monnaie tunisie")
        if answer:
            self.assertGreater(score, 0)
    
    def test_similarity_scores_reasonable(self):
        """Test that similarity scores are in valid range."""
        answer, score = self.chatbot._find_best_faq_match("visa")
        if answer:
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 1)


def run_tests():
    """Run all tests with verbose output."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestTunisiaChatbot))
    suite.addTests(loader.loadTestsFromTestCase(TestDataIntegrity))
    suite.addTests(loader.loadTestsFromTestCase(TestNLPFunctionality))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
