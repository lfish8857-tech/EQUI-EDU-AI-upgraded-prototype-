from agents.content_agent import ContentAgent
from agents.assessment_agent import AssessmentAgent
from agents.accessibility_agent import AccessibilityAgent
from agents.equity_agent import EquityAgent
from agents.motivation_agent import MotivationAgent

class OrchestratorAgent:
    def __init__(self):
        self.content = ContentAgent()
        self.assessment = AssessmentAgent()
        self.accessibility = AccessibilityAgent()
        self.equity = EquityAgent()
        self.motivation = MotivationAgent()

    def handle_request(self, intent, context):
        responses = []
        if intent == "content":
            responses.append(self.content.generate(context))
        if intent == "assessment":
            responses.append(self.assessment.generate(context))
        if context.get("accessibility") and context["accessibility"] != "none":
            responses.append(self.accessibility.make_accessible(context))
        responses.append(self.equity.check_fairness(context))
        responses.append(self.motivation.motivate(context))
        return "\n\n".join(responses)

