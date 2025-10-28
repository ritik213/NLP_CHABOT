import streamlit as st
from nltk.chat.util import Chat, reflections
import html

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you. What do you need help with?",]
    ],
    [
        r"(.*) your name ?",
        ["My name is The Clever Programmer, but you can just call me Robot. I'm a chatbot!",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well!", "I am great! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind that."]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello!", "Hey there!", "Hi! How can I assist you today?"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse.",]
    ],
    [
        r"(.*)created(.*)",
        ["Prakash created me using Python's NLTK library.", "Top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hyderabad, India']
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2.", "In %2 there is a 50% chance of rain."]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health."]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket!", "I enjoy watching football too!"]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"(.*)(movie|film)(.*)",
        ["I love watching sci-fi movies. What's your favorite movie?", "Interstellar and Inception are my top picks!"]
    ],
    [
        r"(.*)(food|dish)(.*)",
        ["I don’t eat, but I hear biryani is delicious!", "Pizza seems to be everyone’s favorite!"]
    ],
    [
        r"(.*)(AI|artificial intelligence)(.*)",
        ["AI is fascinating! I’m actually built using a small part of it."]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. Have a great day!"]
    ],
    [
        r"(.*)",
        ["Our customer service will reach you soon."]
    ],
]

# Default message
st.set_page_config(page_title="NLTK Chatbot — The Clever Programmer", layout="centered")

# ==============================
# CSS DESIGN — FIX WHITE BACKGROUND ISSUE
# ==============================
st.markdown("""
<style>
body {
    background: #0078ff;
    color: #f8f9fa;
    
[data-testid="stAppViewContainer"] {
    background-color: transparent;
}
#
.user-bubble {
    background-color: #0078ff;
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    margin-bottom: 8px;
    display: inline-block;
    #
}
.bot-bubble {
    background-color: #343a40;
    color: #f8f9fa;
    padding: 10px 15px;
    border-radius: 15px;
    margin-bottom: 8px;
    display: inline-block;
    
}
input, textarea {
    color: black !important;
    box-shadow: 2px 4px 15px rgba(0, 0, 0, 0.12);
   
    
}
h1, {
    color: #ffffff;
    text-align: center;
    
}
</style>
""", unsafe_allow_html=True)

# ==============================
# STREAMLIT UI
# ==============================
st.title("🤖CHATBOT || Your AI Chat Assistant")
#st.markdown("<h3>Type lowercase English to chat. Type 'quit' to exit.</h3>", unsafe_allow_html=True)
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

# Chatbot setup
chat = Chat(pairs, reflections)

# Session to store messages
if "history" not in st.session_state:
    st.session_state.history = []

# User input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    send = st.form_submit_button("Send")

if send and user_input:
    response = chat.respond(user_input)
    if not response:
        response = "I'm sorry, I didn’t get that. Could you rephrase?"
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"<div class='user-bubble'><b>You:</b> {html.escape(message)}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'><b>Bot:</b> {html.escape(message)}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.history = []
