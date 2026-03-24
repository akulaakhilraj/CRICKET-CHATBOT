import streamlit as st
from chatbot import get_cricket_response_stream

st.set_page_config(page_title="Cricket Info Chatbot")

st.title(" Cricket News with Chatbot ")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#History
for role, msg in st.session_state.chat_history:
    st.chat_message(role).write(msg)

user_input = st.chat_input("Ask about matches, news, players and stats of the player and more information fo the player...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").write(user_input)

    response_container = st.chat_message("assistant")
    full_response = ""

    with response_container:
        placeholder = st.empty()

        for chunk in get_cricket_response_stream(
            user_input,
            st.session_state.chat_history
        ):
            full_response += chunk
            placeholder.markdown(full_response + " ")

        placeholder.markdown(full_response)

    st.session_state.chat_history.append(("assistant", full_response))