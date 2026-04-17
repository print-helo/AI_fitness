import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
client = Groq(api_key="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")

SYSTEM_PROMPT = "You are an expert AI Fitness Coach. Provide safe, domain-specific workout and nutrition advice. If asked about non-fitness topics, politely redirect the user back to fitness."

# --- PAGE CONFIG ---
st.set_page_config(page_title="FitAI Coach", page_icon="💪", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Hide Streamlit defaults */
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}

/* Root Variables */
:root {
    --bg: #0a0a0f;
    --surface: #111118;
    --card: #16161f;
    --border: #ffffff10;
    --accent: #e8ff47;
    --accent2: #ff6b35;
    --text: #f0f0f0;
    --muted: #888899;
}

body, .stApp {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * {color: var(--text) !important;}

/* Main layout wrapper */
.main-wrapper {
    display: flex;
    flex-direction: column;
    height: 100vh;
    max-width: 860px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Hero Header */
.hero {
    padding: 40px 0 24px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 8px;
}
.hero-badge {
    display: inline-block;
    background: var(--accent);
    color: #000;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 12px;
    text-transform: uppercase;
}
.hero-title {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: clamp(48px, 8vw, 80px) !important;
    line-height: 0.9 !important;
    color: var(--text) !important;
    margin: 0 0 8px !important;
    letter-spacing: 1px;
}
.hero-title span {color: var(--accent);}
.hero-sub {
    font-size: 13px;
    color: var(--muted);
    letter-spacing: 0.5px;
}

/* Stats bar */
.stats-bar {
    display: flex;
    gap: 24px;
    padding: 16px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 16px;
}
.stat {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    color: var(--muted);
}
.stat-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 8px var(--accent);
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% {opacity: 1; transform: scale(1);}
    50% {opacity: 0.5; transform: scale(0.8);}
}

/* Quick action chips */
.chips-label {
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

/* Chat messages */
.chat-area {
    flex: 1;
    overflow-y: auto;
    padding: 8px 0 16px;
}

[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 8px 0 !important;
}

/* User messages */
[data-testid="stChatMessage"][data-testid*="user"] .stMarkdown,
.stChatMessage:has([data-testid="chatAvatarIcon-user"]) [data-testid="stMarkdownContainer"] p {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px 16px 4px 16px !important;
    padding: 12px 16px !important;
}

/* Message container styling */
[data-testid="stChatMessageContent"] {
    background: var(--card) !important;
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
    padding: 14px 18px !important;
}

/* Avatar icons */
[data-testid="chatAvatarIcon-user"] {
    background: var(--accent) !important;
    color: #000 !important;
}
[data-testid="chatAvatarIcon-assistant"] {
    background: var(--accent2) !important;
    color: #fff !important;
}

/* Chat input */
[data-testid="stChatInput"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 4px 8px !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px var(--accent)22 !important;
}
[data-testid="stChatInput"] textarea {
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: var(--muted) !important;
}

/* Bottom send button */
[data-testid="stChatInputSubmitButton"] svg {
    fill: var(--accent) !important;
}

/* Buttons */
.stButton button {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    color: var(--muted) !important;
    border-radius: 20px !important;
    font-size: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
    padding: 6px 14px !important;
    transition: all 0.2s !important;
    cursor: pointer !important;
}
.stButton button:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
    background: var(--accent)11 !important;
}

/* Scrollbar */
::-webkit-scrollbar {width: 4px;}
::-webkit-scrollbar-track {background: transparent;}
::-webkit-scrollbar-thumb {background: var(--border); border-radius: 4px;}

/* Sidebar content */
.sidebar-section {
    padding: 20px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 4px;
}
.sidebar-title {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 12px;
}
.tip-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 8px;
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
}
.tip-card strong {color: var(--accent); font-size: 11px; letter-spacing: 1px; text-transform: uppercase;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("""
    <div style="padding: 24px 0 0;">
        <div style="font-family: 'Bebas Neue', sans-serif; font-size: 28px; color: #e8ff47; letter-spacing: 1px;">FITAI</div>
        <div style="font-size: 11px; color: #888899; margin-top: 2px;">Your Personal Coach</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-section">
        <div class="sidebar-title">Today's Tips</div>
        <div class="tip-card"><strong>💧 Hydration</strong><br>Drink 500ml water before your workout for peak performance.</div>
        <div class="tip-card"><strong>😴 Recovery</strong><br>Muscles grow during rest. Aim for 7–9 hours of sleep.</div>
        <div class="tip-card"><strong>🥗 Protein</strong><br>Target 1.6–2.2g of protein per kg of bodyweight daily.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-section">
        <div class="sidebar-title">Focus Areas</div>
    </div>
    """, unsafe_allow_html=True)

    focus = st.radio("", ["🏋️ Strength", "🏃 Cardio", "🧘 Flexibility", "⚡ HIIT", "🥗 Nutrition"], label_visibility="collapsed")

    st.markdown(f"""
    <div style="margin-top: 16px; padding: 12px; background: #e8ff4711; border: 1px solid #e8ff4733; border-radius: 10px;">
        <div style="font-size: 11px; color: #e8ff47; font-weight: 600;">Active Focus</div>
        <div style="font-size: 14px; color: #f0f0f0; margin-top: 4px;">{focus}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- MAIN CONTENT ---
st.markdown("""
<div class="main-wrapper">
    <div class="hero">
        <div class="hero-badge">AI Powered · Always On</div>
        <div class="hero-title">YOUR PERSONAL<br><span>FITNESS</span> COACH</div>
        <div class="hero-sub">B.Tech CSE AI Essentials Project — Mukul Rajput</div>
    </div>
    <div class="stats-bar">
        <div class="stat"><div class="stat-dot"></div> Online & Ready</div>
        <div class="stat">⚡ LLaMA 3.3 70B</div>
        <div class="stat">🔒 Safe & Evidence-Based</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick action chips
st.markdown('<div class="chips-label">Quick Questions</div>', unsafe_allow_html=True)
cols = st.columns(4)
quick_prompts = [
    "💪 Build muscle fast",
    "🔥 Burn belly fat",
    "🏃 Beginner cardio plan",
    "🥗 High protein meals",
]
for i, (col, qp) in enumerate(zip(cols, quick_prompts)):
    with col:
        if st.button(qp, key=f"chip_{i}"):
            st.session_state.quick_input = qp.split(" ", 1)[1]

st.markdown("<div style='height: 8px'></div>", unsafe_allow_html=True)

# --- CHAT STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "quick_input" not in st.session_state:
    st.session_state.quick_input = None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Welcome message if no chat yet
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("👋 Hey! I'm your **AI Fitness Coach**. I can help you with workout plans, nutrition advice, and recovery tips. What's your fitness goal today?")

# Handle quick input
if st.session_state.quick_input:
    prompt = st.session_state.quick_input
    st.session_state.quick_input = None

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    focus_context = f"The user is currently focused on: {focus}. "
    with st.chat_message("assistant"):
        with st.spinner(""):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": focus_context + SYSTEM_PROMPT},
                    *st.session_state.messages
                ],
                temperature=0.3,
                max_tokens=500,
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

# Chat input
if prompt := st.chat_input("Ask about workouts, diet, recovery, or routines..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    focus_context = f"The user is currently focused on: {focus}. "
    with st.chat_message("assistant"):
        with st.spinner(""):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": focus_context + SYSTEM_PROMPT},
                    *st.session_state.messages
                ],
                temperature=0.3,
                max_tokens=500,
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()