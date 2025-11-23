import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class AssessmentAgent:
    """
    Creates quizzes and assessments using AI.
    """
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.5-flash')


    
    def generate(self, context):
        topic = context.get("topic", "general knowledge")
        learner = context.get("learner", "Student")
        accessibility = context.get("accessibility", "none")
        
        prompt = f"""Create a 3-question quiz about {topic} for a high school student.

Requirements:
- Mix question types: multiple choice, short answer, application
- Make questions fair and unbiased
- Difficulty: moderate (high school level)
- If accessibility is 'dyslexia': use simple, clear language in questions
- Include correct answers at the end

Format each question clearly with numbers."""

        try:
            response = self.model.generate_content(prompt)
            return f"📝 **Quiz for {learner}:**\n\n{response.text}"
        except Exception as e:
            return f"❌ AssessmentAgent Error: {str(e)}"


