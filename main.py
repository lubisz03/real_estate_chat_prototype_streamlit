import streamlit as st
import time

from chat_scenario import chat_scenario


def stream(message: str):
    for word in message.split(' '):
        yield word + ' '
        time.sleep(0.1)


if 'chat_messages' not in st.session_state:
    st.session_state.disabled = False
    st.session_state.index = 0
    st.session_state.chat_messages = [chat_scenario[st.session_state.index]]
    st.chat_message("ai").write_stream(
        stream(chat_scenario[st.session_state.index]['content']))


def send_message_sequence(user_input):
    st.session_state.disabled = True
    if st.session_state.index + 1 < len(chat_scenario):
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_input
        })

    for message in st.session_state.chat_messages:
        if message['role'] == "ai":
            offer = message.get('offer', None)
            with st.chat_message(message['role']):
                st.write(message['content'])
                if offer is not None:
                    for offer in offer:
                        st.write(offer['title'])
                        st.write(offer['description'])
                        st.image(offer['image'], use_container_width=True)
                        st.markdown(f"[Zobacz ofertę]({offer['url']})")
        else:
            st.chat_message(message['role']).write(message['content'])

    if st.session_state.index + 2 < len(chat_scenario):
        st.session_state.chat_messages.append(
            chat_scenario[st.session_state.index + 2])
        with st.chat_message(chat_scenario[st.session_state.index + 2]['role']):
            st.write_stream(
                stream(chat_scenario[st.session_state.index + 2]['content']))

            offer = chat_scenario[st.session_state.index +
                                  2].get('offer', None)
            if offer is not None:
                for offer in offer:
                    st.write(stream(offer['title']))
                    st.write_stream(stream(offer['description']))
                    st.image(offer['image'], use_container_width=True)
                    st.markdown(f"[Zobacz ofertę]({offer['url']})")

    st.session_state.index += 2
    st.session_state.disabled = False


user_input = st.chat_input(
    "Type your message", disabled=st.session_state.disabled)
if user_input and not st.session_state.disabled:
    send_message_sequence(user_input)
