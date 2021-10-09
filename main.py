import streamlit as st
from Reflections import *
from Pairs import *
from ChatBot import *


if "R" not in st.session_state:
    st.session_state['R'] = ChatBot(pairs, reflections)
insurance_chat_bot = st.session_state['R']

st.header("Wiki bảo hiểm")

user_input = st.text_input("What's in your mind?")
answer = insurance_chat_bot.response(user_input)

user_requests = insurance_chat_bot.get_user_requests()
bot_responses = insurance_chat_bot.get_bot_responses()
n = len(user_requests)

if n >= 1:
    for i in range(n):
        st.write("User >> ", user_requests[i])
        st.write("Bot >> ", bot_responses[i])
        st.write('\n')


