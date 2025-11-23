import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class ContentAgent:
    """
    Generates educational content using Google Gemini AI.
    Adapts based on learning style and accessibility needs.
    """
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.5-flash')


    
    def generate(self, context):
        style = context.get("style", "simple")
        topic = context.get("topic", "Science")
        learner = context.get("learner", "Student")
        accessibility = context.get("accessibility", "none")
        
        if not topic or topic.strip() == "":
            return "❌ ContentAgent: Please specify a topic."
        
        # Build AI prompt
        prompt = f"""You are an expert educational tutor. Create a {style} explanation of {topic} for a student named {learner}.

Learning Style: {style}
- If 'simple': Use clear, easy language suitable for beginners
- If 'visual': Include visual analogies, metaphors, and imagine-able descriptions
- If 'detailed': Provide comprehensive explanation with examples and real-world applications

Accessibility Need: {accessibility}
- If 'dyslexia': Use short sentences (max 15 words), simple vocabulary, clear structure
- If 'audio': Write in conversational, listening-friendly style
- If 'none': Standard educational writing

Create an engaging, accurate explanation now (200-300 words):"""

        try:
            response = self.model.generate_content(prompt)
            return f"📚 **{learner}'s Learning Content:**\n\n{response.text}"
        except Exception as e:
            return f"❌ ContentAgent Error: {str(e)}\n\nFalling back to basic explanation: {topic} is an important concept worth exploring."
