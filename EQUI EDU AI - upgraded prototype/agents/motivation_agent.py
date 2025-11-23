import random

class MotivationAgent:
    """
    Provides encouragement and maintains engagement.
    """
    def motivate(self, context):
        learner = context.get("learner", "friend")
        topic = context.get("topic", "this subject")
        
        messages = [
            f"💪 Keep going, {learner}! Learning {topic} takes effort, but you're making great progress.",
            f"🌟 {learner}, every question you ask brings you closer to mastering {topic}!",
            f"🚀 You've got this, {learner}! {topic} might seem challenging now, but you're building valuable skills.",
            f"✨ Great work exploring {topic}, {learner}! Curiosity is the first step to excellence.",
            f"🎯 {learner}, your dedication to understanding {topic} is impressive. Stay focused!",
            f"💡 {learner}, remember: every expert was once a beginner in {topic}. You're on the right path!"
        ]
        
        return random.choice(messages)


