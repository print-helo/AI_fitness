import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
client = Groq(api_key="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")

SYSTEM_PROMPT = "You are an expert AI Fitness Coach. Provide safe, domain-specific workout and nutrition advice. If asked about non-fitness topics, politely redirect the user back to fitness."

# --- UI SETUP ---
st.set_page_config(page_title="AI Fitness Pro")
st.title(" Personal AI Fitness Coach")
st.subheader("B.Tech CSE AI Essentials Project - Mukul")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask about workouts, diet, or routines..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *st.session_state.messages
        ],
        temperature=0.3,
        max_tokens=500,
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)