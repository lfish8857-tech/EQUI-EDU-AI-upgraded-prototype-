class AccessibilityAgent:
    """
    Ensures content meets accessibility standards.
    No AI needed - provides formatting guidance.
    """
    def make_accessible(self, context):
        needs = context.get("accessibility", "none")
        
        if needs == "none":
            return ""
        
        messages = {
            "dyslexia": "♿ **Accessibility: Dyslexia Support Active**\n- Using larger text (22px)\n- Extra line spacing (2.0)\n- High-contrast display\n- Clear, simple language\n- Content chunked for easier processing",
            
            "audio": "♿ **Accessibility: Audio Support Active**\n- Text-to-speech optimized\n- Conversational tone for listening\n- Audio player available (if file uploaded)\n- Adjust playback speed as needed"
        }
        
        return messages.get(needs, f"♿ Accessibility mode: {needs} support enabled")
