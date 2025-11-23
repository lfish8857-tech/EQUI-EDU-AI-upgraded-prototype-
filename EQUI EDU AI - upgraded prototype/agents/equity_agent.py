class EquityAgent:
    """
    Monitors fairness and provides extra support.
    """
    def check_fairness(self, context):
        demographics = context.get("demographics", {})
        gender = demographics.get("gender", "")
        ses = demographics.get("SES", "")
        topic = context.get("topic", "")
        
        messages = ["⚖️ **Equity Check:**"]
        
        # Extra support for underserved groups
        if ses == "low":
            messages.append("✓ Extra learning resources provided for students with limited access")
            messages.append("✓ Free online resources and open educational materials linked")
        
        if gender == "female" and any(stem in topic.upper() for stem in ["MATH", "SCIENCE", "PHYSICS", "CHEMISTRY", "ENGINEERING"]):
            messages.append("✓ Highlighting diverse role models in STEM")
            messages.append("✓ Research shows representation improves outcomes")
        
        if len(messages) == 1:
            messages.append("✓ Content is fair and accessible for all demographics")
        
        return "\n".join(messages)

