# AI fitness

 Personal AI Fitness Coach
A conversational AI fitness assistant built with Streamlit and powered by LLaMA 3.3 70B via the Groq API. Get instant, evidence-based advice on workouts, nutrition, and recovery — all in a sleek dark-themed chat interface.

 Features

Real-time AI chat powered by LLaMA 3.3 70B (via Groq)
Focus area selector — Strength, Cardio, Flexibility, HIIT, Nutrition
Quick action chips for instant common queries
Daily fitness tips in the sidebar
Full conversation memory within a session
Responsive dark UI with custom styling


 Tech Stack
LayerTechnologyFrontendStreamlitAI ModelLLaMA 3.3 70B (Groq)LanguagePython 3.8+APIGroq Cloud API

 Prerequisites
Before running this project, make sure you have:

Python 3.8 or higher installed
A free Groq API key from console.groq.com
pip (Python package manager)


 Installation & Setup
Step 1 — Clone or Download the project
bash# If using git
git clone https://github.com/yourusername/fitness-coach.git
cd fitness-coach

# Or just navigate to the folder where fitness_coach.py is saved
cd path/to/your/project
Step 2 — Install dependencies
bashpip install streamlit groq
Step 3 — Add your API key
Open fitness_coach.py and replace the placeholder with your Groq API key:
pythonclient = Groq(api_key="gsk_your_actual_key_here")

 How to Run
Windows
Open Command Prompt or PowerShell, navigate to the project folder, and run:
cmdcd C:\path\to\your\project
python -m streamlit run fitness_coach.py
Then open your browser and go to: http://localhost:8501

macOS
Open Terminal, navigate to the project folder, and run:
bashcd /path/to/your/project
python3 -m streamlit run fitness_coach.py
Then open your browser and go to: http://localhost:8501

Linux
Open a terminal, navigate to the project folder, and run:
bashcd /path/to/your/project
python3 -m streamlit run fitness_coach.py
Then open your browser and go to: http://localhost:8501

Android (via Termux)
Install Termux from F-Droid, then run:
bashpkg update && pkg upgrade
pkg install python
pip install streamlit groq
cd /path/to/project
python -m streamlit run fitness_coach.py
Open your mobile browser and go to: http://localhost:8501

 Getting a Free Groq API Key

Go to console.groq.com
Sign up with any email (no credit card needed)
Click API Keys in the top navigation
Click Create API key, give it a name
Copy the key — it starts with gsk_...
Paste it into fitness_coach.py


Free tier limit: 14,400 requests/day — more than enough for personal use.


 Project Structure
fitness/
│
├── fitness_coach.py      # Main application file
└── README.md             # This file

 Troubleshooting
streamlit not recognized
bash# Use this instead
python -m streamlit run fitness_coach.py
ModuleNotFoundError: No module named 'groq'
bashpip install groq
429 RESOURCE_EXHAUSTED error
Your API key has hit its rate limit. Wait a few minutes and try again, or generate a new key from console.groq.com.
Port already in use
bashpython -m streamlit run fitness_coach.py --server.port 8502

 Author
Mukul Rajput
B.Tech CSE — AI Essentials Project

 License
This project is for educational purposes as part of a B.Tech CSE coursework submission.
