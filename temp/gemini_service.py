"""
Simple Gemini AI Service
"""

from google.generativeai import GenerativeModel
import google.generativeai as genai
import config

class GeminiService:
    """Simple wrapper for Gemini API"""
    
    def __init__(self):
        """Initialize Gemini"""
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = GenerativeModel(model_name=config.GEMINI_MODEL)
        print(f"✓ Gemini initialized: {config.GEMINI_MODEL}")
    
    def generate(self, prompt: str) -> str:
        """Generate text from prompt"""
        response = self.model.generate_content(contents=prompt)
        return response.text


# Singleton
_service = None

def get_gemini_service():
    global _service
    if _service is None:
        _service = GeminiService()
    return _service


# Test
if __name__ == "__main__":
    print("Testing Gemini...")
    service = get_gemini_service()
    
    result = service.generate("Say hello in one word")
    print(f"Result: {result}")
    print("✓ Test passed!")
