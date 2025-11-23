# EQUI EDU AI - Multi-Agent Learning Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎓 Project Overview

**EQUI EDU AI** is a production-ready, multi-agent educational platform designed to deliver personalized, accessible, and equitable learning experiences for every student. Built as a capstone project demonstrating Level 3 Multi-Agent Orchestration with real AI integration.

### Key Features

✅ **Multi-Agent Orchestration** - Five specialized agents working together  
✅ **AI-Powered Content** - Uses Google Gemini API for intelligent explanations  
✅ **Accessibility Support** - Dyslexia-friendly formatting and audio content  
✅ **Equity Monitoring** - Automatic fairness checks across demographics  
✅ **Session Memory** - Tracks learning history and progress  
✅ **Media Upload** - Support for images and audio files  
✅ **Web Interface** - Clean, intuitive Streamlit UI  

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/lfish8857-tech/EQUI-EDU-AI-upgraded-prototype-
cd EQUI_EDU_AI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API key**

Create a `.env` file in the project root:
```
GEMINI_API_KEY=your-api-key-here
```

Get your free API key at: https://makersuite.google.com/app/apikey

4. **Run the application**
```bash
streamlit run streamlit_app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
EQUI_EDU_AI/
│
├── agents/                          # Specialized agent modules
│   ├── content_agent.py            # Generates explanations
│   ├── assessment_agent.py         # Creates quizzes
│   ├── accessibility_agent.py      # Ensures accessibility
│   ├── equity_agent.py             # Monitors fairness
│   └── motivation_agent.py         # Provides encouragement
│
├── streamlit_app.py                # Main application (UI + Orchestrator)
├── requirements.txt                # Python dependencies
├── .env                            # API keys (create this)
├── .gitignore                      # Git ignore file
└── README.md                       # This file
```

---

## 🎯 How It Works

### The Multi-Agent System

EQUI EDU AI uses a **collaborative multi-agent architecture** where each agent specializes in one aspect of educational support:

1. **Orchestrator Agent** (in `streamlit_app.py`)
   - Coordinates all other agents
   - Routes requests based on user needs
   - Combines responses into coherent output

2. **Content Agent** (`agents/content_agent.py`)
   - Generates educational explanations
   - Adapts to learning styles (simple, visual, detailed)
   - Personalizes content based on accessibility needs

3. **Assessment Agent** (`agents/assessment_agent.py`)
   - Creates fair, unbiased quizzes
   - Generates multiple question types
   - Includes answer keys

4. **Accessibility Agent** (`agents/accessibility_agent.py`)
   - Ensures content meets WCAG standards
   - Provides dyslexia-friendly formatting
   - Supports audio learning modes

5. **Equity Agent** (`agents/equity_agent.py`)
   - Monitors demographic fairness
   - Provides extra support for underserved groups
   - Tracks achievement gaps

6. **Motivation Agent** (`agents/motivation_agent.py`)
   - Maintains learner engagement
   - Provides personalized encouragement
   - Celebrates progress

### User Flow

```
User Input → Orchestrator → Multiple Agents → Combined Response → Display
     ↓                                                              ↓
  Context                                                    Session Memory
```

---

## 💡 Example Usage

### Basic Content Request

1. Enter your name: "Sarah"
2. Topic: "Photosynthesis"
3. Learning style: "visual"
4. Accessibility: "none"
5. Click "Get AI Learning Help!"

**Result:** AI-generated visual explanation of photosynthesis

### Dyslexia-Friendly Content

1. Select accessibility: "dyslexia"
2. Submit your request
3. See content displayed with:
   - 22px font size
   - Extra line spacing (2.5)
   - Yellow background for contrast
   - Clear, simple language

### With Media Upload

1. Upload a diagram (JPG/PNG)
2. Upload audio explanation (MP3/WAV)
3. Submit request
4. See your media displayed alongside AI-generated content

---

## 🛠️ Configuration

### Environment Variables

Create a `.env` file with:

```bash
# Google Gemini API (Required)
GEMINI_API_KEY=your-gemini-api-key

# Optional: Other AI providers
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-claude-key
```

### Switching AI Models

To use a different Gemini model, edit `agents/content_agent.py`:

```python
# Current (Gemini 1.5 Flash - fastest)
self.model = genai.GenerativeModel('gemini-1.5-flash')

# Alternative (Gemini 1.5 Pro - more capable)
self.model = genai.GenerativeModel('gemini-1.5-pro')
```

---

## 🎨 Customization

### Adding New Agents

1. Create a new file in `agents/` folder:
```python
# agents/translation_agent.py
class TranslationAgent:
    def translate(self, context):
        # Your logic here
        return translated_content
```

2. Import in `streamlit_app.py`:
```python
from agents.translation_agent import TranslationAgent
```

3. Add to orchestrator:
```python
self.translation = TranslationAgent()
```

### Customizing UI

Edit `streamlit_app.py` to:
- Change color schemes
- Add new form fields
- Modify layout
- Add new features

---

## 📊 Features in Detail

### Accessibility Support

- **Dyslexia Mode**: Large text (22px), extra spacing, high contrast
- **Audio Support**: Upload and playback audio content
- **Visual Learning**: Image upload for diagrams and visual aids
- **Multiple Formats**: Content adapts to different needs

### Equity Features

- **Demographic Monitoring**: Tracks fairness across gender, SES, etc.
- **Extra Support**: Provides additional resources for underserved groups
- **Bias Detection**: Flags potential unfair content
- **Achievement Gap Tracking**: Monitors learning disparities

### Session Management

- **History Tracking**: Saves last 3 sessions
- **Context Awareness**: Remembers learner preferences
- **Progress Monitoring**: Tracks learning journey
- **Export Ready**: Can be extended to save data

---

## 🧪 Testing

### Manual Testing

Test different scenarios:

1. **Basic Functionality**
   - Topic: "Water Cycle"
   - Style: "simple"
   - Accessibility: "none"

2. **Accessibility Test**
   - Topic: "Solar System"
   - Style: "visual"
   - Accessibility: "dyslexia"

3. **Equity Test**
   - Gender: "female"
   - SES: "low"
   - Topic: "Physics"

4. **Media Upload**
   - Upload image
   - Upload audio
   - Verify display

### Expected Behavior

✅ AI generates relevant, accurate content  
✅ Dyslexia mode shows formatted text  
✅ Equity agent provides extra support  
✅ Media displays correctly  
✅ Session history tracks inputs  

---

## 🚧 Known Limitations

- **API Costs**: Gemini free tier has rate limits (60 requests/min)
- **Offline Mode**: Requires internet connection for AI features
- **File Storage**: Uploaded files not permanently saved
- **Language**: Currently English only
- **Browser Compatibility**: Best on Chrome/Edge/Firefox

---

## 📈 Future Enhancements

- [ ] Add more AI providers (OpenAI, Claude, Llama)
- [ ] Implement persistent storage (database)
- [ ] Add user authentication
- [ ] Support multiple languages
- [ ] Mobile app version
- [ ] Real-time collaboration features
- [ ] Advanced analytics dashboard
- [ ] Teacher portal for monitoring
- [ ] Parent/guardian access


---

## 🤝 Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

### Guidelines

- Follow existing code style
- Add comments for complex logic
- Test all changes
- Update README if needed

---


## 📞 Support & Contact

- **Issues**: Open an issue on GitHub
- **Questions**: Create a discussion thread
- **Email**: shadowhacklegiontestmail@gmail.com

---

## 🙏 Acknowledgments

- **Google Gemini AI** - For providing free AI API
- **Streamlit** - For the amazing web framework
- **Anthropic** - For agent design inspiration
- **Open Source Community** - For tools and libraries


---

**Built with ❤️ for educational equity | Powered by Google Gemini AI**
 
**Last Updated:** November 2025  
**Status:** Production-Ready Prototype
